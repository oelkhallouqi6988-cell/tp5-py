
import logging

# Configuration du logger
logging.basicConfig(
    filename="reservations.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# 1. Exception principale
class ReservationException(Exception):
    def __init__(self, message):
        super().__init__(message)


# 2. Exceptions personnalisees
class CapaciteDepasseeException(ReservationException):
    pass


class NombreInvalideException(ReservationException):
    pass


class NomClientInvalideException(ReservationException):
    pass


# 3. Classe Evenement
class Evenement:

    def __init__(self, nom, capacite):
        if not isinstance(capacite, int) or isinstance(capacite, bool) or capacite <= 0:
            raise NombreInvalideException(
                "La capacite doit etre un entier positif."
            )

        if not isinstance(nom, str) or not nom.strip():
            raise ValueError("Le nom de l'evenement est obligatoire.")

        self.nom = nom
        self.capacite = capacite
        self.places_reservees = 0

    # Methode de reservation
    def reserver(self, nom_client, nb_places):

        try:
            # Verifier le nom du client
            if not isinstance(nom_client, str) or not nom_client.strip():
                raise NomClientInvalideException(
                    "Nom du client requis."
                )

            # Verifier le nombre de places
            if not isinstance(nb_places, int) or isinstance(nb_places, bool) or nb_places <= 0:
                raise NombreInvalideException(
                    "Nombre de places invalide."
                )

            # Verifier la capacite
            if self.places_reservees + nb_places > self.capacite:
                raise CapaciteDepasseeException(
                    "Capacite depassee."
                )

            # Confirmer la reservation
            self.places_reservees += nb_places

            message = (
                f"Reservation confirmee pour {nom_client} "
                f"({nb_places} places)."
            )

            print(message)
            logging.info(message)

        except ReservationException as e:
            logging.error(
                f"Echec reservation pour {nom_client!r} : {e}"
            )
            raise

    # Afficher les informations
    def afficher(self):
        print(
            f"Evenement : {self.nom} | "
            f"{self.places_reservees}/{self.capacite} "
            f"places reservees"
        )


# 4. Programme principal
try:
    event = Evenement("Concert", 5)

    event.reserver("Alice", 2)
    event.afficher()

    event.reserver("Ahmed", 2)
    event.afficher()

    event.reserver("Sara", 3)

except ReservationException as e:
    print("Erreur :", e)

print("\nFin du programme.")
