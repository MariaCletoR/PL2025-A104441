def processar_arquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()
    linhas = conteudo.splitlines()

    if linhas and "nome" in linhas[0].lower():
        linhas = linhas[1:]
    
    compositores_set = set()
    obras_por_periodo = {}       
    titulos_por_periodo = {}     
    
    for linha in linhas:
        campos = linha.split(";")
        if len(campos) < 5:  
            continue
        
        titulo = campos[0].strip()
        periodo = campos[3].strip()
        compositor = campos[4].strip()
        
        compositores_set.add(compositor)
        
        obras_por_periodo[periodo] = obras_por_periodo.get(periodo, 0) + 1
        
        if periodo not in titulos_por_periodo:
            titulos_por_periodo[periodo] = []
        titulos_por_periodo[periodo].append(titulo)
    
    lista_compositores = sorted(compositores_set)
    
    for periodo in titulos_por_periodo:
        titulos_por_periodo[periodo].sort()
    
    return lista_compositores, obras_por_periodo, titulos_por_periodo


if __name__ == '__main__':
    arquivo = "obras.csv"  
    compositores, distribuicao, titulos_periodo = processar_arquivo(arquivo)
    
    print("Lista ordenada dos compositores:")
    for c in compositores:
        print(c)
    
    print("\nDistribuição das obras por período:")
    for periodo, quantidade in distribuicao.items():
        print(f"{periodo}: {quantidade}")
    
    print("\nTítulos das obras por período:")
    for periodo, titulos in titulos_periodo.items():
        print(f"{periodo}:")
        for titulo in titulos:
            print("  -", titulo)
