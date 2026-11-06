
# Exception personnalisee
class SoldeInsuffisantException(Exception):
    def __init__(self, message):
        super().__init__(message)


# Exception pour les montants negatifs ou nuls
class MontantInvalideException(Exception):
    def __init__(self, message):
        super().__init__(message)


# Classe CompteBancaire
class CompteBancaire:

    def __init__(self, nom, solde=0):
        if solde < 0:
            raise MontantInvalideException(
                "Le solde initial ne peut pas etre negatif."
            )

        self.nom = nom
        self.solde = solde

    # Deposer de l'argent
    def deposer(self, montant):
        if montant <= 0:
            raise MontantInvalideException(
                "Le montant du depot doit etre positif."
            )

        self.solde += montant
        print("Depot effectue avec succes.")

    # Retirer de l'argent
    def retirer(self, montant):
        if montant <= 0:
            raise MontantInvalideException(
                "Le montant du retrait doit etre positif."
            )

        if montant > self.solde:
            raise SoldeInsuffisantException(
                "Solde insuffisant pour ce retrait."
            )

        self.solde -= montant
        print("Retrait effectue avec succes.")

    # Afficher le compte
    def afficher(self):
        print(f"Compte : {self.nom}, Solde : {self.solde} €")


# Programme principal
try:
    compte = CompteBancaire("Alice", 100)

    compte.afficher()

    compte.deposer(50)
    compte.afficher()

    compte.retirer(30)
    compte.afficher()

    compte.retirer(200)

except SoldeInsuffisantException as e:
    print("Erreur :", e)

except MontantInvalideException as e:
    print("Erreur :", e)
