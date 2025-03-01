import re

def process_inline(text):
    
    text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', text)
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    return text

def markdown_to_html(markdown_text):

    lines = markdown_text.split('\n')
    html_lines = []
    in_list = False  

    for line in lines:
        line = line.strip()
        if not line:
            if in_list:
                html_lines.append('</ol>')
                in_list = False
            html_lines.append('')
            continue

        header_match = re.match(r'^(#{1,3})\s+(.*)$', line)
        if header_match:
            if in_list:
                html_lines.append('</ol>')
                in_list = False
            header_level = len(header_match.group(1))
            header_text = process_inline(header_match.group(2))
            html_lines.append(f'<h{header_level}>{header_text}</h{header_level}>')
            continue

        list_match = re.match(r'^\d+\.\s+(.*)$', line)
        if list_match:
            if not in_list:
                html_lines.append('<ol>')
                in_list = True
            list_item_text = process_inline(list_match.group(1))
            html_lines.append(f'<li>{list_item_text}</li>')
            continue
        else:
            if in_list:
                html_lines.append('</ol>')
                in_list = False

        processed_line = process_inline(line)
        html_lines.append(processed_line)

    if in_list:
        html_lines.append('</ol>')

    return "\n".join(html_lines)

if __name__ == "__main__":
    markdown_text = """# Exemplo de Cabeçalho 1
## Exemplo de Cabeçalho 2
### Exemplo de Cabeçalho 3

Este é um **exemplo** de texto com *itálico*.

1. Primeiro item
2. Segundo item
3. Terceiro item

Como pode ser consultado em [página da UC](http://www.uc.pt)

Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
"""
    html_text = markdown_to_html(markdown_text)
    print(html_text)
