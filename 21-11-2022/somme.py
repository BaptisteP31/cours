def somme_par_indice_pairs(nombres):
    somme = 0
    for i in range(len(nombres)): # Pour chaque index
        if i%2 == 0: # S'il est pair ...
            somme = somme + nombres[i]

    return somme

list = [1, 2, 3]
print(somme_par_indice_pairs(list))