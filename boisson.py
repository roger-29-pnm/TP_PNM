def commander():
    commandes = []
    choix = 0

    while choix != 4:
        print("\nMenu :")
        print("1. Café")
        print("2. Thé")
        print("3. Eau")
        print("4. Quitter")
        try:
            choix = int(input("Entrez votre choix : "))
        except ValueError:
            print("Veuillez entrer un nombre.")
            continue

        if choix == 1:
            commandes.append("Café")
            print("Vous avez commandé un Café.")
        elif choix == 2:
            commandes.append("Thé")
            print("Vous avez commandé un Thé.")
        elif choix == 3:
            commandes.append("Eau")
            print("Vous avez commandé de l'Eau.")
        elif choix == 4:
            print("Fin des commandes.")
        else:
            print("Choix invalide. Veuillez réessayer.")

