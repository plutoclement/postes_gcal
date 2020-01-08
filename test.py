import json

notes = { 'a' : [(1, 2), (2, 1)], 'b' : [(2, 2), (1, 1)] }
matin  =         {"nom" : "[M12] Matin",
"heure_debut": "07:30",
"heure_fin": "15:00"}
soir  =         {"nom" : "[S12] Soir",
"heure_debut": "12:00",
"heure_fin": "19:30"}
nuit  =         {"nom" : "[N15] Nuit",
"heure_debut": "19:30",
"heure_fin": "07:30"}

postesw = {"matin" : matin,"soir" : soir,"nuit" : nuit,"repos" : 0}
        
# Enregistrer le dictionnaire dans un fichier :
with open('postes.txt', 'w') as file:
    json.dump(postesw, file)

## Charger le dictionnaire depuis un fichier :
with open('postes.txt', 'r') as file:
    postes = json.load(file)
#print(postes)
#print(postes["matin"]["heure_debut"])

for key in postes:
    print(key)