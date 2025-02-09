from Bibliotheque import bibliotheque,clear_console

class Menu:
    def __init__(self):
        self.bibliotheque = bibliotheque()

    # Afficher le menu principal
    def Afficher_menu_principal(self):
        clear_console()
        print("\n===== Gestion de la bibliothèque =====")
        print("1 - Operations sur les livres")
        print("2 - Operations sur les utilisateurs")
        print("3 - Quitter")

    # Afficher le sous-menu pour les livres
    def afficher_sous_menu_livres(self):
        clear_console()
        print("\n===== Operations sur les livres =====")
        print("1 - Ajouter un livre")
        print("2 - Mettre à jour un livre")
        print("3 - Supprimer un livre")
        print("4 - Rechercher un livre")
        print("5 - Lister les livres disponibles")
        print("6 - Retour au menu principal")

    # Afficher le sous-menu pour les utilisateurs
    def afficher_sous_menu_utilisateurs(self):
        clear_console()
        print("\n===== Operations sur les utilisateurs =====")
        print("1 - Ajouter un utilisateur")
        print("2 - Modifier un utilisateur")
        print("3 - Supprimer un utilisateur")
        print("4 - Lister les utilisateurs")
        print("5 - Prêter un livre")
        print("6 - Retourner un livre")
        print("7 - Lister les livres en retard")
        print("8 - Generer des statistiques")
        print("9 - Retour au menu principal")

    # Gerer les operations du sous-menu des livres
    def gerer_sous_menu_livres(self):
        while True:
            self.afficher_sous_menu_livres()
            choix = input("Faites votre choix : ")
            if choix == "1":
                self.bibliotheque.ajouter_livre()
            elif choix == "2":
                isbn = input("Entrez l'ISBN du livre à mettre à jour : ")
                titre = input("Entrez le nouveau titre (laisser vide pour aucun changement) : ")
                auteur = input("Entrez le nouvel auteur (laisser vide pour aucun changement) : ")
                genre = input("Entrez le nouveau genre (laisser vide pour aucun changement) : ")
                self.bibliotheque.mettre_a_jour_livre(isbn, titre, auteur, genre)
            elif choix == "3":
                isbn = input("Entrez l'ISBN du livre à supprimer : ")
                self.bibliotheque.supprimer_livre(isbn)
            elif choix == "4":
                titre = input("Entrez le titre du livre à rechercher : ")
                self.bibliotheque.rechercher_livre_par_titre(titre)
            elif choix == "5":
                self.bibliotheque.lister_livres_disponibles()
            elif choix == "6":
                break  # Retour au menu principal
            else:
                print("Choix invalide. Veuillez reessayer.")

    # Gerer les operations du sous-menu des utilisateurs
    def gerer_sous_menu_utilisateurs(self):
        while True:
            self.afficher_sous_menu_utilisateurs()
            choix = input("Faites votre choix : ")
            if choix == "1":
                self.bibliotheque.ajouter_utilisateur()
            elif choix == "2":
                user_id = input("Entrez l'ID de l'utilisateur à modifier : ")
                nom = input("Entrez le nouveau nom (laisser vide pour aucun changement) : ")
                prenom = input("Entrez le nouveau prenom (laisser vide pour aucun changement) : ")
                telephone = input("Entrez le nouveau numero de telephone (laisser vide pour aucun changement) : ")
                adresse = input("Entrez la nouvelle adresse (laisser vide pour aucun changement) : ")
                activite = input("Entrez la nouvelle activite (laisser vide pour aucun changement) : ")
                email = input("Entrez le nouvel email (laisser vide pour aucun changement) : ")
                self.bibliotheque.modifier_utilisateur(user_id, nom, prenom, telephone, adresse, activite, email)
            elif choix == "3":
                user_id = input("Entrez l'ID de l'utilisateur à supprimer : ")
                self.bibliotheque.supprimer_utilisateur(user_id)
            elif choix == "4":
                self.bibliotheque.lister_utilisateurs()
            elif choix == "5":
                user_id = input("Entrez l'ID de l'utilisateur : ")
                isbn = input("Entrez l'ISBN du livre à emprunter : ")
                self.bibliotheque.preter_livre(user_id, isbn)
            elif choix == "6":
                isbn = input("Entrez l'ISBN du livre à retourner : ")
                self.bibliotheque.retourner_livre(isbn)
            elif choix == "7":
                self.bibliotheque.lister_livres_en_retard()
            elif choix == "8":
                self.bibliotheque.generer_statistiques()
            elif choix == "9":
                break  # Retour au menu principal
            else:
                print("Choix invalide. Veuillez reessayer.")
                input("Entrer Enter pour continuer...")

    # Demarrer l'application
    def demarrer(self):
        try:
            while True:
                self.Afficher_menu_principal()
                choix = input("Faites votre choix : ")
                if choix == "1":
                    self.gerer_sous_menu_livres()
                elif choix == "2":
                    self.gerer_sous_menu_utilisateurs()
                elif choix == "3":
                    print("Merci d'avoir utilise notre système ! Au revoir !")
                    break
                else:
                    print("Choix invalide. Veuillez reessayer.")
                    input("Entrer Enter pour continuer...")
        finally:
            # Sauvegarder les donnees dans les fichiers CSV
            self.bibliotheque.save_data()


if __name__ == "__main__":
    menu = Menu()
    menu.demarrer()