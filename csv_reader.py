
import unittest
import tempfile
import os

from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)


class TestCsv(unittest.TestCase):

    # Creer un fichier temporaire pour chaque test
    def creer_fichier(self, contenu):

        fichier = tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False
        )

        fichier.write(contenu)
        fichier.close()

        self.addCleanup(os.remove, fichier.name)

        return fichier.name

    # Test 1 : CSV valide
    def test_csv_valide(self):

        chemin = self.creer_fichier(
            "1;Ordinateur;750.50\n"
            "2;Clavier;45.90\n"
            "3;Souris;20.00\n"
        )

        articles = charger_csv(chemin)

        self.assertEqual(len(articles), 3)
        self.assertEqual(articles[0]["nom"], "Ordinateur")
        self.assertEqual(articles[0]["prix"], 750.50)

    # Test 2 : fichier absent
    def test_fichier_absent(self):

        with self.assertRaises(FichierIntrouvableException):
            charger_csv("fichier_inexistant.csv")

    # Test 3 : prix texte
    def test_prix_texte(self):

        chemin = self.creer_fichier(
            "1;Ordinateur;abc\n"
        )

        with self.assertRaises(LigneInvalideException):
            charger_csv(chemin)

    # Test 4 : prix negatif
    def test_prix_negatif(self):

        chemin = self.creer_fichier(
            "1;Ordinateur;-50\n"
        )

        with self.assertRaises(PrixNegatifException):
            charger_csv(chemin)

    # Test 5 : nombre de colonnes incorrect
    def test_colonnes_invalides(self):

        chemin = self.creer_fichier(
            "1;Ordinateur\n"
        )

        with self.assertRaises(LigneInvalideException):
            charger_csv(chemin)

    # Test 6 : ligne vide
    def test_ligne_vide(self):

        chemin = self.creer_fichier(
            "1;Ordinateur;750\n"
            "\n"
            "2;Clavier;45\n"
        )

        articles = charger_csv(chemin)

        self.assertEqual(len(articles), 2)


if __name__ == "__main__":
    unittest.main()
