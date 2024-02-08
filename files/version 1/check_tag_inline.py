def check_line_for_tags(line: str) -> list[str]:
    open_ = False
    parsed = []
    content = ""
    
    for i in line:
        
        if i == "<" and open_:
            raise Exception(f"Tag was never closed: {line}")
            
        if i == ">" and not open_:
            raise Exception(f"Tag was never opened: {line}")
        
        if i == "<":
            open_ = True
            
        if open_:
            content += i
            
        if i == ">" and content == "<>":
            raise Exception("Tag is empty")
            
        if i == ">":
            open_ = False
            parsed.append(content)
            content = ""
            
    if open_:
            raise Exception(f"Tag was never closed: {line}")
            
    return parsed