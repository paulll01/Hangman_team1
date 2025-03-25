# Aici este fisierul principal unde vom asabla toate modulele si vom rula aplicatia

# Pasul 1 - Introducere cuvinte de ghicit 
# Pasul 2 - Clasificarea cuvintelor pe niveluri de dificultate si numarul de greseli acceptate
# Pasul 2.1 - Extragerea unui cuvant random din lista de cuvinte
# Pasul 3 - Secventiere/afisare grafica a spanzuratorii in functie de numarul de greseli
# Pasul 4 - Citire de la tastatura a literei introduse de jucator
# Pasul 5 - Cautarea in structura a caracterului introdus de jucator si validare literei
# Pasul 6 - Actualizare grafica a spanzuratorii in functie de numarul de greseli
# Pasul 7 - Reluare ciclu daca mai sunt permise incercari
# Pasul 8 - Reluare ciclu daca cuvantul nu a fost ghicit
# Pasul 9 - Crearea unei formule de performanta pentru a fi introdusa intr-un clasament

from logica import initializeaza_stare_cuvant, actualizeaza_stare_cuvant, este_cuvant_ghicit
from afisare import afiseaza_stare_cuvant, afiseaza_spanzuratoare, afiseaza_litere_incercate
from input_util import cere_litera
from cuvinte import incarca_cuvinte, alege_cuvant

def joc_spanzuratoarea():
    cuvinte = incarca_cuvinte()
    cuvant = alege_cuvant(cuvinte)
    stare = initializeaza_stare_cuvant(cuvant)
    litere_incercate = set()
    
    greseli = 0
    greseli_maxime = 6

    while greseli < greseli_maxime and not este_cuvant_ghicit(stare):
        afiseaza_stare_cuvant(stare)
        afiseaza_spanzuratoare(greseli)
        afiseaza_litere_incercate(litere_incercate)

        litera = cere_litera(litere_incercate)
        litere_incercate.add(litera)

        if litera in cuvant:
            actualizeaza_stare_cuvant(cuvant, stare, litera)
        else:
            greseli += 1

    if este_cuvant_ghicit(stare):
        print(f"Felicitări! Ai ghicit cuvântul: {cuvant}")
    else:
        afiseaza_spanzuratoare(greseli)
        print(f"Ai pierdut! Cuvântul era: {cuvant}")

if __name__ == "__main__":
    joc_spanzuratoarea()

cuvinte = incarca_cuvinte() 
# e.g. cuvinte = ['abc', 'bsa', 'casd', 'dasd', 'easd', 'fasd']
