import re

token_specification = [
    ('COMMENT',    r'#.*'),                        
    ('STRING',     r'"[^"]*"'),                     
    ('NUMBER',     r'\d+'),                         
    ('VARIABLE',   r'\?[A-Za-z_]\w*'),               
    ('KEYWORD',    r'\b(?:select|where|SELECT|WHERE|LIMIT)\b'),   
    ('LBRACE',     r'\{'),                         
    ('RBRACE',     r'\}'),                   
    ('DOT',        r'\.'),                   
    ('AT',         r'@'),                          
    ('IDENTIFIER', r'[A-Za-z_][\w:.-]*'),            
    ('SKIP',       r'[ \t\n]+'),                 
    ('MISMATCH',   r'.'),                       
]

def tokenize(code):
  
    tokens = []
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup   
        value = mo.group()     
        if kind == 'NUMBER':
            value = int(value)  
            tokens.append((kind, value))
        elif kind == 'STRING':
            tokens.append((kind, value))
        elif kind == 'SKIP' or kind == 'COMMENT':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Caractere inesperado: {value!r}')
        else:
            tokens.append((kind, value))
    return tokens

if __name__ == '__main__':
    code = '''# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
    ?s a dbo:MusicalArtist. 
    ?s foaf:name "Chuck Berry"@en . 
    ?w dbo:artist ?s. 
    ?w foaf:name ?nome. 
    ?w dbo:abstract ?desc 
} LIMIT 1000
'''
    tokens = tokenize(code)
    for token in tokens:
        print(token)
