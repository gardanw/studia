def find_seeds(i,j):
    seed = dict()
    for ite in i:
        if ite in j:
            for k in range(len(i[ite])):
                for l in range(len(j[ite])):
                    if i[ite][k]-j[ite][l] not in seed:
                        seed[i[ite][k]-j[ite][l]] = [(i[ite][k], j[ite][l])]
                    else:
                        seed[i[ite][k]-j[ite][l]].append((i[ite][k], j[ite][l]))
    return seed

def find_match(seeds):
    matchs = dict()
    for i in seeds:
        lista_krotek = sorted(seeds[i])
        match = [lista_krotek[0][0], lista_krotek[0][1], 3]
        for j in range(len(lista_krotek)-1):
            dlugosc = lista_krotek[j+1][0] - lista_krotek[j][0]
            if dlugosc < 9:
                match[2] += dlugosc
            else:
                match = [lista_krotek[j+1][0], lista_krotek[j+1][1], 3]
                if i not in matchs:
                    matchs[i] = [match]
                else:
                    matchs[i].append(match)
    return matchs

plik = open("sekwencje.fasta")
sequences = list()
pom = list()
for i in plik:
    if i[0] == '>':
        pom.append(i[2:7])
    elif len(i) != 1 and i[0] != '>':
        pom.append(i[:len(i)-1])
        sequences.append(tuple(pom))
        pom = list()    

tuples_list = list()
tuples_map = list()
for i in sequences:
    pom = list()
    for j in range(0,len(i[1])-2):
       pom.append(i[1][j:j+3])
    tuples_list.append(pom)

for i in range(len(tuples_list)):
    pom_tuple = dict()
    for j in range(len(tuples_list[i])):
        if tuples_list[i][j] not in pom_tuple:
            pom_tuple[tuples_list[i][j]] = [j]
        else:
            pom_tuple[tuples_list[i][j]].append(j)
    tuples_map.append(pom_tuple)
    
seeds = find_seeds(tuples_map[1221], tuples_map[1222])
print(find_match(seeds))