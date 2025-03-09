# TPC 2 - Análise de um Dataset de Obras Musicais 

**Autor:** [Maria Cleto Rocha]

**Número:** [A104441]

![Fotografia do Estudante](mariafoto.jpeg)

---

## Introdução e Descrição
Este segundo ficheiro foi criado e implementado no âmbito da Unidade Curricular de **Processamento de Linguagens**, tendo como objetivo principal a análise de um dataset de obras musicais (armazenado num ficheiro CSV).  
A aplicação lê os dados do ficheiro CSV sem recorrer ao módulo `csv` do Python (lendo-o linha a linha), e processa essas informações para gerar:
1. Uma **lista ordenada alfabeticamente** dos compositores;
2. Uma **distribuição** do número de obras por período (e.g. Barroco, Clássico, Romântico, etc.);
3. Um **dicionário** em que, para cada período, é associada uma **lista alfabética** dos títulos das obras desse período.

---

## Regras de Funcionamento
1. **Leitura do ficheiro**:  
   - O programa abre o ficheiro CSV (`obras.csv`) e processa o seu conteúdo linha a linha, separando os campos por `";"`.
2. **Tratamento de possíveis cabeçalhos**:  
   - Caso a primeira linha contenha algo como `"nome"`, `"titulo"`, etc., a mesma é ignorada.
3. **Armazenamento de dados**:  
   - São criadas estruturas para guardar compositores (sem repetições), a contagem de obras por período e, adicionalmente, as listas de títulos de obras por período.
4. **Ordenação**:  
   - No final, os compositores e os títulos das obras de cada período são ordenados alfabeticamente.
5. **Apresentação dos resultados**:  
   - O programa imprime então uma lista de compositores, a distribuição de obras por período e as listas de títulos de cada período.

---

### Arquitetura do Programa
- **Função `processar_arquivo(nome_arquivo)`**:  
  - **Abre e lê** o ficheiro `nome_arquivo`;
  - **Separa** cada linha em campos (por `";"`);
  - **Ignora** a primeira linha se for um cabeçalho;
  - **Atualiza**:
    - A lista de compositores (sem duplicações);
    - O dicionário com a contagem de obras por período;
    - O dicionário que mapeia cada período para a sua lista de títulos;
  - **Ordena** compositores e títulos, e retorna as três estruturas de dados finais.

- **Compenentes principais (`if __name__ == '__main__':`)**:  
  - Define o nome do ficheiro CSV (`"obras.csv"` por omissão);
  - Chama a função `processar_arquivo`;
  - Imprime a **lista ordenada** de compositores, a **distribuição** das obras por período e as **listas** de títulos por período.

---

## Código Fonte
O código completo pode ser encontrado no seguinte repositório (exemplo de link):
[🔗 obras_musicais.py](https://github.com/MariaCletoR/PL2025-A104441/blob/main/TPC2/obras_musicais.py)

---

## Execução
Para correr o programa, basta utilizar o comando abaixo (assumindo que tem o Python 3 instalado) e have a certeza de que o ficheiro CSV (`obras.csv`) se encontra na mesma pasta:

```sh
python3 obras_musicais.py
