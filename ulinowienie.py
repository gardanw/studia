def find_seeds(i,j):
    keys = i.keys()
    seed = {}
    for ite in keys:
        if ite in j:
            for k in range(len(i[ite])):
                for l in range(len(j[ite])):
                    if i[ite][k]-j[ite][l] not in seed:
                        seed[i[ite][k]-j[ite][l]] = [(i[ite][k], j[ite][l])]
                    else:
                        seed[i[ite][k]-j[ite][l]].append((i[ite][k], j[ite][l]))
    return seed


plik = open("sekwencje.fasta")
sequences = []
pom = []
for i in plik:
#    print(len(i))
    if i[0] == '>':
        pom.append(i[2:7])
    elif len(i) != 1 and i[0] != '>':
        pom.append(i[:len(i)-1])
        sequences.append(tuple(pom))
        pom = []    
#print(sequences)
#sequences = [("3w12B","CGSHLVEALYLVCGE"), ("2czyB", "APQLIMLANVALTGE")]
tuples_list = []
tuples_map = []
for i in sequences:
    pom = []
    for j in range(0,len(i[1])-2):
       pom.append(i[1][j:j+3])
    tuples_list.append(pom)
#print(tuples_list)
for i in range(len(tuples_list)):
    pom_tuple = {}
    for j in range(len(tuples_list[i])):
        if tuples_list[i][j] not in pom_tuple:
            pom_tuple[tuples_list[i][j]] = [j]
        else:
            pom_tuple[tuples_list[i][j]].append(j)
    tuples_map.append(pom_tuple)
#print(tuples_map)
for i in range(len(tuples_map)):
    for j in range(i, len(tuples_map)):
        if i != j:
            print(find_seeds(tuples_map[i], tuples_map[j]))