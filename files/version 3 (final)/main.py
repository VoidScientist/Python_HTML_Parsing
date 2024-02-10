from tag_parser import parse
from structural_checker import check_html_structure

with open("htmlparsing.txt", "r") as f:
    data, err_tag = parse(f)
    err, hints = check_html_structure(data)

    print("HINTS:")
    print(*hints, sep="\n", end="\n\n")
    print("TAG RELATED ERRORS:")
    print(*err_tag, sep="\n", end="\n\n")
    print("STRUCTURAL ERRORS:")
    print(*err, sep="\n", end="\n\n")
    
    input("Press Enter To Continue...")

# welp, that was fun.