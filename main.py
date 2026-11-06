
from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException,
    CsvException
)


def main():

    chemin = "articles.csv"

    try:
        articles = charger_csv(chemin)

        print("Import CSV reussi !")
        print("\nListe des articles :")

        for article in articles:
            print(article)

    except FichierIntrouvableException as e:
        print("Erreur fichier :", e)

    except LigneInvalideException as e:
        print("Erreur format :", e)

    except PrixNegatifException as e:
        print("Erreur prix :", e)

    except CsvException as e:
        print("Erreur CSV :", e)


if __name__ == "__main__":
    main()
