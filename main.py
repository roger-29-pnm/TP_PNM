
from boisson import commander
liste_commandes = commandes()

print("\n Récapitulatif de vos commandes :")
for i, boisson in enumerate(liste_commandes, 1):
    print(f"{i}. {boisson}")
