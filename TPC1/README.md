# TPC 1:: Somador On/Off em Python

**Autor:** Maria Cleto Rocha 
**Número:** A104441

![Fotografia do Estudante em questao](mariafoto.jpeg)
---

## Introdução e descrição
Este primeiro ficheiro foi criado e implementado no âmbito da Unidade Curricular de Processamento de Linguagens, onde o objetivo principal é introduzir um somador on/off criado num programa em Python.
O mesmo implementa, como ja foi referido, um somador que opera de acordo com um interruptor **On/Off**. O programa processa e analisa um texto e soma todas as sequências de números encontradas no mesmo - **Apenas quando o estado do interruptor está ligado**.

---

## Regras de Funcionamento
1. O programa percorre o texto e soma todas as sequências de números encontradas.
2. Sempre que encontrar um `"Off"` (maiúsculas ou minúsculas), o somador **desliga**.
3. Sempre que encontrar um `"On"` (maiúsculas ou minúsculas), o somador **liga**.
4. Ao encontrar um `"="`, o resultado da soma é **exibido na saída**.

---

### **Arquitetura do Programa**
- O programa percorre um **texto de entrada**, identificando números e comandos (`on`, `off`, `=`);
- O mesmo usa um **booleano (`isON`)** de maneira a controlar quando os números estão, de facto, a ser somados;
- Quando o comando `"="` é encontrado, o resultado da soma é impresso.

### **Componentes Principais**
- **Função `somador(texto)`**:  
  - Percorre o texto e soma os números encontrados quando o somador está ligado (`ON`);
  - Altera o estado ao encontrar `"on"` ou `"off"`;
  - Exibe o resultado ao encontrar `"="`.

- **Função `main()`**:  
  - Solicita ao utilizador um **input de texto**;
  - Chama a função `somador(texto)` e imprime o resultado final.

##  **Código fonte**
É possível aceder ao código completo no seguinte repositório:  
[🔗 somadoronoff.py](https://github.com/MariaCletoR/PL2025-A104441/blob/main/TPC1/somadoronoff.py)

## **Execução**
Para correr o programa, pode usar o seguinte comando no terminal e posteriormente fornecer um input desejado.

```sh
python3 somador.py