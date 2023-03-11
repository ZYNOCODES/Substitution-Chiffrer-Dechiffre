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

