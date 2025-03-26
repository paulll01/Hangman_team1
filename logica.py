# Ionut
def initializeaza_stare_cuvant(cuvant_de_ghicit):

    stare_cuvant = ['_'] * len(cuvant_de_ghicit)

    return stare_cuvant

#va returna noua stare stare  = ['a', '_', '_', '_', '_', '_']
def actualizeaza_stare_cuvant(cuvant, stare, litera):

    for i,l  in enumerate(cuvant):

        if l == litera:

            stare[i] = litera

    return stare

def este_cuvant_ghicit(stare):

    return '_' not in stare
