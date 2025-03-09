# TPC 4 - Analisador Léxico de Código

**Autor:** [Maria Cleto Rocha]  
**Número:** [A104441]

![Fotografia do Estudante](mariafoto.jpeg)

---

## Introdução e Descrição
Este ficheiro foi desenvolvido no âmbito da Unidade Curricular de **Processamento de Linguagens**. O objetivo do mesmo é implementar um analisador léxico que processa códigos, extraindo e classificando os diferentes tokens presentes no código.  
A aplicação utiliza expressões regulares para identificar e diferenciar elementos como comentários, strings, números, variáveis, palavras-chave e identificadores, permitindo assim a análise e interpretação do código fornecido.

---

## Regras de Funcionamento
1. **Definição dos Tokens**:  
   - São definidas diversas especificações de tokens, cada uma associada a uma expressão regular.  
   - Exemplos:  
     - `COMMENT` para comentários (iniciados por `#`);  
     - `STRING` para literais de string delimitados por aspas;  
     - `NUMBER` para sequências numéricas;  
     - `VARIABLE` para variáveis que iniciam com `?`;  
     - `KEYWORD` para palavras reservadas como `select`, `SELECT`,`WHERE`, `where` e `LIMIT`;  
     - `IDENTIFIER` para nomes que seguem um padrão de identificador.  

2. **Processo de Tokenização**:  
   - A função `tokenize(code)` compila todas as expressões regulares num único padrão e percorre o código utilizando `re.finditer`.  
   - Para cada correspondência encontrada, o token é classificado de acordo com o seu tipo.  
   - Tokens de espaços em branco e comentários são ignorados.  
   - Caso seja detectado um caractere que não se enquadre em nenhum token (definido como `MISMATCH`), é levantada uma exceção.

3. **Exemplo de Execução**:  
   - Ao executar o script, um exemplo de código (contendo uma consulta similar a SPARQL) é analisado e os tokens extraídos são impressos no terminal.

---

## Arquitetura do Programa
- **Função `tokenize(code)`**:  
  - **Construção do Regex**:  
    - Cria uma expressão regular composta, combinando todas as especificações de tokens.
  - **Iteração e Classificação**:  
    - Utiliza `re.finditer` para identificar e classificar cada token presente no código.  
    - Converte tokens numéricos para inteiros e ignora espaços e comentários.
  - **Gestão de Erros**:  
    - Se um caractere não corresponder a nenhum padrão esperado, o programa gera um erro com uma mensagem de "Caractere inesperado".

- **Bloco Principal (`if __name__ == '__main__':`)**:  
  - Define um exemplo de código que simula uma consulta com uma sintaxe similar a SPARQL.  
  - Chama a função `tokenize` para processar o exemplo e imprime os tokens resultantes.

---

## Código Fonte
O código completo pode ser encontrado no seguinte repositório (exemplo de link):  
[🔗 analisadorlex.py](https://github.com/MariaCletoR/PL2025-A104441/blob/main/TPC4/analisadorlex.py)

---

## Execução
Para executar o analisador léxico, certifique-se de ter o Python 3 instalado e utilize o comando abaixo (garantindo que o script se encontra na mesma pasta):

```sh
python3 analisadorlex.py


