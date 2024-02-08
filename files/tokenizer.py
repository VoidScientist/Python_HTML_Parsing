token_list = ("Greater", "Inferior", "Identifier", "Equal", "Quote", "Slash", "Dash", "Excla")

class Token:
    def __init__(self, nat, lexeme):
        self.nat = nat
        self.lexeme = lexeme
    def __str__(self):
        return f"{self.nat} {self.lexeme}"

def tokenizer(f):
    tokens = []
    
    # CONSUME FIRST CHARACTER
    a = f.read(1)
    
    # WHILE CHARACTER IN FILE
    while a:
        
        if a == "<":
            tokens.append(Token("Inferior", "<"))
            
        if a == "!":
            tokens.append(Token("Excla", "!"))
            
        if a == "-":
            tokens.append(Token("Dash", "-"))
            
        if a == ">":
            tokens.append(Token("Greater", ">"))
            
        if a == "=":
            tokens.append(Token("Equal", "="))
            
        if a == "\"":
            tokens.append(Token("Quote", "\""))
            
        if a == "/":
            tokens.append(Token("Slash", "/"))
            
        if a.isalnum():
            
            lex = a
            a = f.read(1)
            
            while a.isalnum():
                lex += a
                a = f.read(1)
                
            tokens.append(Token("Identifier", lex))
            
            continue
        
        a = f.read(1)
    
    return tokens