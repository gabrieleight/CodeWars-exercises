#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

def inverte_string(frase):
    lista = frase.split()
    frase_invertida = ''
    for i in lista:
        if i.isalpha():
            frase_invertida += i[1:] + i[0] + 'ay' + ' '
        else:
            frase_invertida += i
        
        #se eu quiser inverter a palavra inteira:
        #frase_invertida += i[::-1] + 'ay' + ' '
    return frase_invertida.strip()
    
if __name__ == "__main__":
    palavra = 'Pig latin is cool'
    print(inverte_string(palavra))