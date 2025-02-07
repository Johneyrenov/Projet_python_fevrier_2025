from datetime import datetime
from fonctions import (
    charger_livres, sauvegarder_livres, ajouter_livre, supprimer_livre,
    rechercher_livre, afficher_livres, ajouter_utilisateur, sauvegarder_utilisateurs, charger_utilisateurs,
    enregistrer_emprunt, retourner_livre, charger_emprunts, sauvegarder_emprunts,
    generer_statistiques
)

# Fichiers CSV
FICHIER_LIVRES = "livres.csv"
FICHIER_UTILISATEURS = "users.csv"
FICHIER_EMPRUNTS = "emprunts.csv"

# Chargement des donnes
livres = charger_livres(FICHIER_LIVRES)
utilisateurs = charger_utilisateurs(FICHIER_UTILISATEURS)
emprunts = charger_emprunts(FICHIER_EMPRUNTS)

def menu():
    while True:
        print("\n===== MENU BIBLIOTHEQUE =====")
        print("1. Ajouter un livre")
        print("2. Supprimer un livre")
        print("3. Rechercher un livre")
        print("4. Afficher tous les livres")
        print("5. Ajouter un utilisateur")
        print("6. Enregistrer un emprunt")
        print("7. Retourner un livre")
        print("8. Afficher les statistiques")
        print("9. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            isbn = input("ISBN : ")
            titre = input("Titre : ")
            auteur = input("Auteur : ")
            genre = input("Genre : ")
            ajouter_livre(FICHIER_LIVRES, livres, isbn, titre, auteur, genre)
            print("Livre ajoute avec succes.")

        elif choix == "2":
            isbn = input("ISBN du livre a supprimer : ")
            livres[:] = supprimer_livre(FICHIER_LIVRES, livres, isbn)
            print("Livre supprime avec succes.")

        elif choix == "3":
            terme = input("Entrez un mot-cle (titre, auteur, genre) : ")
            resultats = rechercher_livre(livres, terme)
            if resultats:
                afficher_livres(resultats)
            else:
                print("Aucun livre trouve.")

        elif choix == "4":
            afficher_livres(livres)

        elif choix == "5":
            user_id = input("ID utilisateur : ")
            nom = input("Nom : ")
            contact = input("Contact : ")
            ajouter_utilisateur(FICHIER_UTILISATEURS, utilisateurs, user_id, nom, contact)
            print("Utilisateur ajoute avec succes.")

        elif choix == "6":
            user_id = input("ID utilisateur : ")
            isbn = input("ISBN du livre : ")
            date_retour_prevue = input("Date de retour prevue (YYYY-MM-DD) : ")
            enregistrer_emprunt(FICHIER_EMPRUNTS, emprunts, user_id, isbn, date_retour_prevue)
            print("Emprunt enregistre avec succes.")

        elif choix == "7":
            isbn = input("ISBN du livre a retourner : ")
            retourner_livre(FICHIER_EMPRUNTS, emprunts, isbn)
            print("Livre retourner avec succes.")

        elif choix == "8":
            stats = generer_statistiques(livres, emprunts)
            print(f"Total de livres : {stats['total_livres']}")
            print(f"Livres empruntes : {stats['livres_empruntes']}")
            print(f"Livres disponibles : {stats['livres_disponibles']}")

        elif choix == "9":
            print("Au revoir !")
            break

        else:
            print("Choix invalide, veuillez reessayer.")

if __name__ == "__main__":
    menu()
