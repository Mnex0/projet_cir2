import csv
from io import StringIO

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

"""
Toutes les fonctions commençant par 'import' - sauf pour 'mois' étant donnée la facilité du peuplement de cette dernière -
prennent en argument une liste de liste correspondant au fichier csv parsé et un nom de fichier d'écriture intitulé 'fichier_destination', 
écrivent à la fin du fichier destination les requêtes sql nécessaires pour peupler la database, à savoir uniquement des INSERT
et ne renvoient rien.
"""

# ------------------------------- IMPORTS -----------------------------------------------

def import_installation(liste, fichier_destination):
    res = []
    for i in range(1, len(liste)):
        res.append([
            int(liste[i][0]),                                         # id (not NULL)
            ('NULL' if liste[i][4]=='' else int(liste[i][4])),        # nb_panneau
            ('NULL' if liste[i][7]=='' else int(liste[i][7])),        # nb_ondulateur
            ('NULL' if liste[i][10]=='' else int(liste[i][10])),      # puissance_crete
            ('NULL' if liste[i][11]=='' else float(liste[i][11])),    # surface
            ('NULL' if liste[i][12]=='' else int(liste[i][12])),      # pente
            ('NULL' if liste[i][13]=='' else int(liste[i][13])),      # pente_optimum
            ('NULL' if liste[i][14]=='' else liste[i][14]),           # orientation (varchar)
            ('NULL' if liste[i][15]=='' else liste[i][15]),           # orientation_optimum (varchar)
            ('NULL' if liste[i][17]=='' else int(liste[i][17])),      # production_pvgis
            float(liste[i][18]),                                      # lat (not NULL)
            float(liste[i][19]),                                      # lon (not NULL)
            ('NULL' if liste[i][6]=='' else liste[i][6]),             # modele_panneau
            ('NULL' if liste[i][9]=='' else liste[i][9]),             # modele_ondulateur
            ('NULL' if liste[i][16]=='' else liste[i][16]),           # nom_installateur
            ('NULL' if liste[i][21]=='' else int(liste[i][21])),      # code insee
            ('NULL' if liste[i][2]=='' else int(liste[i][2])),        # num_mois
            ('NULL' if liste[i][3]=='' else int(liste[i][3]))         # num_annee
            ])
    print(res)
    with open(fichier_destination, "a") as fichier:
        line = ""
        for i in range(len(res)):
            line = f"INSERT INTO `installation` VALUES ('{res[i][0]}')\n"
            fichier.write("INSERT INTO `installation` VALUES ('"+str(res[i][0])+"','"+str(res[i][1])+"','"+str(res[i][2])+"','"+str(res[i][3])+"','"+str(res[i][4])+"','"+str(res[i][5])+"','"+str(res[i][6])+"','"+str(res[i][7])+"','"+str(res[i][8])+"','"+str(res[i][9])+"','"+str(res[i][10])+"','"+str(res[i][11])+"','"+str(res[i][12])+"','"+str(res[i][13])+"','"+str(res[i][14])+"','"+str(res[i][15])+"','"+str(res[i][16])+"','"+str(res[i][17])+"','"+str(res[i][18])+"','"+str(res[i][19])+"')\n")
    return


def import_annee(liste, fichier_destination):    
    with open(fichier_destination, "a") as fichier:
        line = ""
        done = []
        for i in range(1, len(liste)):
            print(liste[i][3], (liste[i][3] in done))
            if not(liste[i][3] in done): # liste[i][3] est l'annee de l'installation
                line = f"INSERT INTO `annee` VALUES ('{liste[i][3]}')\n"
                fichier.write(line)
                done.append(liste[i][3])


def import_mois(fichier_destination):
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

def communes(liste, fichier_destination):
    # Cette fonction extrait les données du fichier "communes-france-2024-limite.csv"
    # et renvoie une liste utilisable par les tables ayant besoin de code INSEE
    line = ""

# ------------------------------- Main --------------------------------------------------

def main():
    #communes = parse_csv("/dataRessources/communes-france-2024-limite.csv")
    liste = parse_csv("dataRessources/cleanData.csv")
    import_mois("import_mois.sql")
    import_annee(liste, "import_annee.sql")
    #import_installation("data.csv","sql2")

main()