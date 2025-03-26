# Florin

#  returneaza _ _ _ a _ _ _
def afiseaza_stare_cuvant(stare):
    for element in stare:
        print(element, end=' ')
    print("")

# de afisat spanzuratoarea
def afiseaza_spanzuratoare(greseli):
    if greseli == 0:
        print('''
    +---+
    |   |
        |
        |
        |
        |
        |  0/6 vieti consumate
  ==========\n''')
    elif greseli == 1:
        print('''
    +---+
    |   |
    O   |
        |
        |
        |
        |  1/6 vieti consumate
  ==========\n''')
    elif greseli == 2:
        print('''
    +---+
    |   |
    O   |
    |   |
        |
        |
        |  2/6 vieti consumate
  ==========\n''')
    elif greseli == 3:
        print('''
    +---+
    |   |
    O   |
   /|   |
        |
        |
        |  3/6 vieti consumate
  ==========\n''')
    elif greseli == 4:
        print('''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
        |  4/6 vieti consumate
  ==========\n''')
    elif greseli == 5:
        print('''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
        |  5/6 vieti consumate
  ==========\n''')
    else:
        print('''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
        |  6/6 vieti consumate, ESTI SPANZURAT!!!!!
  ==========\n''')

# de afisat setul
def afiseaza_litere_incercate(litere_incercate):
    print("\nLiterele incercate sunt:",end=' ')
    for element in litere_incercate:
        print(element, end=' ')
    print("")

#afiseaza_spanzuratoare(78)
#stare = ['_', '_', '_', '_', '_', '_']
#afiseaza_stare_cuvant(stare)
#litere_incercate = {'e','j','y','g'}
#afiseaza_litere_incercate(litere_incercate)
