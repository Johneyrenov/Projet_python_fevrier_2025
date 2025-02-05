class Livre:
    def __init__(self, isbn, titre, auteur, genre, disponible=True):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.genre = genre
        self.disponible = disponible  
    
    def __str__(self):
        return f"{self.titre} de {self.auteur} ({self.genre}) - ISBN: {self.isbn} - {'Disponible' if self.disponible else 'Emprunter'}"

class Utilisateur:
    def __init__(self, user_id, nom, contact):
        self.user_id = user_id
        self.nom = nom
        self.contact = contact
        self.emprunts = []  
    
    def emprunter(self, emprunt):
        self.emprunts.append(emprunt)
    
    def retourner(self, isbn):
        for emprunt in self.emprunts:
            if emprunt.isbn == isbn and not emprunt.retourne:
                emprunt.retourne = True
                break
    
    def __str__(self):
        return f"Utilisateur {self.nom} ({self.user_id}) - Contact : {self.contact}"

class Emprunt:
    def __init__(self, user_id, isbn, date_emprunt, date_retour_prevue, retourne=False):
        self.user_id = user_id
        self.isbn = isbn
        self.date_emprunt = date_emprunt
        self.date_retour_prevue = date_retour_prevue
        self.retourne = retourne  
    
    def __str__(self):
        return f"Emprunt de {self.isbn} par {self.user_id} - Date d'emprunt: {self.date_emprunt} - Retour prevu le: {self.date_retour_prevue} - {'Retourner' if self.retourne else 'Non retourner'}"
