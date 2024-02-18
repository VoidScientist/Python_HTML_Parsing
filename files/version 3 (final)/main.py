from tag_parser import parse
from structural_checker import check_html_structure

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
# about tag names, so there's an hyper-parameter to allow it in "tag_parser.py"
#
# Disclaimer 3: nested tags like <a> aren't allowed, but for the sake of simplicity (mostly
# because i couldn't get it to work) it was not implemented. TODO make it maybe.
#
# But it passes the google page with lots of obfuscated JS so i'm happy at least.
#
# Data Structures used : stack - queue
# Modus Operandi : Finite State Machine
# ----------------------------------------------------

with open("htmlparsing.txt", "r", encoding="utf-8") as f:
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