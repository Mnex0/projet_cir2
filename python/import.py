import csv

def parse_csv(file_path):
    liste = []
    try:
        with open(file_path, 'r', encoding='utf-8', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                liste.append(row)
        return liste

    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} n'a pas été trouvé.")
        return []
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return []

def calculer_nb_lignes(nom_fichier) :
    with open(nom_fichier,"r") as fichier:
        l=fichier.readlines()
    return len(l)

def associe_INSEE(communes: list, ville, code_postal):
    for i in range(len(communes)):
        if (communes[i][6] == code_postal and communes[i][1] == ville):
            print(f"Trouvé")
            return communes[i][0]
    print(f"Code Insee non trouvé pour : {ville} - {code_postal}")
    return f"p{code_postal}" # Renvoie un code insee de format "p" + Code_postal pour tout de même stocker l'information postale

"""
Toutes les fonctions commençant par 'import' - sauf pour 'mois' étant donnée la facilité du peuplement de cette dernière -
prennent en argument une liste de liste correspondant au fichier csv parsé et un nom de fichier d'écriture intitulé 'fichier_destination', 
écrivent à la fin du fichier destination les requêtes sql nécessaires pour peupler la database, à savoir uniquement des INSERT
et ne renvoient rien.
"""

# ------------------------------- IMPORTS -----------------------------------------------

def import_installation(data: list, communes: list, fichier_destination = "import_installation.sql"):
    res = [] # Liste résultat
    unique = [] # liste qui va contenir un tuple de toutes les infos d'une ligne sauf l'id
    for i in range(1, len(data)): # On démarre à un pour ne pas avoir l'en-tête
        insee = associe_INSEE(communes, data[i][24], data[i][21])   # respectivement la localité et le code postal
        temp = (
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
        )
        if not(temp in unique): # On vérifie si les données privées de l'id sont les mêmes pour ne pas ajouter les doublons
            res.append([int(data[i][0]), temp]) # On ajoute dans la liste avec l'id en plus. Ex : [[id, TUPLE(données)], ...]
            unique.append(temp)
    print(unique)
    with open(fichier_destination, "w") as fichier:
        line = ""
        for i in range(len(res)):
            line = f"INSERT INTO `installation` VALUES ('{res[i][0]}, {res[i][1][1]}')\n"
            fichier.write(line)
            fichier.write("INSERT INTO `installation` VALUES ('"+str(res[i][0])+"','"+str(res[i][1])+"','"+str(res[i][2])+"','"+str(res[i][3])+"','"+str(res[i][4])+"','"+str(res[i][5])+"','"+str(res[i][6])+"','"+str(res[i][7])+"','"+str(res[i][8])+"','"+str(res[i][9])+"','"+str(res[i][10])+"','"+str(res[i][11])+"','"+str(res[i][12])+"','"+str(res[i][13])+"','"+str(res[i][14])+"','"+str(res[i][15])+"','"+str(res[i][16])+"','"+str(res[i][17])+"','"+str(res[i][18])+"','"+str(res[i][19])+"')\n")
    return


def import_annee(liste: list, fichier_destination = "import_annee.sql"):    
    with open(fichier_destination, "w") as fichier:
        line = ""
        done = []
        for i in range(1, len(liste)):
            print(liste[i][3], (liste[i][3] in done))
            if not(liste[i][3] in done): # liste[i][3] est l'annee de l'installation
                line = f"INSERT INTO `annee` VALUES ('{liste[i][3]}')\n"
                fichier.write(line)
                done.append(liste[i][3])


def import_mois(fichier_destination = "import_mois.sql"):
    with open(fichier_destination, "a") as fichier:
        line = ""
        for i in range(12):
            line = f"INSERT INTO `mois` VALUES ('{i+1}')\n"
            fichier.write(line)

"""def import_localisation(liste, fichier_destination):
    line = ""
    for i in range(len(liste)):
        if not str(liste[i][24]) in result:
            line = "INSERT INTO `region` VALUES ('" + str(liste[i][25]) + "')\nINSERT INTO `departement` VALUES ('" + (str(liste[i][21]))[:2]+str(liste[i][26])+str(liste[i][25])+"')\nINSERT INTO `ville` VALUES ('" + str(liste[i][]) + "')\nINSERT INTO `ville` VALUES ('" + str(liste[i][24]) + "')\n"

"""


# ------------------------------- Main --------------------------------------------------

def main():
    liste = parse_csv("dataRessources/cleanData.csv")
    communes = parse_csv("dataRessources/communes-france-2024-limite.csv")
    #import_mois("import_mois.sql")
    #import_annee(liste, "import_annee.sql")
    import_installation(liste, communes, "import_installation.sql")

main()