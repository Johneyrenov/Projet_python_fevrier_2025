from datetime import datetime,timedelta
#class representant un livre dans la biblio
class Livre:
    def __init__(self, isbn, titre, auteur, genre, disponible=True):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.genre = genre
        self.disponible = disponible  
    
    def __str__(self):
        return f"{self.titre} de {self.auteur} ({self.genre}) - ISBN: {self.isbn} - {'Disponible' if self.disponible else 'Emprunter'}"
#Methode pour convertir objet livre en dict pour CSV Stockage
     # Méthode pour convertir un objet Livre en dictionnaire
    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titre": self.titre,
            "auteur": self.auteur,
            "genre": self.genre,
            "disponible": self.disponible
        }
        
#Class methode pour creer un objet livre a partir d'un dict(CSV loading)
    @classmethod
    def from_dict(cls,data):
        return cls(
            isbn=data["isbn"],
            titre=data["titre"],
            auteur=data["auteur"],
            genre=data["genre"],
            disponible=data["disponible"]
        )
#class representant un utilisateur de la biblio
class Utilisateur:
    def __init__(self, user_id, nom, contact):
        self.user_id = user_id
        self.nom = nom
        self.contact = contact
        self.emprunts = []  
    
    def emprunter(self, emprunt):
        self.emprunts.append(emprunt)
#Methode pour convertir un objet user en dictionaire(pour Stockage CSV)
    def to_dict(self):
        return{
            "user_id" :self.user_id,
            "nom" : self.nom,
            "contact": self.contact
        }
#class methode
    @classmethod
    def from_dict(cls,data):
        return cls(
            user_id=data["user_id"],
            nom=data["nom"],
            contact=data["contact"]
        )
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
 #methode pour convertir objet emprunt en dictionaire pour stockage CSV
    def to_dict(self):
        return{
            "user_id": self.user_id,
            "isbn": self.isbn,
            "date_emprunt": self.date_emprunt.strftime("%Y-%m-%d"),
            "date_retour_prevue": self.date_retour_prevue.strftime("%Y-%m-%d"),
            "retourne" : self.retourne
          
        }
#class methode pour creer un objet emprunt a partir d'un dict(CSV loading)
    @classmethod
    def from_dict(cls,data):
        return cls(
            user_id=data["user_id"],
            isbn=data["isbn"],
            date_emprunt=datetime.strptime(data["date_emprunt"], "%Y-%m-%d"),
            date_retour_prevue=datetime.strptime(data["date_retour_prevue"], "%Y-%m-%d"),
            retourne=data["retourne"]
            
        )