import csv
from datetime import datetime, timedelta
from classes import Utilisateur, Livre, Emprunt

class bibliotheque:
    def __init__(self):
        self.livres = []
        self.utilisateurs = []
        self.emprunts = []
        self.load_donnees()

    # Charger les données depuis les fichiers CSV
    def load_donnees(self):
        try:
            with open("livres.csv", mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.livres.append(Livre.from_dict(row))  
        except FileNotFoundError:
            print("Aucun fichier de livres trouvé. Un nouveau fichier sera créé.")

        try:
            with open("utilisateurs.csv", mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.utilisateurs.append(Utilisateur.from_dict(row))
        except FileNotFoundError:
            print("Aucun fichier d'utilisateurs trouvé. Un nouveau fichier sera créé.")

        try:
            with open("emprunts.csv", mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.emprunts.append(Emprunt.from_dict(row))
        except FileNotFoundError:
            print("Aucun fichier d'emprunts trouvé. Un nouveau fichier sera créé.")

    # Sauvegarder les données dans les fichiers CSV
    def save_data(self):
        with open("livres.csv", mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["isbn", "titre", "auteur", "genre", "disponible"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for livre in self.livres:
                writer.writerow(livre.to_dict())

        with open("utilisateurs.csv", mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["user_id", "nom", "contact"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for utilisateur in self.utilisateurs:
                writer.writerow(utilisateur.to_dict())

        with open("emprunts.csv", mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["user_id", "isbn", "date_emprunt", "date_retour_prevue", "retourne"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for emprunt in self.emprunts:
                writer.writerow(emprunt.to_dict())

    # Ajouter un livre
    def ajouter_livre(self, isbn, titre, auteur, genre):
        livre = Livre(isbn, titre, auteur, genre)
        self.livres.append(livre)
        self.save_data()
        print(f"Livre '{titre}' ajouté avec succès !")

    # Lister les livres disponibles
    def lister_livres_disponibles(self):
        livres_disponibles = [livre for livre in self.livres if livre.disponible]
        if not livres_disponibles:
            print("Aucun livre disponible.")
        else:
            for livre in livres_disponibles:
                print(livre)

    # Mettre à jour un livre
    def mettre_a_jour_livre(self, isbn, titre, auteur, genre):
        for livre in self.livres:
            if livre.isbn == isbn:
                if titre:
                    livre.titre = titre
                if auteur:
                    livre.auteur = auteur
                if genre:
                    livre.genre = genre
                self.save_data()
                print(f"Le livre avec ISBN {isbn} a été mis à jour.")
                return
        print(f"Aucun livre trouve avec ISBN {isbn}.")

    # Supprimer un livre
    def supprimer_livre(self, isbn):
        self.livres = [livre for livre in self.livres if livre.isbn != isbn]
        self.save_data()
        print(f"Livre avec ISBN {isbn} supprimé.")

    # Rechercher un livre par titre
    def rechercher_livre_par_titre(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                print(livre)
                return
        print(f"Aucun livre trouve avec le titre '{titre}'.")

    # Ajouter un utilisateur
    def ajouter_utilisateur(self, user_id, nom, contact):
        utilisateur = Utilisateur(user_id, nom, contact)
        self.utilisateurs.append(utilisateur)
        self.save_data()
        print(f"Utilisateur '{nom}' ajouté avec succès!")

    # Supprimer un utilisateur
    def supprimer_utilisateur(self, user_id):
        self.utilisateurs = [utilisateur for utilisateur in self.utilisateurs if utilisateur.user_id != user_id]
        self.save_data()
        print(f"Utilisateur {user_id} supprimé.")
        
    def modifier_utilisateur(self, user_id, nouveau_nom=None, nouveau_contact=None):
    # Chercher l'utilisateur dans la liste
        utilisateur = next((utilisateur for utilisateur in self.utilisateurs if utilisateur.user_id == user_id), None)

        if utilisateur is None:
              print(f"Aucun utilisateur trouvé avec l'ID {user_id}.")
              return

    # Mettre à jour les informations de l'utilisateur seulement si de nouvelles valeurs sont passées
        if nouveau_nom:
            utilisateur.nom = nouveau_nom
        if nouveau_contact:
                utilisateur.contact = nouveau_contact

    # Sauvegarder les données après la modification
        self.save_data()
        print(f"Les informations de l'utilisateur avec l'ID {user_id} ont été mises à jour.")

    
    # Lister les utilisateurs
    def lister_utilisateurs(self):
        for utilisateur in self.utilisateurs:
            print(utilisateur)

    # Prêter un livre
    def preter_livre(self, user_id, isbn):
        livre = next((livre for livre in self.livres if livre.isbn == isbn and livre.disponible), None)
        if not livre:
            print("Le livre n'est pas disponible.")
            return

        utilisateur = next((u for u in self.utilisateurs if u.user_id == user_id), None)
        if not utilisateur:
            print("Utilisateur non trouvé.")
            return

        date_emprunt = datetime.now()
        date_retour_prevue = date_emprunt + timedelta(days=14)
        emprunt = Emprunt(user_id, isbn, date_emprunt, date_retour_prevue)

        livre.disponible = False
        self.emprunts.append(emprunt)
        self.save_data()
        print(f"Livre '{livre.titre}' prêté à {utilisateur.nom}.")

    # Retourner un livre
    def retourner_livre(self, isbn):
        emprunt = next((e for e in self.emprunts if e.isbn == isbn and not e.retourne), None)
        if not emprunt:
            print("Aucun emprunt trouvé pour ce livre.")
            return

        emprunt.retourne = True
        livre = next((livre for livre in self.livres if livre.isbn == isbn), None)
        if livre:
            livre.disponible = True

        print(f"Livre '{livre.titre}' retourné avec succès.")

    # Lister les livres en retard
    def lister_livres_en_retard(self):
        today = datetime.now()
        retards = [e for e in self.emprunts if not e.retourne and e.date_retour_prevue < today]
        for emprunt in retards:
            print(emprunt)

    # Générer des statistiques
    def generer_statistiques(self):
        total_emprunts = len(self.emprunts)
        livres_retournes = sum(1 for e in self.emprunts if e.retourne)
        livres_en_retard = total_emprunts - livres_retournes
        print(f"Total emprunts: {total_emprunts}, Livres retournés: {livres_retournes}, En retard: {livres_en_retard}")
