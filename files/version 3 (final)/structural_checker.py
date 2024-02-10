def check_html_structure(tags: list) -> tuple[list, list]:
    """
    This function checks if all tags are properly written in code.
    :param tags:
    :return errors: lists of errors and hints
    """
    errors = []
    hints = []
    stack = []

    for tag in tags:

        # if tag invalid or empty throw 
        if not tag["valid"] or tag["tag"] == "":
            str_tag = f"<{'/' * (tag['nature'] == 'CLOSE') + tag['tag']}>"
            errors.append(f"UnknownTagError at line {tag['start']}: Invalid tag {str_tag}.")

        elif tag["nature"] == "CLOSE" and tag["self_closing"]:
            hints.append(f"Self-closing tag <{tag['tag']}> closed (uselessly) at line {tag['start']}")
            continue

        elif tag["nature"] == "OPEN" and not tag["self_closing"]:
            stack.append(tag)

        elif tag["nature"] == "CLOSE" and not stack:
            errors.append(f"MismatchedTagError at line {tag['start']}: Tag </{tag['tag']}> never opened.")

        elif not stack:
            continue

        elif tag["nature"] == "CLOSE" and tag["tag"] == stack[-1]["tag"]:
            del stack[-1]

        elif tag["nature"] == "CLOSE" and stack[-1]["tag"] != tag["tag"]:
            str_tag = f"<{'/' * (tag['nature'] == 'CLOSE') + tag['tag']}>"
            errors.append(f"MismatchedTagError at line {tag['start']}: Awaiting </{stack[-1]['tag']}> got {str_tag} instead.")

    errors += [f"MismatchedTagError at line {tag['start']}: Unclosed tag <{'/' * (tag['nature'] == 'CLOSE') + tag['tag']}>." 
    for tag in stack]

    return errors, hints