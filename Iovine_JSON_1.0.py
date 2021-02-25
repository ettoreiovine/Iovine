# Frankenstein, Il piccolo principe, L'isola del tesoro, La fattoria degli animali,
# I viaggi di Gulliver, Se questo è un uomo, Piccole donne, L'amico ritrovato,
# Pinocchio, Orgoglio e pregiudizio
import json
libri = [
            {
            "titolo": "Frankenstein",
            "autore": "Mary Shelley",
            "genere": "Horror",
            "anno_di_pubblicazione": 1823,
            "lingua_originale": "Inglese"
            },
            {
            "titolo": "Il piccolo principe",
            "autore": "Antoine de Saint-Exupéry",
            "genere": "Favola",
            "anno_di_pubblicazione": 1943,
            "lingua_originale": "Francese"
            },
            {
            "titolo": "L'isola del tesoro",
            "autore": "Robert Louis Stevenson",
            "genere": "Romanzo",
            "anno_di_pubblicazione": 1883,
            "lingua_originale": "Inglese"
            },
            {
            "titolo": "La fattoria degli animali",
            "autore": "George Orwell",
            "genere": "Allegoria",
            "anno_di_pubblicazione": 1945,
            "lingua_originale": "Inglese"
            },
            {
            "titolo": "I viaggi di Gulliver",
            "autore": "Jonathan Swift",
            "genere": "Satira",
            "anno_di_pubblicazione": 1726,
            "lingua_originale": "Inglese"
            },
            {
            "titolo": "Se questo è un uomo",
            "autore": "Primo Levi",
            "genere": "Biografia",
            "anno_di_pubblicazione": 1947,
            "lingua_originale": "Italiano"
            },
            {
            "titolo": "Piccole donne",
            "autore": "Louisa May Alcott",
            "genere": "Romanzo",
            "anno_di_pubblicazione": 1868,
            "lingua_originale": "Inglese"
            },
            {
            "titolo": "L'amico ritrovato",
            "autore": "Fred Uhlman",
            "genere": "Dramma",
            "anno_di_pubblicazione": 1971,
            "lingua_originale": "Inglese"
            },
            {
            "titolo": "Pinocchio",
            "autore": "Carlo Collodi",
            "genere": "Romanzo",
            "anno_di_pubblicazione": 1883,
            "lingua_originale": "Italiano"
            },
            {
            "titolo": "Orgoglio e pregiudizio",
            "autore": "Jane Austen",
            "genere": "Romanzo",
            "anno_di_pubblicazione": 1813,
            "lingua_originale": "Inglese"
            }
        ]

with open("libri.json", "w") as f:
    json.dump(libri, f)

f.close()

with open("libri.json", "r") as f:
    dati_da_file = json.load(f)

f.close()

print("Stampa il file intero: ", dati_da_file)
            
