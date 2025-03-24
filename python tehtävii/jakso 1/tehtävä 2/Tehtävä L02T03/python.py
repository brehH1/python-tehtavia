nimi = input("Anna nimesi: ")

i = nimi.find(' ')

etunimi = nimi[:i]
sukunimi = nimi[i+1:]

print("Etunimesi:", etunimi)
print("Sukunimesi:", sukunimi)
