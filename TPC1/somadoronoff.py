def somador(texto):
    m = 0
    isON = True
    soma = 0
    while m < len(texto):
        on = texto[m] + texto[m+1] if m < len (texto) - 2 else ""
        off = texto[m] + texto[m+1] + texto[m+2] if m < len(texto) - 3 else ""

        if on.lower() == "on":
            isON = True
            m = m + 1

        elif off.lower() == "off":
            isON = False
            m = m + 1

        elif texto[m] == '=':
            print ("Valor com o '=' encontrado : " ,soma)
            m = m + 1

        elif '0' < texto[m] < '9' and isON:
            num = int (texto[m])
            m = m + 1

            while m < len(texto) and '0' < texto[m] < '9':
                num = num * 10 + int(texto[m])
                m = m + 1
            soma = soma + num     

        else: 
            m = m + 1

    return soma

def main():
    texto = str (input("Escreva aqui o texto a analisar: "))
    print("Valor final: " ,somador(texto))
        
if __name__ == "__main__": 
    main()


