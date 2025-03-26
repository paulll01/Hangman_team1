# Daniel

import random
# aici incarcam o lista de c=uvinte din fisier din .txt -> Majuscule/fara diacritice
def incarca_cuvinte():
    cuvinte = ["casă","masă","telefon","floare","pădure","copil","caiet","calculator","mere",
    "chitară","portocală","creion","joc","coleg","fereastră","pahar","prieten","examen","bunic",
    "carte","drum","lac","munte","teatru","tren","cântec","umbră","călătorie","lacrimă","răsărit",
    "sat","mâncare","bucurie","amintire","căldură","lumină","ploaie","zâmbet","câine","pisică",
    "păsăre","pește","vultur","leu","tigru","urs","elefant","zebră","girafă","cangur","vulpe","lup"]
    return cuvinte
# pentru functionalitate am definit mai intai hard-coded lista de cuvinte
# si pentru a primi o revizie a fisierului :) 

# trimitem lista de cuvinte si cu random returneaza un cuvant random
def alege_cuvant(cuvinte):
    return random.choice(cuvinte).upper()

# Cerem o litera de la tastatura
def cere_litera(litere_incercate):
    
    # print("Litere incercate:",litere_incercate)
    
    litera = input("Introduceti o litera: ").strip().upper()
    
    # Verifica daca input-ul este gol
    if not litera:
        print("Nu ati introdus nimic. incercati din nou.")
        return cere_litera(litere_incercate)
    
    # Verifica daca a fost introdus un singur caracter
    if len(litera) != 1:
        print("Introduceti o singura litera!")
        return cere_litera(litere_incercate)
    
    # Verifica daca caracterul este o litera
    if not litera.isalpha():
        print("Introduceti doar litere!")
        return cere_litera(litere_incercate)
    
    # Verifica daca litera a fost deja incercata
    if litera.upper() in litere_incercate:
        print("Litera a fost deja incercata!")
        return cere_litera(litere_incercate)
    
    # litere_incercate.append(litera)
    # print(litere_incercate)
    return litera.upper()

# Test
# print(alege_cuvant(incarca_cuvinte()))
# # litere_incercate = ["A","E","I"] # lista
# print("Litere incercate(inainte):",litere_incercate)
# print(cere_litera(litere_incercate))
# print("Litere incercate(dupa):",litere_incercate)