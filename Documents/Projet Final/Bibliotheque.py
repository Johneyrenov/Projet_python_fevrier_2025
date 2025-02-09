import csv
import re  # Module pour les expressions regulières
from datetime import datetime, timedelta
from classes import Utilisateur, Livre, Emprunt
import random
import os

class bibliotheque:
    def __init__(self):
        self.livres = []
        self.utilisateurs = []
        self.emprunts = []
        self.load_donnees()

    # Charger les donnees depuis les fichiers CSV
    def load_donnees(self):
        try:
            with open("livres.csv", mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.livres.append(Livre.from_dict(row))  
        except FileNotFoundError:
            print("Aucun fichier de livres trouve. Un nouveau fichier sera cree.")

        try:
            with open("utilisateurs.csv", mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.utilisateurs.append(Utilisateur.from_dict(row))
        except FileNotFoundError:
            print("Aucun fichier d'utilisateurs trouve. Un nouveau fichier sera cree.")

        try:
            with open("emprunts.csv", mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.emprunts.append(Emprunt.from_dict(row))
        except FileNotFoundError:
            print("Aucun fichier d'emprunts trouve. Un nouveau fichier sera cree.")

    # Sauvegarder les donnees dans les fichiers CSV
    def save_data(self):
        with open("livres.csv", mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["isbn", "titre", "auteur", "genre", "disponible"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for livre in self.livres:
                writer.writerow(livre.to_dict())

        with open("utilisateurs.csv", mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["user_id", "nom", "prenom", "telephone", "adresse", "activite", "email"]
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

    def is_isbn_unique(self, isbn):
      
        for livre in self.livres:
            if livre.isbn == isbn:
                return False
        return True

    # Ajouter un livre
    def ajouter_livre(self):
        clear_console()  # Nettoyer l'ecran avant de commencer
        print("\n===*** Ajout d'un nouveau livre ***===")
        
        # Demander l'ISBN (doit être unique)
        while True:
            isbn = input("Entrez l'ISBN du livre : ").strip()
            if not isbn:  # Verifie si le champ est vide
                clear_console()
                print("Erreur : L'ISBN est obligatoire. Veuillez reessayer.")
                continue  # Redemander la saisie
            if self.is_isbn_unique(isbn):  # Verifie que l'ISBN est unique
                break
            clear_console()
            print("Erreur : L'ISBN existe dejà. Veuillez reessayer.")
        
        # Demander le titre (obligatoire)
        while True:
            titre = input("Entrez le titre du livre : ").strip()
            if titre:  # Verifie que le titre n'est pas vide
                break
            clear_console()
            print("Erreur : Le titre est obligatoire. Veuillez reessayer.")
        
        # Demander l'auteur (obligatoire)
        while True:
            auteur = input("Entrez l'auteur du livre : ").strip()
            if auteur:  # Verifie que l'auteur n'est pas vide
                break
            clear_console()
            print("Erreur : L'auteur est obligatoire. Veuillez reessayer.")
        
        # Demander le genre (obligatoire)
        while True:
            genre = input("Entrez le genre du livre : ").strip()
            if genre:  # Verifie que le genre n'est pas vide
                break
            clear_console()
            print("Erreur : Le genre est obligatoire. Veuillez reessayer.")
     
        
        # Creer un nouveau livre
        livre = Livre(isbn, titre, auteur, genre)
        self.livres.append(livre)
        self.save_data()
   
        print(f"\nLivre '{titre}' ajoute avec succès !")
        input("Presser Enter pour continuer...")

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
                print(f"Le livre avec ISBN {isbn} a ete mis à jour.")
                return
        print(f"Aucun livre trouve avec ISBN {isbn}.")
        input("Entrer Enter pour continuer...")

    # Supprimer un livre
    def supprimer_livre(self, isbn):
        self.livres = [livre for livre in self.livres if livre.isbn != isbn]
        self.save_data()
        print(f"Livre avec ISBN {isbn} supprime.")
        input("Entrer Enter pour continuer...")

    # Rechercher un livre par titre
    def rechercher_livre_par_titre(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                print(livre)
                return
        print(f"Aucun livre trouve avec le titre '{titre}'.")
        input("Entrer Enter pour continuer...") 
   
    # Ajouter un utilisateur
    def ajouter_utilisateur(self):
        clear_console()
        print("\n=== Ajout d'un nouvel utilisateur ===")
        
        # Demander le nom (obligatoire)
        while True:
            nom = input("Entrez le nom de l'utilisateur : ").strip()
            if nom and nom.replace(" ", "").isalpha():
                break
            clear_console()
            print("Erreur : Le nom est obligatoire et doit contenir uniquement des lettres.")
        
        # Demander le prenom (obligatoire)
        while True:
            prenom = input("Entrez le prenom de l'utilisateur : ").strip()
            if prenom and prenom.replace(" ", "").isalpha():
                break
            clear_console()
            print("Erreur : Le prenom est obligatoire et doit contenir uniquement des lettres. Veuillez reessayer.")
        
        # Demander le telephone (obligatoire)
        while True:
            telephone = input("Entrez le numero de telephone : ").strip()
            if telephone.isdigit():
                break
            clear_console()
            print("Erreur : Le telephone est obligatoire. Veuillez reessayer.")
        
        # Demander l'adresse (obligatoire)
        while True:
            adresse = input("Entrez l'adresse de l'utilisateur : ").strip()
            if adresse:
                break
            clear_console()
            print("Erreur : L'adresse est obligatoire. Veuillez reessayer.")
        
        # Demander l'activite (obligatoire)
        while True:
            activite = input("Entrez l'activite de l'utilisateur : ").strip()
            if activite and activite.replace(" ", "").isalpha():
                break
            clear_console()
            print("Erreur : L'activite est obligatoire. Veuillez reessayer.")
        
        # Demander l'email (obligatoire)
        while True:
            email = input("Entrez l'adresse email de l'utilisateur : ").strip()
            if email and re.match(r"[^@]+@[^@]+\.[^@]+", email):
                break
            clear_console()
            print("Erreur : L'email est obligatoire et doit être au format valide.")
        
        # Generer un ID unique pour l'utilisateur
        user_id = f"{nom[0].upper()}{prenom[0].upper()}{random.randint(10000, 99999)}"
        
        # Creer un nouvel utilisateur
        utilisateur = Utilisateur(user_id, nom, prenom, telephone, adresse, activite, email)
        
        # Ajouter l'utilisateur à la liste
        self.utilisateurs.append(utilisateur)
        
        # Sauvegarder les donnees
        self.save_data()
       
        print(f"\nUtilisateur '{nom} {prenom}' ajoute avec succès !")
        input("Appuyez sur Enter pour continuer...")
        
    # Supprimer un utilisateur
    def supprimer_utilisateur(self, user_id):
        utilisateur_trouve = None
        for utilisateur in self.utilisateurs:
            if utilisateur.user_id == user_id:
                utilisateur_trouve = utilisateur
                break
        
        if utilisateur_trouve:
            self.utilisateurs.remove(utilisateur_trouve)
            print(f"L'utilisateur avec l'ID {user_id} a ete supprime avec succès.")
        else:
            print(f"L'utilisateur avec l'ID {user_id} n'existe pas.")
        self.save_data()
        input("Appuyez sur Enter pour continuer...")

    # Modifier un utilisateur
    def modifier_utilisateur(self, user_id, nouveau_nom=None, nouveau_prenom=None, nouveau_telephone=None, nouvelle_adresse=None, nouvelle_activite=None, nouvel_email=None):
        # Chercher l'utilisateur dans la liste
        utilisateur = next((u for u in self.utilisateurs if u.user_id == user_id), None)
        if utilisateur is None:
            print(f"Aucun utilisateur trouve avec l'ID {user_id}.")
            input("Appuyez sur Enter pour continuer...")
            return  
        
        # Mettre à jour les informations de l'utilisateur
        if nouveau_nom:
            utilisateur.nom = nouveau_nom
        if nouveau_prenom:
            utilisateur.prenom = nouveau_prenom
        if nouveau_telephone:
            utilisateur.telephone = nouveau_telephone
        if nouvelle_adresse:
            utilisateur.adresse = nouvelle_adresse
        if nouvelle_activite:
            utilisateur.activite = nouvelle_activite
        if nouvel_email:
            utilisateur.email = nouvel_email
        
        # Sauvegarder les donnees après la modification
        self.save_data()
        print(f"Les informations de l'utilisateur avec l'ID {user_id} ont ete mises à jour.")
        input("Appuyez sur Enter pour continuer...")

    # Lister les utilisateurs
    def lister_utilisateurs(self):
        for utilisateur in self.utilisateurs:
            print(utilisateur)
            input("Appuyez sur Enter pour continuer...")

    # Prêter un livre
    def preter_livre(self, user_id, isbn):
        livre = next((livre for livre in self.livres if livre.isbn == isbn and livre.disponible), None)
        if not livre:
            print("Le livre n'est pas disponible.")
            input("Appuyez sur Enter pour continuer...")
            return

        utilisateur = next((u for u in self.utilisateurs if u.user_id == user_id), None)
        if not utilisateur:
            print("Utilisateur non trouve.")
            input("Appuyez sur Enter pour continuer...")
            return

        # Saisie de la date de retour prevue
        while True:
            date_retour_str = input("Entrez la date de retour prevue (format JJ/MM/AAAA) : ").strip()
            try:
                date_retour_prevue = datetime.strptime(date_retour_str, "%d/%m/%Y")
                break
                clear_console()
            except ValueError:
                print("Erreur : Format de date invalide. Veuillez utiliser le format JJ/MM/AAAA.")
                input("Appuyez sur Enter pour continuer...")
        # Date d'emprunt (date actuelle)
        date_emprunt = datetime.now()

        # Creer un nouvel emprunt
        emprunt = Emprunt(user_id, isbn, date_emprunt, date_retour_prevue)

        # Marquer le livre comme indisponible
        livre.disponible = False

        # Ajouter l'emprunt à la liste
        self.emprunts.append(emprunt)

        # Sauvegarder les donnees
        self.save_data()

        print(f"Livre '{livre.titre}' prête à {utilisateur.prenom}. Date de retour prevue : {date_retour_prevue.strftime('%d/%m/%Y')}.")
        input("Entrer Enter pour continuer...")

    # Retourner un livre
    def retourner_livre(self, isbn):
        emprunt = next((e for e in self.emprunts if e.isbn == isbn and not e.retourne), None)
        if not emprunt:
            print("Aucun emprunt trouve pour ce livre.")
            return

        emprunt.retourne = True
        livre = next((livre for livre in self.livres if livre.isbn == isbn), None)
        if livre:
            livre.disponible = True

        print(f"Livre '{livre.titre}' retourne avec succès.")
        input("Entrer Enter pour continuer...")

    # Lister les livres en retard
    def lister_livres_en_retard(self):
        today = datetime.now()
        livres_en_retard = []

        for emprunt in self.emprunts:
            if not emprunt.retourne and emprunt.date_retour_prevue < today:
                livre = next((livre for livre in self.livres if livre.isbn == emprunt.isbn), None)
                utilisateur = next((u for u in self.utilisateurs if u.user_id == emprunt.user_id), None)
                if livre and utilisateur:
                    livres_en_retard.append((livre, utilisateur, emprunt.date_retour_prevue))

        if not livres_en_retard:
            print("Aucun livre en retard.")
            input("Entrer Enter pour continuer...")
        else:
            print("\n=== Livres en retard ===")
            for livre, utilisateur, date_retour_prevue in livres_en_retard:
                print(f"Livre : {livre.titre}, Emprunte par : {utilisateur.prenom} {utilisateur.nom}, Date de retour prevue : {date_retour_prevue.strftime('%d/%m/%Y')}")
                input("Entrer Enter pour continuer...")

    # Generer des statistiques
    def generer_statistiques(self):
        total_emprunts = len(self.emprunts)
        livres_retournes = sum(1 for e in self.emprunts if e.retourne)
        livres_en_retard = total_emprunts - livres_retournes
        print(f"Total emprunts: {total_emprunts}, Livres retournes: {livres_retournes}, En retard: {livres_en_retard}")
        input("Entrer Enter pour continuer...")


def clear_console():
   
    if os.name == 'nt':  # Pour Windows
        os.system('cls')
    else:  # Pour macOS et Linux
        os.system('clear')