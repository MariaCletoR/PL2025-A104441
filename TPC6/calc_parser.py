class CalcParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def eat(self, token_type):
        if self.current_token[0] == token_type:
            self.pos += 1
            self.current_token = self.tokens[self.pos]
        else:
            raise Exception(f"Erro de sintaxe: esperava {token_type}, recebeu {self.current_token[0]}")

    def parse(self):
        result = self.expr()
        if self.current_token[0] != 'EOF':
            raise Exception("Erro: input não completamente consumido")
        return result

    def expr(self):
        result = self.term()
        return self.expr_linha(result)

    def expr_linha(self, acc):
        if self.current_token[0] == 'SOMA':
            self.eat('SOMA')
            return self.expr_linha(acc + self.term())
        elif self.current_token[0] == 'SUB':
            self.eat('SUB')
            return self.expr_linha(acc - self.term())
        else:
            return acc

    def term(self):
        result = self.factor()
        return self.term_linha(result)

    def term_linha(self, acc):
        if self.current_token[0] == 'MUL':
            self.eat('MUL')
            return self.term_linha(acc * self.factor())
        elif self.current_token[0] == 'DIV':
            self.eat('DIV')
            return self.term_linha(acc / self.factor())
        else:
            return acc

    def factor(self):
        if self.current_token[0] == 'NUM':
            value = self.current_token[1]
            self.eat('NUM')
            return value
        elif self.current_token[0] == 'LPAR':
            self.eat('LPAR')
            result = self.expr()
            self.eat('RPAR')
            return result
        else:
            raise Exception("Erro: esperava número ou '('")

class CalcParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def eat(self, token_type):
        if self.current_token[0] == token_type:
            self.pos += 1
            self.current_token = self.tokens[self.pos]
        else:
            raise Exception(f"Erro de sintaxe: esperava {token_type}, recebeu {self.current_token[0]}")

    def parse(self):
        result = self.expr()
        if self.current_token[0] != 'EOF':
            raise Exception("Erro: input não completamente consumido")
        return result

    def expr(self):
        result = self.term()
        return self.expr_linha(result)

    def expr_linha(self, acc):
        if self.current_token[0] == 'SOMA':
            self.eat('SOMA')
            return self.expr_linha(acc + self.term())
        elif self.current_token[0] == 'SUB':
            self.eat('SUB')
            return self.expr_linha(acc - self.term())
        else:
            return acc

    def term(self):
        result = self.factor()
        return self.term_linha(result)

    def term_linha(self, acc):
        if self.current_token[0] == 'MUL':
            self.eat('MUL')
            return self.term_linha(acc * self.factor())
        elif self.current_token[0] == 'DIV':
            self.eat('DIV')
            return self.term_linha(acc / self.factor())
        else:
            return acc

    def factor(self):
        if self.current_token[0] == 'NUM':
            value = self.current_token[1]
            self.eat('NUM')
            return value
        elif self.current_token[0] == 'LPAR':
            self.eat('LPAR')
            result = self.expr()
            self.eat('RPAR')
            return result
        else:
            raise Exception("Erro: esperava número ou '('")

