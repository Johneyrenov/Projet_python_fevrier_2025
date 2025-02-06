import csv
from datetime import datetime
from classes import Livre, Utilisateur, Emprunt

# livres

def charger_livres(fichier_csv):
    try:
        with open(fichier_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [Livre(row['isbn'], row['titre'], row['auteur'], row['genre'], row['disponible'] == 'True') for row in reader]
    except FileNotFoundError:
        return []

def sauvegarder_livres(fichier_csv, livres):
    with open(fichier_csv, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['isbn', 'titre', 'auteur', 'genre', 'disponible']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for livre in livres:
            writer.writerow({'isbn': livre.isbn, 'titre': livre.titre, 'auteur': livre.auteur, 'genre': livre.genre, 'disponible': livre.disponible})

def ajouter_livre(fichier_csv, livres, isbn, titre, auteur, genre):
    nouveau_livre = Livre(isbn, titre, auteur, genre)
    livres.append(nouveau_livre)
    sauvegarder_livres(fichier_csv, livres)

def supprimer_livre(fichier_csv, livres, isbn):
    livres = [livre for livre in livres if livre.isbn != isbn]
    sauvegarder_livres(fichier_csv, livres)
    return livres

def rechercher_livre(livres, terme):
    return [livre for livre in livres if terme.lower() in livre.titre.lower() or terme.lower() in livre.auteur.lower() or terme.lower() in livre.genre.lower()]

def afficher_livres(livres):
    for livre in livres:
        print(livre)

# users

def charger_utilisateurs(fichier_csv):
    try:
        with open(fichier_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [Utilisateur(row['user_id'], row['nom'], row['contact']) for row in reader]
    except FileNotFoundError:
        return []

def sauvegarder_utilisateurs(fichier_csv, utilisateurs):
    with open(fichier_csv, mode='w', newline='', encoding= 'utf-8') as file:
        fieldnames = ['user_id', 'nom', 'contact']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for utilisateur in utilisateurs:
            writer.writerow({'user_id': utilisateur.user_id, 'nom': utilisateur.nom, 'contact': utilisateur.contact})

def ajouter_utilisateur(fichier_csv, utilisateurs, user_id, nom, contact):
    utilisateur = Utilisateur(user_id, nom, contact)
    utilisateurs.append(utilisateur)
    sauvegarder_utilisateurs(fichier_csv, utilisateurs)

# emprunts

def charger_emprunts(fichier_csv):
    try:
        with open(fichier_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [Emprunt(row['user_id'], row['isbn'], row['date_emprunt'], row['date_retour_prevue'], row['retourne'] == 'True') for row in reader]
    except FileNotFoundError:
        return []

def sauvegarder_emprunts(fichier_csv, emprunts):
    with open(fichier_csv, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['user_id', 'isbn', 'date_emprunt', 'date_retour_prevue', 'retourne']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for emprunt in emprunts:
            writer.writerow({
                'user_id': emprunt.user_id,
                'isbn': emprunt.isbn,
                'date_emprunt': emprunt.date_emprunt,
                'date_retour_prevue': emprunt.date_retour_prevue,
                'retourne': emprunt.retourne
            })

def enregistrer_emprunt(fichier_csv, emprunts, user_id, isbn, date_retour_prevue):
    date_emprunt = datetime.today().strftime('%Y-%m-%d')
    emprunt = Emprunt(user_id, isbn, date_emprunt, date_retour_prevue)
    emprunts.append(emprunt)
    sauvegarder_emprunts(fichier_csv, emprunts)

def retourner_livre(fichier_csv, emprunts, isbn):
    for emprunt in emprunts:
        if emprunt.isbn == isbn and not emprunt.retourne:
            emprunt.retourne = True
            break
    sauvegarder_emprunts(fichier_csv, emprunts)

# statistiques

def generer_statistiques(livres, emprunts):
    total_livres = len(livres)
    livres_empruntes = len([e for e in emprunts if not e.retourne])
    return {
        "total_livres": total_livres,
        "livres_empruntes": livres_empruntes,
        "livres_disponibles": total_livres - livres_empruntes
    }


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