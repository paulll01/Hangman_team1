from logica import initializeaza_stare_cuvant, actualizeaza_stare_cuvant, este_cuvant_ghicit
from afisare import afiseaza_stare_cuvant, afiseaza_spanzuratoare, afiseaza_litere_incercate
from cuvinte import incarca_cuvinte, alege_cuvant, cere_litera

def joc_spanzuratoarea():
    cuvinte = incarca_cuvinte()
    cuvant = alege_cuvant(cuvinte)
    stare = initializeaza_stare_cuvant(cuvant)
    litere_incercate = set()
    
    greseli = 0
    greseli_maxime = 6

    while greseli < greseli_maxime and not este_cuvant_ghicit(stare):
        print("\033[3J\033[H\033[2J", end="")
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
