
from Bibliotheque import bibliotheque
#from menu import Menu
#Classe representant le menu de l'application

class Menu:
    def __init__(self):
        self.bibliotheque = bibliotheque()
    #Affichache menu principal
    def Afficher_menu_principal(self):
        print("\n=====Gestion de la bibliotheque====")
        print("1-Operations sur les livres")
        print("2-Operations sur utilisateurs")
        print("3-Quitter") 
    #Sous_menu pour les livres
    def afficher_sous_menu_livres(self):
        print("\n=====Operations sur les livres===")
        print("1-Ajouter un livre") 
        print("2-Mettre a jour un livre") 
        print("3-Supprimer un livre") 
        print("4-Rechercher un livre") 
        print("5-Lister les livres dispos") 
        print("6-Retour au menu principal") 
        
#Sous_menu pour les users
    def afficher_sous_menu_utilisateurs(self):
        print("\n=====Operations sur les utilisateurs===")
        print("1-Ajouter un utilisateurs") 
        print("2-Modifier un utilisateurs") 
        print("3-Supprimer un utilisateur") 
        print("4-Lister les utilisateurs")
        print("5-Preter un livre") 
        print("6-Retourner un livre") 
        print("7-Lister les livres en retard")
        print("8-Generer des statistiques")
        print("9-Retour au menu principal")
 #Gerer operations du sous_menu des livres       
    def gerer_sous_menu_livres(self):
     while True:
        self.afficher_sous_menu_livres()
        choix = input("Faites votre choix : ")
        if choix == "1":
            isbn = input("Entrer l'ISBN du livre : ")
            titre = input("Entrer le titre du livre : ")
            auteur = input("Entrer l'auteur du livre : ")
            genre = input("Entrer le genre du livre : ")
            self.bibliotheque.ajouter_livre(isbn, titre, auteur,genre)
        elif choix == "2":
             isbn = input("Entrer l'ISBN du livre a mettre a jour: ")
             titre= input("Entrer le nouveau titre(Laisser vide pour aucun changement) : ")
             auteur= input("Entrer le nouvel auteur du livre (Laisser vide pour aucun changement) : ")
             genre = input("Entrer le nouveau genre (Laisser vide pour aucun changement) : ")
             self.bibliotheque.mettre_a_jour_livre(isbn,titre,auteur,genre)
        elif choix == "3":
            isbn=input("Entrer ISBN du livre a supprimer : ")
            self.bibliotheque.supprimer_livre(isbn)
        elif choix == "4":
            titre = input("Entrer le titre du livre a rechercher : ")
            self.bibliotheque.rechercher_livre_par_titre(titre)
        elif choix == "5":
            self.bibliotheque.lister_livres_disponibles()
        elif choix == "6":
            break #Retour au main menu
        else:
            print("Choix invalide.Veuillez reessayer.")
            
    #Gerer operations sous_menu users
    def gerer_sous_menu_utilisateurs(self):
        while True:
            self.afficher_sous_menu_utilisateurs()
            choix = input("Faites votre choix : ")
            if choix == "1":
                user_id = input("Entrer l'ID de utilisateur : ")
                nom = input("Entrer le nom de l'utilisateur :")
                contact = input("Saisir les infos de contact : ")
                self.bibliotheque.ajouter_utilisateur(user_id, nom, contact)
            elif choix == "2":
                 user_id = input("Entrer l'ID de l'utilisateur à modifier : ")
                 nom = input("Entrer le nouveau nom de l'utilisateur (laisser vide pour rien changer) : ")
                 contact = input("Saisir les nouvelles informations de contact (laisser vide pour aucun changement) : ")
    # Passer les nouveaux arguments à modifier_utilisateur
                 self.bibliotheque.modifier_utilisateur(user_id, nouveau_nom=nom if nom else None, nouveau_contact=contact if contact else None)

            elif choix == "3":
                user_id = input("Entrer ID de l'utilsateur a supprimer : ") 
                self.bibliotheque.supprimer_utilisateur(user_id)
            elif choix == "4": 
                self.bibliotheque.lister_utilisateurs()
            elif choix == "5":
                user_id = input("Entrez l'ID de l'utilisateur : ")
                isbn = input("Entrer ISBN du livre a emprunter : ")
                self.bibliotheque.preter_livre(user_id,isbn)
            elif choix == "6":
                isbn = input("Entrer ISBN du livre a retourner : ")
                self.bibliotheque.retourner_livre(isbn)
            elif choix == "7":
                self.bibliotheque.lister_livres_en_retard()
            elif choix == "8":  
                self.bibliotheque.generer_statistiques()
            elif choix == "9":
                break 
            else:
                print("Choix invalide.Reessayer!")
            
            #Demarrer app 
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
                    print("Merci d'avoir utilisé notre système ! Au revoir !")
                    break
                else:
                    print("Choix invalide. Reessayez")
        finally:
            # Add donnees dans le fichier CSV
            self.bibliotheque.save_data()
                
if __name__ == "__main__":
     menu = Menu()
     menu.demarrer()

                
                
                
            
            
    