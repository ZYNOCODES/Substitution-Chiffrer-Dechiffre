
#Chiffrement par Substitution

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Pi = "GVCSALUTDPKZRNBIFXYEMWJQHO"
text = "LA CRYPTANALYSE EST LA SCIENCE QUI CONSISTE A TENTER DE DECHIFFRER UN MESSAGE AYANT ETE CHIFFRE SANS POSSEDER " \
       "LA CLE DE CHIFFREMENT. LE PROCESSUS PAR LEQUEL ON TENTE DE COMPRENDRE UN MESSAGE EN PARTICULIER EST APPELE UNE ATTAQUE."

print("La substitution Pi :")
print(Pi)
print("Input text :")
print(text)
print("\n")

chiffrer = ""

for letter in text:
    if letter.upper() in alphabet:
        chiffrer += Pi[alphabet.find(letter.upper())]
    else:
        chiffrer += letter

print("Text chiffrer :")
print(chiffrer)

dechiffrer = ""

for letter in chiffrer:
    if letter.upper() in alphabet:
        dechiffrer += alphabet[Pi.find(letter.upper())]
    else:
        dechiffrer += letter

print("Text dechiffrer :")
print(dechiffrer)

#Chiffrement par decalage

alphabet = list('abcdefghijklmnopqrstuvwxyz')
alphabet2 = list('abcdefghijklmnopqrstuvwxyz')

phrase = input("Ecrivez une phrase:")
print(phrase)
decalage = input("Valeur du decalage?")
def ceasar():
    x,y,z = 0,1,1
    while x<26:
        y = x+int(decalage)
        z = y - 26
        if(y<26):
            alphabet[x] = alphabet[y]
        else:
            alphabet[x] = alphabet2[z]
        x = x + 1
    print(alphabet)
ceasar()
newPhraseList = list(phrase)
nbLettres = len(phrase)
newPhrase = ""
n = 0
while n<nbLettres:
    newPhrase = newPhrase+""+newPhraseList[n]
    phraseFinal = newPhrase.replace(newPhraseList[n],alphabet[n])
    n = n + 1
    print (phraseFinal)