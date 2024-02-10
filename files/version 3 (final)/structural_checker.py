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

        if not tag["valid"] or tag["tag"] == "":
            str_tag = f"<{'/' * (tag['nature'] == 'CLOSE') + tag['tag']}>"
            errors.append(f"Invalid tag {str_tag} at line {tag['start']}")

        elif tag["nature"] == "CLOSE" and tag["self_closing"]:
            hints.append(f"Self-closing tag <{tag['tag']}> closed (uselessly) at line {tag['start']}")
            continue

        elif tag["nature"] == "OPEN" and not tag["self_closing"]:
            stack.append(tag)

        elif tag["nature"] == "CLOSE" and not stack:
            errors.append(f"Tag </{tag['tag']}> never opened at line {tag['start']}")

        elif not stack:
            continue

        elif tag["nature"] == "CLOSE" and tag["tag"] == stack[-1]["tag"]:
            del stack[-1]

        elif tag["nature"] == "CLOSE" and stack[-1]["tag"] != tag["tag"]:
            str_tag = f"<{'/' * (tag['nature'] == 'CLOSE') + tag['tag']}>"
            errors.append(f"Awaiting </{stack[-1]['tag']}> got {str_tag} at line {tag['start']}")

    errors += [f"Unclosed tag <{'/' * (tag['nature'] == 'CLOSE') + tag['tag']}> at line {tag['start']}" for tag in
               stack]

    return errors, hints