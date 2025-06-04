from claude import *

def calculer_nb_lignes(nom_fichier) :
    with open(nom_fichier,"r") as fichier:
        l=fichier.readlines()
    return len(l)

#def import_annee(nom_fichier_source, nom_fichier_destination):
#    res = []
#    n=calculer_nb_lignes("data.csv")
#    with open(nom_fichier_source,"r") as fichier:
#        fichier.readline()
#        for i in range(1, n):
#            temp = fichier.readline().split(',')
#            res.append(temp[3][1:-1])
#    #print(res)
#    with open(nom_fichier_destination, "w") as fichier:
#        for i in range(1,len(res)):
#            fichier.write("INSERT INTO `annee` VALUES ("+res[i]+")\n")

def import_installation(nom_fichier_source, nom_fichier_destination):
    temp = parse_csv_file(nom_fichier_source)
    res = []
    for i in range(1, len(temp)):
        res.append([
            int(temp[i][0]),                                        #id
            ('NULL' if temp[i][4]=='' else int(temp[i][4])),        #nb_panneau
            ('NULL' if temp[i][7]=='' else int(temp[i][7])),        #nb_ondulateur
            ('NULL' if temp[i][10]=='' else int(temp[i][10])),      #puiss_crete
            ('NULL' if temp[i][11]=='' else float(temp[i][11])),    #surface
            ('NULL' if temp[i][12]=='' else int(temp[i][12])),      #pente
            ('NULL' if temp[i][13]=='' else int(temp[i][13])),      #pente opti
            ('NULL' if temp[i][14]=='' else temp[i][14]),           #orientation (varchar)
            ('NULL' if temp[i][15]=='' else temp[i][15]),           #orientation opti (varchar)
            ('NULL' if temp[i][17]=='' else int(temp[i][17])),      #produ pvgis
            float(temp[i][18]),                                     #lat
            float(temp[i][19]),                                     #lon
            ('NULL' if temp[i][6]=='' else temp[i][6]),             #panneau modele
            ('NULL' if temp[i][9]=='' else temp[i][9]),             #ondu modele
            ('NULL' if temp[i][5]=='' else temp[i][5]),             #panneau marque
            ('NULL' if temp[i][8]=='' else temp[i][8]),             #ondu marque
            ('NULL' if temp[i][16]=='' else temp[i][16]),           #installateur
            ('NULL' if temp[i][21]=='' else int(temp[i][21])),      #code insee
            ('NULL' if temp[i][2]=='' else int(temp[i][2])),        #mois
            ('NULL' if temp[i][3]=='' else int(temp[i][3]))         #annee
            ])
    print(res)
    with open(nom_fichier_destination, "w") as fichier:
        for i in range(len(res)):
            fichier.write("INSERT INTO `installation` VALUES ('"+str(res[i][0])+"','"+str(res[i][1])+"','"+str(res[i][2])+"','"+str(res[i][3])+"','"+str(res[i][4])+"','"+str(res[i][5])+"','"+str(res[i][6])+"','"+str(res[i][7])+"','"+str(res[i][8])+"','"+str(res[i][9])+"','"+str(res[i][10])+"','"+str(res[i][11])+"','"+str(res[i][12])+"','"+str(res[i][13])+"','"+str(res[i][14])+"','"+str(res[i][15])+"','"+str(res[i][16])+"','"+str(res[i][17])+"','"+str(res[i][18])+"','"+str(res[i][19])+"')\n")
    return

def import_annee(temp):
    result = ""
    for i in range(len(temp)):
        if not str(temp[i][3]) in result:
            result += "INSERT INTO `annee` VALUES ('" + str(temp[i][3]) + "')\n"

def import_mois(temp):
    result = ""
    for i in range(len(temp)):
        if not str(temp[i][2]) in result:
            result += "INSERT INTO `mois` VALUES ('" + str(temp[i][2]) + "')\n"

def import_localisation(temp):
    result = ""
    for i in range(len(temp)):
        if not str(temp[i][24]) in result:
            result += "INSERT INTO `region` VALUES ('" + str(temp[i][25]) + "')\nINSERT INTO `departement` VALUES ('" + (str(temp[i][21]))[:2]+str(temp[i][26])+str(temp[i][25])+"')\nINSERT INTO `ville` VALUES ('" + str(temp[i][]) + "')\nINSERT INTO `ville` VALUES ('" + str(temp[i][24]) + "')\n"


import_installation("data.csv","sql2")