import json

FICHEIRO_STOCK = "stock.json"

def carregar_stock():
    try:
        with open(FICHEIRO_STOCK, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_stock(stock):
    with open(FICHEIRO_STOCK, "w") as f:
        json.dump(stock, f, indent=4)

def listar_stock(stock):
    print("cod | nome         | quantidade | preço")
    print("---------------------------------------")
    for item in stock:
        print(f"{item['cod']}  {item['nome']}  {item['quant']}  {item['preco']}")

def converter_para_centimos(valor):
    if valor.endswith("e"):
        return int(valor[:-1]) * 100
    elif valor.endswith("c"):
        return int(valor[:-1])
    else:
        return 0

def mostrar_saldo(saldo):
    euros = saldo // 100
    centimos = saldo % 100
    print(f"maq: Saldo = {euros}e{centimos}c")

def dar_troco(saldo):
    moedas = [200, 100, 50, 20, 10, 5, 2, 1]
    troco = []
    for moeda in moedas:
        while saldo >= moeda:
            saldo -= moeda
            troco.append(moeda)
    if troco:
        print("maq: Pode retirar o troco:", end=" ")
        contagem = {}
        for m in troco:
            contagem[m] = contagem.get(m, 0) + 1
        troco_str = ", ".join(f"{v}x {m if m >= 100 else m}c" if m < 100 else f"{v}x {m//100}e" for m, v in contagem.items())
        print(troco_str + ".")
    else:
        print("maq: Não há troco a devolver.")

def adicionar_produto(stock):
    cod = input(">> Código do produto: ").strip()
    nome = input(">> Nome do produto: ").strip()
    quant = int(input(">> Quantidade: "))
    preco = float(input(">> Preço (ex: 0.7): "))

    for item in stock:
        if item["cod"] == cod:
            item["quant"] += quant
            print("maq: Produto existente, quantidade atualizada.")
            return
    stock.append({"cod": cod, "nome": nome, "quant": quant, "preco": preco})
    print("maq: Produto adicionado ao stock.")

stock = carregar_stock()
saldo = 0

print("maq: 2024-03-08, Stock carregado, Estado atualizado.")
print("maq: Bom dia. Estou disponível para atender o seu pedido.")

while True:
    comando = input(">> ").strip().upper()

    if comando == "LISTAR":
        listar_stock(stock)

    elif comando.startswith("MOEDA"):
        partes = comando[6:].split(",")
        for p in partes:
            p = p.strip().strip(".")
            saldo += converter_para_centimos(p)
        mostrar_saldo(saldo)

    elif comando.startswith("SELECIONAR"):
        cod = comando[10:].strip()
        produto = next((item for item in stock if item["cod"] == cod), None)
        if produto:
            preco = int(produto["preco"] * 100)
            if produto["quant"] == 0:
                print("maq: Produto esgotado.")
            elif saldo >= preco:
                produto["quant"] -= 1
                saldo -= preco
                print(f'maq: Pode retirar o produto dispensado "{produto["nome"]}"')
                mostrar_saldo(saldo)
            else:
                print("maq: Saldo insufuciente para satisfazer o seu pedido")
                mostrar_saldo(saldo)
                print(f"maq: Pedido = {preco//100}e{preco%100}c")
        else:
            print("maq: Produto inexistente.")

    elif comando == "ADICIONAR":
        adicionar_produto(stock)

    elif comando == "SAIR":
        dar_troco(saldo)
        print("maq: Até à próxima")
        guardar_stock(stock)
        break

    else:
        print("maq: Comando não reconhecido. Tente novamente.")
