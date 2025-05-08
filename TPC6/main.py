from calc_lex import CalcLexer
from calc_parser import CalcParser

if __name__ == "__main__":
    while True:
        try:
            expr = input("\nExpressão ('ENTER' para sair): ")
            if not expr:
                break
            lexer = CalcLexer(expr)
            parser = CalcParser(lexer.tokens)
            resultado = parser.parse()
            print("Resultado:", resultado)
        except Exception as e:
            print("Erro:", e)
