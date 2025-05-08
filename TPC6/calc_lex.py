import re

PADROES_TOKENS = [
    (r'\d+', 'NUM'),    
    (r'\+', 'SOMA'), 
    (r'-', 'SUB'),    
    (r'\*', 'MUL'),      
    (r'/', 'DIV'),     
    (r'\(', 'LPAR'),     
    (r'\)', 'RPAR')     
]

class CalcLexer:
    def __init__(self, input_str):
        self.input = input_str
        self.tokens = []
        self.tokenize()

    def tokenize(self):
        s = self.input.strip()
        while s:
            match = None
            for padrao, token_type in PADROES_TOKENS:
                regex = re.compile(padrao)
                match = regex.match(s)
                if match:
                    value = match.group(0)
                    if token_type == 'NUM':
                        value = int(value)
                    self.tokens.append((token_type, value))
                    s = s[len(match.group(0)):].lstrip()
                    break
            if not match:
                raise Exception(f"Token inválido: {s}")
        self.tokens.append(('EOF', None))