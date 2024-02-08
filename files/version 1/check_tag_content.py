def check_tag_content(tag: str) -> list[str]:
    """
    FUNCTION THAT CHECKS IF TAG IS AN OPEN OR CLOSE ONE
    ALSO RETRIEVE CONTENT FOR FURTHER CHECKING
    
    INPUT : TAG -> String
    
    OUTPUT : 1. OPEN, CLOSE OR COMMENT
             2. CONTENT
    
    """
    match list(tag):
        case ["<", "/", *content, ">"]:
            return ["CLOSE", "".join(content)]
        case ["<", "!", "-", *content, "-", ">"]:
            return ["COMMENT", "".join(content)]
        case ["<", *content, ">"]:
            return ["OPEN", "".join(content)]
        case _:
            raise Exception(f"Invalid Tag: {tag}")