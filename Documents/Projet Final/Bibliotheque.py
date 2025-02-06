from classes import Livre
from classes import Utilisateur
from datetime import datetime,timedelta
class bibliotheque:
    def __init__(self):
        self.livres = []
        self.utilisateurs =[]
        self.emprunts = []
        #Methode pour les livres
        #Ajouter livres
    def ajouter_livre(self,isbn,titre,auteur,genre):
        livre = Livre(isbn,titre,auteur,genre)
        self.livres.append(livre)
        print(f"Livre '{titre}' ajoute avec succes !")
        
        #Lister livre dispo
    def lister_livres_disponibles(self):
        if not self.livres:
            print("Aucun livre disponible.")
        else:
            for livre in self.livres:
                print(livre)
    
    def mettre_a_jour_livre(self, isbn, titre, auteur, genre):
        for livre in self.livres:
            if livre.isbn == isbn:
                if titre:
                    livre.titre = titre
                if auteur:
                    livre.auteur = auteur
                if genre:
                    livre.genre = genre
                print(f"Le livre avec ISBN {isbn} a été mis a jour")
                return
        print(f"Aucun livre trouve avec ISBN {isbn}.")
        
    
    def supprimer_livre(self, isbn):
        for livre in self.livres:
            if livre.isbn == isbn:
                self.livres.remove(livre)
                print(f"Le livre avec ISBN {isbn} a été supprimé.")
                return
        print(f"Aucun livre trouvé avec ISBN {isbn}.")

    def rechercher_livre_par_titre(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                print(livre)
                return
        print(f"Aucun livre trouvé avec le titre '{titre}'.")
        
    #Methodes pour les utilisateurs
    def ajouter_utilisateur(self, user_id, nom, contact):
        utilisateur = Utilisateur(user_id, nom, contact)
        self.utilisateurs.append(utilisateur)
        print(f"Utilisateur '{nom}' ajouté avec succès!")
        
    def supprimer_utilisateur(self, user_id):
        for utilisateur in self.utilisateurs:
            if utilisateur.user_id == user_id:
                self.utilisateurs.remove(utilisateur)
                print(f"Utilisateur {user_id} supprimé.")
                return
        print(f"Aucun utilisateur trouvé avec ID {user_id}.")
    
    def lister_utilisateurs(self):
        if not self.utilisateurs:
            print("Aucun utilisateur inscrit.")
        else:
            for utilisateur in self.utilisateurs:
                print(utilisateur)
                
    def rechercher_utilisateur_par_id(self, user_id):
        for utilisateur in self.utilisateurs:
            if utilisateur.user_id == user_id:
                print(utilisateur)
                return
        print(f"Aucun utilisateur trouvé avec l'ID {user_id}.")
        
    #Methodes sur les emprunts
    def preter_livre(self,user_id,isbn):
        livre = next((livre for livre in self.livres if livre.isbn == isbn and livre.disponible), None)
        if livre is None:
            print("Le livre n'est pas disponible.")
            return
        #Verifier si user existe
        utilisateur = next((utilisateur for utilisateur in self.utilisateurs if utilisateur.user_id == user_id), None)
        if utilisateur is None:
            print("Utilisateur non trouve")
            return
        #Enregistrer un emprunt
        date_emprunt = datetime.now()
        date_retour_prevue = date_emprunt + timedelta(days=14)  
        emprunt = emprunt(user_id, isbn, date_emprunt, date_retour_prevue)
        
      #Assigner l'emprunt a l'utilisateur et le mettre non disponible
        utilisateur.emprunter(emprunt)
        livre.disponible = False
        self.emprunts.append(emprunt)
        print(f"Le livre {livre.titre} a été prêté à {utilisateur.nom}.")
         # Trouver l'emprunt en cours 
    def retourner_livre(self, isbn):
        emprunt = next((emprunt for emprunt in self.emprunts if emprunt.isbn == isbn and not emprunt.retourne), None)
        if emprunt is None:
            print("Aucun emprunt trouvé pour ce livre")
            return
        #Marquer emprunt retourne
        emprunt.retourne = True

        # Mettre à jour la disponibilité du livre
        livre = next((livre for livre in self.livres if livre.isbn == isbn), None)
        if livre:
            livre.disponible = True

        print(f"Le livre {livre.titre} a été retourne")
        
    def lister_livres_en_retard(self):
        today = datetime.now()
        livres_en_retard = [emprunt for emprunt in self.emprunts if not emprunt.retourne and emprunt.date_retour_prevue < today]
        if not livres_en_retard:
            print("Aucun livre en retard")
        else:
            for emprunt in livres_en_retard:
                print(emprunt)
                
    def generer_statistiques(self):
        total_emprunts = len(self.emprunts)
        livres_retournes = len([emprunt for emprunt in self.emprunts if emprunt.retourne])
        livres_en_retard = total_emprunts - livres_retournes
        print(f"Total emprunts: {total_emprunts}")
        print(f"Livres retournés: {livres_retournes}")
        print(f"Livres en retard: {livres_en_retard}")