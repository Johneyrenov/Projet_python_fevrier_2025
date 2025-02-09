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
    def __init__(self, user_id, nom,prenom, telephone,adresse,activite,email):
        self.user_id = user_id
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.adresse = adresse
        self.activite = activite
        self.email = email
        self.emprunts = []  
    
    def emprunter(self, emprunt):
        self.emprunts.append(emprunt)
#Methode pour convertir un objet user en dictionaire(pour Stockage CSV)
    def to_dict(self):
        return{
            "user_id" :self.user_id,
            "nom" : self.nom,
            "prenom" : self.prenom,
            "telephone": self.telephone,
            "adresse": self.adresse,
            "activite": self.activite,
            "email": self.email
        }
#class methode
    @classmethod
    def from_dict(cls,data):
        return cls(
            user_id=data["user_id"],
            nom=data["nom"],
            prenom=data["prenom"],
            telephone=data["telephone"],
            adresse=data["adresse"],
            activite=data["activite"],
            email=data["email"]
        )
    def retourner(self, isbn):
        for emprunt in self.emprunts:
            if emprunt.isbn == isbn and not emprunt.retourne:
                emprunt.retourne = True
                break
    
    def __str__(self):
        return f"Utilisateur {self.nom} ({self.user_id}) - telephone : {self.telephone} - adresse : {self.adresse} - activite : {self.activite} - email {self.adresse}"

class Emprunt:
    def __init__(self, user_id, isbn, date_emprunt, date_retour_prevue,retourne=False):
        self.user_id = user_id
        self.isbn = isbn
        self.date_emprunt = date_emprunt
        self.date_retour_prevue = date_retour_prevue
        self.retourne = retourne  # Par défaut, le livre n'est pas retourné

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "isbn": self.isbn,
            "date_emprunt": self.date_emprunt.strftime('%d/%m/%Y'),
            "date_retour_prevue": self.date_retour_prevue.strftime('%d/%m/%Y'),
            "retourne": str(self.retourne)
        }
        
    @classmethod
    def from_dict(cls, data):
        date_emprunt = datetime.strptime(data["date_emprunt"], '%d/%m/%Y')
        date_retour_prevue = datetime.strptime(data["date_retour_prevue"], '%d/%m/%Y')
        retourne = data["retourne"].lower() == "true"  # Convertir en booléen
        return cls(
            user_id=data["user_id"],
            isbn=data["isbn"],
            date_emprunt=date_emprunt,
            date_retour_prevue=date_retour_prevue,
            retourne=retourne
        )
#class methode pour creer un objet emprunt a partir d'un dict(CSV loading)
    @classmethod
    def from_dict(cls,data):
        return cls(
            user_id=data["user_id"],
            isbn=data["isbn"],
            date_emprunt=datetime.strptime(data["date_emprunt"], "%d/%m/%Y"),
            date_retour_prevue=datetime.strptime(data["date_retour_prevue"], "%d/%m/%Y"),
            retourne=data["retourne"]
            
        )