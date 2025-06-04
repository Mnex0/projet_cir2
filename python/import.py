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
        fichier.write("-- _______________________ Installations __________________________--\n")
        line = ""
        for i in range(len(res)):
            line = f'INSERT INTO `installation`(`id`, `nb_panneau`, `nb_onduleur`, `puissance_crete`, `surface`, `pente`, `pente_optimum`, `orientation`, `orientation_optimum`, `production_pvgis`, `lat`, `lon`, `modele_panneau`, `modele_onduleur`, `nom`, `code_INSEE`, `num_mois`, `num_annee`) VALUES ({res[i][0]}, {res[i][1]}, {res[i][2]}, {res[i][3]}, {res[i][4]}, {res[i][5]}, {res[i][6]}, "{res[i][7]}", "{res[i][8]}", {res[i][9]}, {res[i][10]}, {res[i][11]}, "{res[i][12]}", "{res[i][13]}", "{res[i][14]}", "{res[i][15]}", {res[i][16]}, {res[i][17]})\n'
            fichier.write(line)

# --------------------------- Premier import ------------------------
"""
elif len(done)%10 == 0:
    line = f",\n    ({liste[i][3]})
"""

def import_annee(liste: list, fichier_destination = "sql/import_annee.sql"):    
    with open(fichier_destination, "w") as fichier:
        fichier.write("use projet_cir2;\n-- _______________________ Annees __________________________--\n")
        fichier.write("INSERT INTO `annee`(`num_annee`)\nVALUES")
        line = ""
        done = [""]
        for i in range(1, len(liste)):
            if not(liste[i][3] in done): # liste[i][3] est l'annee de l'installation
                line = f",\n    ({liste[i][3]})"
                if len(done) == 1:
                    line = f"\n    ({liste[i][3]})" # Pas de début avec ","
                fichier.write(line)
                done.append(liste[i][3])
        fichier.write(";\n")

def import_installateur(liste: list, fichier_destination = "sql/import_installateur.sql"):
    with open(fichier_destination, "a") as fichier:
        fichier.write("-- _______________________ Installateurs __________________________--\n")
        fichier.write("INSERT INTO `installateur`(`nom`)\nVALUES")
        line = ""
        done = [""]
        for i in range(1, len(liste)):
            if not((liste[i][16]).lower() in done): # liste[i][16] est le nom de l'installateur, lower permet de vérifier les doublons indistinctement des majuscules
                line = f',\n    ("{liste[i][16]}")'
                if len(done) == 1:
                    line = f'\n    ("{liste[i][16]}")'
                fichier.write(line)
                done.append((liste[i][16]).lower())
        fichier.write(";\n")

def import_marque_ondu(liste: list, fichier_destination = "sql/import_marque_ondu.sql"):
    with open(fichier_destination, "a") as fichier:
        fichier.write("-- _______________________ Marques Onduleurs __________________________--\n")
        fichier.write("INSERT INTO `marque_ondu`(`marque`)\nVALUES")
        line = ""
        done = [""]
        for i in range(1, len(liste)):
            if not((liste[i][8]).lower() in done): # liste[i][8] est la marque d'onduleur
                line = f',\n    ("{liste[i][8]}")'
                if len(done) == 1:
                    line = f'\n    ("{liste[i][8]}")'
                fichier.write(line)
                done.append((liste[i][8]).lower())
        fichier.write(";\n")

def import_marque_pan(liste: list, fichier_destination = "sql/import_marque_pan.sql"):
    with open(fichier_destination, "a") as fichier:
        fichier.write("-- _______________________ Marques Panneaux __________________________--\n")
        fichier.write("INSERT INTO `marque_pan`(`marque`)\nVALUES")
        line = ""
        done = [""]
        for i in range(1, len(liste)):
            if not((liste[i][5]).lower() in done): # liste[i][5] est la marque de panneau
                line = f',\n    ("{liste[i][5]}")'
                if len(done) == 1:
                    line = f'\n    ("{liste[i][5]}")'
                fichier.write(line)
                done.append((liste[i][5]).lower())
        fichier.write(";\n")

def import_mois(fichier_destination = "sql/import_mois.sql"):
    with open(fichier_destination, "a") as fichier:
        fichier.write("-- _______________________ Mois __________________________--\n")
        fichier.write("INSERT INTO `mois`(`num_mois`)\nVALUES\n   ")
        line = ""
        for i in range(11):
            line = f" ({i+1}),"
            fichier.write(line)
        fichier.write(f" (12);\n")


def import_region(liste: list, fichier_destination = "sql/import_region.sql"): # Attention, toujours revérifier s'il reste des caractères étranges dans le sql et les enlever
    with open(fichier_destination, "a") as fichier:
        fichier.write("-- _______________________ Marques Regions __________________________--\n")
        fichier.write("INSERT INTO `region`(`nom_region`)\nVALUES")
        line = ""
        done = [""]
        for i in range(1, len(liste)):
            if not((liste[i][25]).lower() in done): # liste[i][25] est la région (administrative area lvl 1)
                line = f',\n    ("{liste[i][25]}")'
                if len(done) == 1:
                    line = f'\n    ("{liste[i][25]}")'
                fichier.write(line)
                done.append((liste[i][25]).lower())
        fichier.write(";\n")

# ------------------------------- Main --------------------------------------------------

def premierImport(liste: list, fichier_destination = "sql/premierImport.sql"):
    import_annee(liste, fichier_destination)
    import_installateur(liste, fichier_destination)
    import_marque_ondu(liste, fichier_destination)
    import_marque_pan(liste, fichier_destination)
    import_mois(fichier_destination)
    import_region(liste, fichier_destination)

def main():
    liste = parse_csv("dataRessources/cleanData.csv")
    communes = parse_csv("dataRessources/communes-france-2024-limite.csv")
    #premierImport(liste)
    #import_installation(liste, communes, "sql/import_installation.sql")

main()