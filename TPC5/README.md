# TPC 5 - Máquina Vending

**Autor:** [Maria Cleto Rocha]  
**Número:** [A104441]

![Fotografia do Estudante](mariafoto.jpeg)

---

## Introdução e Descrição
Este ficheiro foi desenvolvido no âmbito da Unidade Curricular de **Processamento de Linguagens**. O objetivo é simular o funcionamento de uma máquina de vending, permitindo listar produtos, inserir moedas, selecionar produtos e receber troco.  
A máquina mantém o estado do stock entre execuções, persistindo os dados num ficheiro `stock.json`. O código foca-se na simplicidade, eficiência e boa interação com o utilizador.

---

## Regras de Funcionamento

1. **Gestão do Stock**:  
   - O stock é carregado automaticamente a partir de um ficheiro `stock.json` ao iniciar o programa.  
   - O stock é atualizado e guardado novamente ao sair do programa.  
   - Cada produto tem:  
     - `cod` – código do produto (ex: A23);  
     - `nome` – nome do produto (ex: água 0.5L);  
     - `quant` – quantidade disponível;  
     - `preco` – preço em euros.

2. **Comandos Disponíveis**:
   - `LISTAR`: Lista todos os produtos disponíveis com o código, nome, quantidade e preço.  
   - `MOEDA`: Permite inserir moedas no formato `1e, 50c, 20c`, atualizando o saldo.  
   - `SELECIONAR <código>`: Tenta comprar o produto com o código dado. Verifica saldo e stock.  
   - `ADICIONAR`: Permite adicionar novos produtos ou repor stock dos existentes.  
   - `SAIR`: Devolve o troco ao utilizador e termina a aplicação.

3. **Gestão de Saldo e Troco**:  
   - O saldo é acumulado com as moedas inseridas.  
   - Ao comprar produtos, o saldo é descontado.  
   - Ao sair, é calculado e devolvido o troco em moedas (ex: 1x 50c, 1x 20c).

---

## Exemplo de Interação
```text
maq: 2024-03-08, Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
>> LISTAR
maq:
cod | nome         | quantidade | preço
----------------------------------------
A23 água 0.5L 8 0.7
...
>> MOEDA 1e, 20c.
maq: Saldo = 1e20c
>> SELECIONAR A23
maq: Pode retirar o produto dispensado "água 0.5L"
maq: Saldo = 50c
>> SAIR
maq: Pode retirar o troco: 1x 50c.
maq: Até à próxima
