def calculer_nb_lignes(nom_fichier) :
    with open(nom_fichier,"r") as fichier:
        l=fichier.readlines()
    return len(l)

def recopier_fichier(nom_fichier_source, nom_fichier_destination):
    res = []
    n=calculer_nb_lignes("data.csv")
    with open(nom_fichier_source,"r") as fichier:
        fichier.readline()
        for i in range(1, n):
            temp = fichier.readline().split(',')
            res.append(temp[3][1:-1])
    #print(res)
    with open(nom_fichier_destination, "w") as fichier:
        for i in range(1,len(res)):
            fichier.write("INSERT INTO `annee` VALUES ("+res[i]+")\n")

def recopier_fichier_installation(nom_fichier_source, nom_fichier_destination):
    res = []
    n=calculer_nb_lignes("data.csv")
    with open(nom_fichier_source,"r") as fichier:
        fichier.readline()
        for i in range(1, n):
            temp = fichier.readline().split(',')
            res.append((temp[0][1:-1],temp[4][1:-1],temp[7][1:-1],temp[10][1:-1],
                        temp[11][1:-1],temp[12][1:-1],temp[13][1:-1],temp[14][1:-1],
                        temp[15][1:-1],temp[17][1:-1],temp[18][1:-1],temp[19][1:-1],temp[6][1:-1],
                        temp[9][1:-1],temp[5][1:-1],temp[8][1:-1],temp[16][1:-1],temp[21][1:-1]
                        ,temp[2][1:-1],temp[3][1:-1]))
    #print(res)
    with open(nom_fichier_destination, "w") as fichier:

        recopier_fichier("data.csv","sql")

        recopier_fichier_installation("data.csv","sql2")

#INSERT INTO