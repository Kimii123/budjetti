# Kysytään kulutuskohteet

vuokra = float(input("Vuokran määrä: "))
vakuutukset = float(input("Vakuutusten määrä: "))
kouluruokailu = float(input("Kouluruokailun määrä: "))
sahko = float(input("Sähkön määrä: "))
liikkuminen = float(input("Liikkumisen määrä: "))

# Lasketaan yhteen

yhteensa = vuokra + vakuutukset + kouluruokailu + sahko + liikkuminen 

print(f"Ynteens {yhteensa} euroa kuukaudessa.")