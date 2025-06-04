from claude import *

def calculer_nb_lignes(nom_fichier) :
    with open(nom_fichier,"r") as fichier:
        l=fichier.readlines()
    return len(l)

<<<<<<< Updated upstream
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
=======
def associe_INSEE(communes: list, ville, code_postal):
    for i in range(len(communes)):
        if (communes[i][6] == code_postal and communes[i][1] == ville):
            #print(f"Trouvé")
            return communes[i][0]
    #print(f"Code Insee non trouvé pour : {ville} - {code_postal}")
    return f"p{code_postal}" # Renvoie un code insee de format "p" + Code_postal pour tout de même stocker l'information postale



# ------------------------------- IMPORTS -----------------------------------------------
"""
Toutes les fonctions commençant par 'import' - sauf pour 'mois' étant donnée la facilité du peuplement de cette dernière -
prennent en argument une liste de liste correspondant au fichier csv parsé et un nom de fichier d'écriture intitulé 'fichier_destination', 
écrivent à la fin du fichier destination les requêtes sql nécessaires pour peupler la database, à savoir uniquement des INSERT
et ne renvoient rien.
"""

def import_installation(data: list, communes: list, fichier_destination = "import_installation.sql"):
    res = [] # Liste résultat
    unique = [] # liste qui va contenir la liste de toutes les infos d'une ligne
    for i in range(1, len(data)): # On démarre à 1 pour ne pas avoir l'en-tête
        insee = associe_INSEE(communes, data[i][24], data[i][21])   # respectivement la localité et le code postal
        temp = [
            int(data[i][0]),                                        # id (not NULL)
            ('NULL' if data[i][4]=='' else int(data[i][4])),        # nb_panneau
            ('NULL' if data[i][7]=='' else int(data[i][7])),        # nb_ondulateur
            ('NULL' if data[i][10]=='' else int(data[i][10])),      # puissance_crete
            ('NULL' if data[i][11]=='' else float(data[i][11])),    # surface
            ('NULL' if data[i][12]=='' else int(data[i][12])),      # pente
            ('NULL' if data[i][13]=='' else int(data[i][13])),      # pente_optimum
            ('NULL' if data[i][14]=='' else data[i][14]),           # orientation (varchar)
            ('NULL' if data[i][15]=='' else data[i][15]),           # orientation_optimum (varchar)
            ('NULL' if data[i][17]=='' else int(data[i][17])),      # production_pvgis
            float(data[i][18]),                                     # lat (not NULL)
            float(data[i][19]),                                     # lon (not NULL)
            ('NULL' if data[i][6]=='' else data[i][6]),             # modele_panneau
            ('NULL' if data[i][9]=='' else data[i][9]),             # modele_ondulateur
            ('NULL' if data[i][16]=='' else data[i][16]),           # nom_installateur
            ('NULL' if data[i][21]=='' else insee),                 # code insee
            ('NULL' if data[i][2]=='' else int(data[i][2])),        # num_mois
            ('NULL' if data[i][3]=='' else int(data[i][3]))         # num_annee
        ]
        if not(temp[1:] in unique): # On vérifie si les données privées de l'id sont les mêmes pour ne pas ajouter les doublons
            res.append(temp) # On ajoute dans la liste avec l'id
            unique.append(temp[1:]) # On ajoute sans l'id car, lui, diffère toujours et ne nous permet pas de trier les doublons
    print(unique)
    with open(fichier_destination, "w") as fichier:
        fichier.write("-- _______________________ Installations __________________________")
        line = ""
        for i in range(len(res)):
            line = f"INSERT INTO `installation` VALUES ({res[i][0]}, {res[i][1]}, {res[i][2]}, {res[i][3]}, {res[i][4]}, {res[i][5]}, {res[i][6]}, `{res[i][7]}`, `{res[i][8]}`, {res[i][9]}, {res[i][10]}, {res[i][11]}, `{res[i][12]}`, `{res[i][13]}`, `{res[i][14]}`, `{res[i][15]}`, {res[i][16]}, {res[i][17]})\n"
            fichier.write(line)

# --------------------------- Premier import ------------------------

def import_annee(liste: list, fichier_destination = "sql/import_annee.sql"):    
    with open(fichier_destination, "w") as fichier:
        fichier.write("-- _______________________ Annees __________________________")
        line = ""
        done = []
        for i in range(1, len(liste)):
            print(liste[i][3], (liste[i][3] in done))
            if not(liste[i][3] in done): # liste[i][3] est l'annee de l'installation
                line = f"INSERT INTO `annee` VALUES ('{liste[i][3]}')\n"
                fichier.write(line)
                done.append(liste[i][3])
>>>>>>> Stashed changes

def import_localisation(temp):
    result = ""
    for i in range(len(temp)):
        if not str(temp[i][24]) in result:
            result += "INSERT INTO `region` VALUES ('" + str(temp[i][25]) + "')\nINSERT INTO `departement` VALUES ('" + (str(temp[i][21]))[:2]+str(temp[i][26])+str(temp[i][25])+"')\nINSERT INTO `ville` VALUES ('" + str(temp[i][]) + "')\nINSERT INTO `ville` VALUES ('" + str(temp[i][24]) + "')\n"

<<<<<<< Updated upstream
import_installation("data.csv","sql2")
=======
def import_mois(fichier_destination = "sql/import_mois.sql"):
    with open(fichier_destination, "a") as fichier:
        fichier.write("-- _______________________ Mois __________________________")
        line = ""
        for i in range(12):
            line = f"INSERT INTO `mois` VALUES ('{i+1}')\n"
            fichier.write(line)


# ------------------------------- Main --------------------------------------------------

def premierImport(liste: list, communes: list, fichier_destination = "sql/premierImport.sql"):
    import_annee(fichier_destination)
    import_mois(fichier_destination)

def main():
    liste = parse_csv("dataRessources/cleanData.csv")
    communes = parse_csv("dataRessources/communes-france-2024-limite.csv")
    #import_mois("import_mois.sql")
    #import_annee(liste, "import_annee.sql")
    import_installation(liste, communes, "sql/import_installation.sql")

main()
>>>>>>> Stashed changes
