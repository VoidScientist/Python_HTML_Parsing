data = []

# so this all kinda works, but the program is disgusting, rework needed.

def parse_line(line, num=1):
    try:
        return [check_tag_content(tag) for tag in check_line_for_tags(line)]
    except Exception as e:
        print(f"Exception occurred at line {num}: {e}")
        return []
    

with open("htmlparsing.txt", "r") as f:
    self_closing = ["meta", "link", "!DOCTYPE", "img"]
    stack = []
    line = f.readline()
    num = 1
    
    while line:
        r = parse_line(line.strip(), num)
        
        for i in r:
            
            nat = i[0]
            tag = i[1].split(" ")[0]
            
            if tag in self_closing:
                continue
            
            elif nat == "OPEN":
                stack.append(tag)
                    
            elif tag == stack[-1]:
                del stack[-1]
                
            elif nat == "CLOSE" and tag != stack[-1]:
                print(f"Unmatched closing tag at line {num} || awaiting </{stack[-1]}> but </{tag}> found")
                
            elif nat != "COMMENT":
                print(f"{stack[-1]} never closed at line {num}")
            
        line = f.readline()
        num+=1 