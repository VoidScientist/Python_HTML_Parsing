from tag_list import tags

# ----------------------------------------------------
# This is a basic HTML parser that is supposed to detect errors.
# It was made as homework for the advanced algo course at ESME Sudria.
#
# GROUP MEMBERS: Louis ARCELON, Rémi PICHOT, Raphaël KERVAON, Théo VOREAUX.
#
# Disclaimer : this algorithm is quite rudimentary, poorly optimised, and might let errors slip
# especially those that are related to the javascript parser incorporated in HTML.
#
# Disclaimer 2: i found out by testing on the google main page again structural errors
# might be detected for custom html elements, this could be avoided by simply not caring
# about tag names, so here's the super-parameter:
#
ALLOW_CUSTOM = True
#
# But it passes the google page with lots of obfuscated JS so i'm happy at least.
#
# Data Structures used : stack - queue
# Modus Operandi : Finite State Machine
# ----------------------------------------------------

def check_tag(identifier: str) -> tuple[bool, bool]:
    """
    This function checks if the identifier exists in HTML and if self closing
    :param identifier:
    :return: tuple (VALID?, SELF_CLOSING?)
    """
    valid = True
    self_closing = identifier in tags["self_closing"]

    if not self_closing and not ALLOW_CUSTOM:
        valid = identifier in tags["normal"]

    return valid, self_closing


def parse_content(tag: str) -> tuple[str, str, list[str], bool, bool]:
    """
    This function create the tag dict by checking its function and validity
    :param tag:
    :return tag_dict:
    """

    nature, data = pattern_matching(tag)

    if nature == "ERROR": return nature, None, None, False, False
    if nature == "COMMENT": return nature, None, None, True, True

    identifier, *attributes = data.split(" ")

    if identifier.lower() == "!doctype" and list(map(lambda x: x.lower(), attributes)) == ["html"]:
        return "OPEN", "doctype", "html", True, True

    validity, type = check_tag(identifier)

    return nature, identifier, attributes, validity, type


def pattern_matching(tag: str) -> list[str]:
    """
    This function uses python's structural pattern matching to check the nature and content of a tag.

    :param tag:
    :return A list of form [NATURE, CONTENT] both strings:

    NATURE TYPES : OPEN - CLOSE - COMMENT
    """
    match list(tag):

        case ["<", "/", *content, ">"]:
            return ["CLOSE", "".join(content)]
        case ["<", "!", "-", "-", *content, "-", "-", ">"]:
            return ["COMMENT", "".join(content)]
        case ["<", *content, ">"]:
            return ["OPEN", "".join(content)]
        case _:
            return ["ERROR", f"Tag {tag} can't be at ."]


def parse(f) -> tuple[list[dict], list[str]]:
    """
    This function retrieves all the tags in an HTML file
    :param f: an opened file
    :return: a list of tag represented by dicts (could've used OOP, but since we didn't see it in class : dicts)
    """

    char = f.read(1)

    tag_attributes = ("nature", "tag", "attributes", "valid", "self_closing", "start", "end")

    buffer = []
    risky = ["script", "style"]
    escape_tag = ""

    parse_modes = ["TAG", "SCRIPT", "DEFAULT"]
    current_mode = "DEFAULT"

    errors = []

    char_on_line = 1

    line = 1
    line_start = 1

    tags = []
    tag = ""

    while char:

        if char == "\n":
            line += 1
            char = f.read(1)
            char_on_line = 1
            continue

        match current_mode:

            case "DEFAULT":

                if char == "<":
                    tag = char
                    line_start = line
                    current_mode = "TAG"

                if char == ">":
                    errors.append(f"Tag was never opened at line {line} character {char_on_line}")

            case "TAG":

                tag += char

                if char == "<":
                    errors.append(f"Tag opened inside another at line {line} character {char_on_line}")

                if char == ">":
                    current_mode = "DEFAULT"

                    tag_data = [i for i in parse_content(tag)] + [line_start, line]
                    tag_dict = dict(zip(tag_attributes, tag_data))
                    tags.append(tag_dict)

                    if (tag_dict["tag"] in risky) and tag_dict["nature"] == "OPEN":
                        current_mode = "SCRIPT"
                        escape_tag = "</" + tag_dict["tag"] + ">"

                    tag = ""

            case "SCRIPT":

                if char == "<":
                    i = 0
                    while char == escape_tag[i]:
                        buffer.append(char)
                        char = f.read(1)
                        i += 1
                        if i == len(escape_tag):
                            current_mode = "DEFAULT"
                            buffer.append(char)
                            break
                    else:
                        buffer = []

        if buffer and current_mode != "SCRIPT":
            char = buffer.pop(0)
        else:
            char = f.read(1)

        char_on_line += 1

    return tags, errors
