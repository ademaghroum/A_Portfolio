somme = 0
compteur = 0

while somme <= 40:
    valeur = int(input("Valeur ? "))
    somme += valeur
    compteur += 1

print(f"La somme des {compteur} entiers vaut {somme}")