# TPC 6 - Analisador Sintático Recursivo Descendente para Expressões Aritméticas

**Autor:** [Maria Cleto Rocha]  
**Número:** [A104441]

![Fotografia do Estudante](mariafoto.jpeg)

---

## Introdução e Descrição

Este 6º TPC foi desenvolvido no âmbito da Unidade Curricular de **Processamento de Linguagens**.  
O objetivo é construir um **parser recursivo descendente LL(1)** que reconheça e **avalie expressões aritméticas** com parêntesis, inteiros e operadores binários (`+`, `-`, `*`, `/`).

O programa foi dividido em dois módulos principais:
- Um **analisador léxico** (`calc_lex.py`) que transforma a expressão numa lista de tokens;
- Um **analisador sintático** (`calc_parser.py`) que segue uma gramática LL(1) e calcula o valor da expressão.

---

## Regras de Funcionamento

### Tokens Reconhecidos (`calc_lex.py`)
- `NUM`: números inteiros (ex: 3, 10, 42)
- `SOMA`: operador de adição (`+`)
- `SUB`: operador de subtração (`-`)
- `MUL`: operador de multiplicação (`*`)
- `DIV`: operador de divisão (`/`)
- `LPAR` / `RPAR`: parêntesis esquerdo e direito (`(` e `)`)
- `EOF`: fim da expressão

### Gramática LL(1) utilizada (`calc_parser.py`)

```
Expr     → Term Expr’
Expr’    → + Term Expr’ | - Term Expr’ | ε
Term     → Factor Term’
Term’    → * Factor Term’ | / Factor Term’ | ε
Factor   → (Expr) | NUM
```

### Funcionamento Geral
1. O `Lexer` percorre a string da expressão e devolve uma lista de tokens.
2. O `Parser` aplica recursivamente as regras da gramática para processar os tokens e calcular o valor.
3. O resultado final da expressão é impresso no terminal.

---

## Exemplo de Execução

```bash
$ python3 main.py

Expressão (ENTER para sair): 2+3
Resultado: 5

Expressão (ENTER para sair): 67-(2+3*4)
Resultado: 53

Expressão (ENTER para sair): (9-2)*(13-4)
Resultado: 63
```

---

## Arquitetura do Programa

- **`calc_lex.py`**:
  - Define os padrões dos tokens com expressões regulares.
  - Gera uma lista de tokens a partir da expressão inserida.

- **`calc_parser.py`**:
  - Implementa um analisador LL(1) recursivo descendente.
  - Avalia a expressão aritmética ao mesmo tempo que faz a análise sintática.

- **`main.py`**:
  - Interface interativa com o utilizador.
  - Lê input, passa pelo lexer e parser, e mostra o resultado.

---

## Código Fonte

- [`calc_lex.py`](./calc_lex.py) — Analisador Léxico  
- [`calc_parser.py`](./calc_parser.py) — Parser Recursivo Descendente  
- [`main.py`](./main.py) — Interface de teste

---

## Execução

Para executar o TPC6, é necessário ter o Python 3 instalado e posteriormente escrever:

```bash
python3 main.py
```

Insere expressões como `2+3` ou `(5+4)*2` e o resultado será calculado automaticamente.

---
