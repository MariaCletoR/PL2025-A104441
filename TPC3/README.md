# TPC 3 - Conversor de Markdown para HTML 

**Autor:** [Maria Cleto Rocha]  
**Número:** [A104441]

![Fotografia do Estudante](mariafoto.jpeg)
---

## Introdução e Descrição
Neste 3º TPC da Unidade Curricular de Processamento de Linguagens, foi desenvolvido um conversor de Markdown para HTML. O objetivo é transformar, de forma automática, elementos básicos da sintaxe Markdown na sua correspondente representação em HTML. Entre os elementos convertidos, destacam-se:

- **Cabeçalhos:** Linhas iniciadas com `#`, `##` ou `###` são convertidas para `<h1>`, `<h2>` e `<h3>`, respetivamente.
- **Negrito:** Pedaços de texto entre `**` são convertidos para `<b>`.
- **Itálico:** Pedaços de texto entre `*` são convertidos para `<i>`.
- **Listas Numeradas:** Linhas iniciadas com números seguidos de um ponto (ex: `1.`, `2.`) são agrupadas dentro de um `<ol>` com cada item em `<li>`.
- **Links:** Sintaxe `[texto](URL)` é transformada em `<a href="URL">texto</a>`.
- **Imagens:** Sintaxe `![texto alternativo](URL)` é convertida para `<img src="URL" alt="texto alternativo"/>`.

---

## Regras de Funcionamento
1. **Cabeçalhos:** Linhas iniciadas por 1 a 3 símbolos `#` são convertidas para as tags do cabeçalho correspondentes.
2. **Negrito e Itálico:** Pedaços delimitados por `**` ou `*` são convertidos, respetivamente, para `<b>` e `<i>`.
3. **Listas Numeradas:** O programa identifica linhas numeradas e as encapsula entre `<ol>` e `<li>`.
4. **Links e Imagens:** Utiliza expressões regulares para identificar os padrões Markdown e substituir pelas tags HTML apropriadas.

---

### **Arquitetura do Programa**
- **Divisão de Funcionalidades:**
  - **`process_inline(text)`**: Processa elementos inline como imagens, links, negrito e itálico utilizando expressões regulares.
  - **`markdown_to_html(markdown_text)`**: Realiza a conversão do texto completo, processando cabeçalhos, listas numeradas e outros elementos.

- **Uso de Expressões Regulares:**  
  O módulo `re` é utilizado para identificar e substituir os padrões Markdown pelos seus equivalentes em HTML, garantindo uma conversão simples e intuitiva.

### **Componentes Principais**
- **Função `process_inline(text)`:**  
  Converte:
  - Imagens (`![texto](url)`) para `<img src="url" alt="texto"/>`.
  - Links (`[texto](url)`) para `<a href="url">texto</a>`.
  - Negrito (`**texto**`) para `<b>texto</b>`.
  - Itálico (`*texto*`) para `<i>texto</i>`.

- **Função `markdown_to_html(markdown_text)`:**  
  - Separa o texto em linhas e processa cabeçalhos e itens de lista.
  - Aplica as conversões necessárias para cada linha, organizando o HTML final de forma estruturada.
  
- **Exemplo de Execução:**  
  O bloco `if __name__ == "__main__":` no código permite testar o conversor com um exemplo de Markdown, demonstrando a saída HTML que foi gerada.

---

## **Código Fonte**
É possível aceder ao código completo neste repositório:  
[🔗 conversor.py](https://github.com/MariaCletoR/PL2025-A104441/blob/main/TPC3/conversor.py)
---

## **Execução**
Para executar o programa, utilize o seguinte comando no terminal:

```sh
python3 conversor_md_html.py
