import csv
import os

def parse_csv(file_path):
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        return data

    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} n'a pas été trouvé.")
        return []
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return []

def calculer_nb_lignes(nom_fichier):
    with open(nom_fichier,"r") as fichier:
        l=fichier.readlines()
    return len(l)

def associe_INSEE(communes: list, ville, code_postal):
    if code_postal == 'NULL' or ville == 'NULL':
        return 'NULL'
    
    # Recherche exacte par code postal et nom de ville
    for i in range(1, len(communes)):  # Commence à 1 pour éviter l'en-tête
        if (communes[i][6] == code_postal and communes[i][1].lower() == ville.lower()):
            return f'"{communes[i][0]}"'
    
    # Si pas trouvé, recherche par code postal seulement
    for i in range(1, len(communes)):
        if communes[i][6] == code_postal:
            return f'"{communes[i][0]}"'
    
    return 'NULL'  # Si aucune correspondance trouvée

def nuller_data(data: list):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '':
                data[i][j] = 'NULL'
    return data

# ___________________________ IMPORTS __________________________________________________________________________________________________________

# --------------------------- Premiers imports ----------------------------------------------------------------------------------

def import_annee(data: list, fichier_destination = "sql/import_annee.sql"):    
    os.makedirs("sql", exist_ok=True)
    with open(fichier_destination, "w", encoding="utf-8") as fichier:
        fichier.write("use projet_cir2;\n-- _______________________ Annees __________________________--\n")
        fichier.write("INSERT INTO `annee`(`num_annee`)\nVALUES")
        line = ""
        done = [""]
        for i in range(1, len(data)):
            if not(data[i][3] in done):
                line = f", ({data[i][3]})"
                if len(done) == 1:
                    line = f"\n    ({data[i][3]})"
                elif len(done)%10 == 0:
                    line = f",\n    ({data[i][3]})"
                fichier.write(line)
                done.append(data[i][3])
        fichier.write(";\n")

def import_installateur(data: list, fichier_destination = "sql/import_installateur.sql"):
    with open(fichier_destination, "a", encoding="utf-8") as fichier:
        fichier.write("-- _______________________ Installateurs __________________________--\n")
        fichier.write("INSERT INTO `installateur`(`nom`)\nVALUES")
        line = ""
        done = [""]
        for i in range(1, len(data)):
            if not((data[i][16]).lower() in done):
                line = f', ("{data[i][16]}")'
                if len(done) == 1:
                    line = f'\n    ("{data[i][16]}")'
                elif len(done)%10 == 0:
                    line = f',\n    ("{data[i][16]}")'
                fichier.write(line)
                done.append((data[i][16]).lower())
        fichier.write(";\n")

def import_marque_ondu(data: list, fichier_destination = "sql/import_marque_ondu.sql"):
    with open(fichier_destination, "a", encoding="utf-8") as fichier:
        fichier.write("-- _______________________ Marques Onduleurs __________________________--\n")
        fichier.write("INSERT INTO `marque_ondu`(`marque`)\nVALUES")
        line = ""
        done = [""]
        for i in range(1, len(data)):
            if not((data[i][8]).lower() in done):
                line = f', ("{data[i][8]}")'
                if len(done) == 1:
                    line = f'\n    ("{data[i][8]}")'
                elif len(done)%10 == 0:
                    line = f',\n    ("{data[i][8]}")'
                fichier.write(line)
                done.append((data[i][8]).lower())
        fichier.write(";\n")

def import_marque_pan(data: list, fichier_destination = "sql/import_marque_pan.sql"):
    with open(fichier_destination, "a", encoding="utf-8") as fichier:
        fichier.write("-- _______________________ Marques Panneaux __________________________--\n")
        fichier.write("INSERT INTO `marque_pan`(`marque`)\nVALUES")
        line = ""
        done = [""]
        for i in range(1, len(data)):
            if not((data[i][5]).lower() in done):
                line = f', ("{data[i][5]}")'
                if len(done) == 1:
                    line = f'\n    ("{data[i][5]}")'
                elif len(done)%10 == 0:
                    line = f',\n    ("{data[i][5]}")'
                fichier.write(line)
                done.append((data[i][5]).lower())
        fichier.write(";\n")

def import_mois(fichier_destination = "sql/import_mois.sql"):
    with open(fichier_destination, "a", encoding="utf-8") as fichier:
        fichier.write("-- _______________________ Mois __________________________--\n")
        fichier.write("INSERT INTO `mois`(`num_mois`)\nVALUES\n   ")
        line = ""
        for i in range(11):
            line = f" ({i+1}),"
            fichier.write(line)
        fichier.write(f" (12);\n")

def import_region(communes: list, fichier_destination = "sql/import_region.sql"):
    with open(fichier_destination, "a", encoding="utf-8") as fichier:
        fichier.write("-- _______________________ Regions __________________________--\n")
        fichier.write("INSERT INTO `region`(`nom_region`)\nVALUES")
        line = ""
        done = [""]
        
        # Utilise les régions du fichier communes
        for i in range(1, len(communes)):  # Commence à 1 pour éviter l'en-tête
            region_nom = communes[i][3]
            if not(region_nom.lower() in done) and region_nom != 'NULL':
                line = f', ("{region_nom}")'
                if len(done) == 1:
                    line = f'\n    ("{region_nom}")'
                elif len(done)%5 == 0:
                    line = f',\n    ("{region_nom}")'
                fichier.write(line)
                done.append(region_nom.lower())
        fichier.write(";\n")

# --------------------------- Imports intermédiaires ----------------------------------------------------------------------------

def import_departement(communes: list, fichier_destination = "sql/import_departement.sql"):
    with open(fichier_destination, "w", encoding="utf-8") as fichier:
        fichier.write("use projet_cir2;\n-- _______________________ Departements __________________________--\n")
        fichier.write("INSERT INTO `departement`(`numero`, `nom_departement`, `nom_region`)\nVALUES")
        line = ""
        done = [""]
        
        # Utilise les départements du fichier communes
        for i in range(1, len(communes)):  # Commence à 1 pour éviter l'en-tête
            dep_numero = communes[i][4]
            dep_nom = communes[i][5]
            region_nom = communes[i][3]
            dep_key = (dep_numero.lower(), dep_nom.lower())
            
            if not(dep_key in done) and dep_numero != 'NULL' and dep_nom != 'NULL':
                if len(done) == 1:
                    line = f'\n    '
                elif len(done)%5 == 0:
                    line = f',\n    '
                else:
                    line = f', '
                
                line += f'("{dep_numero}", "{dep_nom}", "{region_nom}")'
                
                fichier.write(line)
                done.append(dep_key)
        fichier.write(";\n")

def import_ville(communes: list, fichier_destination = "sql/import_ville.sql"):
    with open(fichier_destination, "a", encoding="utf-8") as fichier:
        fichier.write("-- _______________________ Villes __________________________--\n")
        fichier.write("INSERT INTO `ville`(`code_INSEE`, `localite`, `id_dep`)\nVALUES")
        line = ""
        first = True
        
        # Utilise directement les villes du fichier communes
        for i in range(1, len(communes)):  # Commence à 1 pour éviter l'en-tête
            code_insee = communes[i][0]
            localite = communes[i][1]
            dep_numero = communes[i][4]
            
            if code_insee != 'NULL' and localite != 'NULL' and dep_numero != 'NULL':
                if first:
                    line = f'\n    '
                    first = False
                elif i % 5 == 0:
                    line = f',\n    '
                else:
                    line = f', '

                line += f'("{code_insee}", "{localite}", (SELECT id_dep FROM departement WHERE numero = "{dep_numero}" LIMIT 1))'
                
                fichier.write(line)
        fichier.write(";\n")

def import_modele_ondu(data: list, fichier_destination = "sql/import_modele_ondu.sql"):
    with open(fichier_destination, "a", encoding="utf-8") as fichier:
        fichier.write("-- _______________________ Modeles onduleurs __________________________--\n")
        fichier.write("INSERT INTO `modele_ondu`(`id_ondu`, `modele_onduleur`, `marque`)\nVALUES")
        line = ""
        done = [""]
        id_counter = 1
        
        for i in range(1, len(data)):
            modele_key = (data[i][9].lower(), data[i][8].lower())
            if not(modele_key in done):
                if len(done) == 1:
                    line = f'\n    '
                elif len(done)%5 == 0:
                    line = f',\n    '
                else:
                    line = f', '
                line += f'({id_counter}, "{data[i][9]}", "{data[i][8]}")'
                done.append(modele_key)
                fichier.write(line)
                id_counter += 1
        fichier.write(";\n")

def import_modele_pan(data: list, fichier_destination = "sql/import_modele_pan.sql"):
    with open(fichier_destination, "a", encoding="utf-8") as fichier:
        fichier.write("-- _______________________ Modeles panneaux __________________________--\n")
        fichier.write("INSERT INTO `modele_pan`(`id_pan`, `modele_panneau`, `marque`)\nVALUES")
        line = ""
        done = [""]
        id_counter = 1
        
        for i in range(1, len(data)):
            modele_key = (data[i][6].lower(), data[i][5].lower())
            if not(modele_key in done):
                if len(done) == 1:
                    line = f'\n    '
                elif len(done)%5 == 0:
                    line = f',\n    '
                else:
                    line = f', '
                line += f'({id_counter}, "{data[i][6]}", "{data[i][5]}")'
                done.append(modele_key)
                fichier.write(line)
                id_counter += 1
        fichier.write(";\n")

# --------------------------- Import final --------------------------------------------------------------------------------------

def get_id_mappings(data: list):
    """Crée des mappings pour les IDs des modèles"""
    pan_mapping = {}
    ondu_mapping = {}
    
    # Mapping pour panneaux
    done_pan = []
    id_counter_pan = 1
    for i in range(1, len(data)):
        modele_key = (data[i][6].lower(), data[i][5].lower())
        if not(modele_key in done_pan):
            pan_mapping[modele_key] = id_counter_pan
            done_pan.append(modele_key)
            id_counter_pan += 1
    
    # Mapping pour onduleurs
    done_ondu = []
    id_counter_ondu = 1
    for i in range(1, len(data)):
        modele_key = (data[i][9].lower(), data[i][8].lower())
        if not(modele_key in done_ondu):
            ondu_mapping[modele_key] = id_counter_ondu
            done_ondu.append(modele_key)
            id_counter_ondu += 1
    
    return pan_mapping, ondu_mapping

def import_installation(data: list, communes: list, fichier_destination = "sql/import_installation.sql"):
    pan_mapping, ondu_mapping = get_id_mappings(data)
    
    with open(fichier_destination, "w", encoding="utf-8") as fichier:
        fichier.write("use projet_cir2;\n-- _______________________ Installations __________________________--\n")
        fichier.write("INSERT INTO `installation`(`nb_panneau`, `nb_onduleur`, `puissance_crete`, `surface`, `pente`, `pente_optimum`, `orientation`, `orientation_optimum`, `production_pvgis`, `lat`, `lon`, `id_pan`, `modele_panneau`, `id_ondu`, `modele_onduleur`, `nom`, `code_INSEE`, `num_mois`, `num_annee`)\nVALUES")
        
        done = []
        first = True
        
        for i in range(1, len(data)):
            # Utilise la nouvelle fonction associe_INSEE qui gère mieux les correspondances
            insee = associe_INSEE(communes, data[i][24], data[i][21])
            
            # Skip cette installation si pas de correspondance INSEE valide
            if insee == 'NULL':
                continue
            
            # Récupération des IDs
            pan_key = (data[i][6].lower(), data[i][5].lower()) if data[i][6] != 'NULL' and data[i][5] != 'NULL' else None
            ondu_key = (data[i][9].lower(), data[i][8].lower()) if data[i][9] != 'NULL' and data[i][8] != 'NULL' else None
            
            # Skip si pas de modèle valide
            if not pan_key or not ondu_key:
                continue
                
            id_pan = pan_mapping.get(pan_key, 1)
            id_ondu = ondu_mapping.get(ondu_key, 1)
            
            # Création de la ligne de données (sans l'ID auto-increment)
            temp = [
                ('NULL' if data[i][4] == 'NULL' else data[i][4]),        # nb_panneau
                ('NULL' if data[i][7] == 'NULL' else data[i][7]),        # nb_onduleur
                ('NULL' if data[i][10] == 'NULL' else data[i][10]),      # puissance_crete
                ('NULL' if data[i][11] == 'NULL' else data[i][11]),      # surface
                ('NULL' if data[i][12] == 'NULL' else data[i][12]),      # pente
                ('NULL' if data[i][13] == 'NULL' else data[i][13]),      # pente_optimum
                ('NULL' if data[i][14] == 'NULL' else f'"{data[i][14]}"'), # orientation
                ('NULL' if data[i][15] == 'NULL' else f'"{data[i][15]}"'), # orientation_optimum
                ('NULL' if data[i][17] == 'NULL' else data[i][17]),      # production_pvgis
                data[i][18],                                             # lat
                data[i][19],                                             # lon
                id_pan,                                                  # id_pan
                f'"{data[i][6]}"',                                       # modele_panneau
                id_ondu,                                                 # id_ondu
                f'"{data[i][9]}"',                                       # modele_onduleur
                f'"{data[i][16]}"',                                      # nom installateur
                insee,                                                   # code_INSEE
                ('NULL' if data[i][2] == 'NULL' else data[i][2]),        # num_mois
                ('NULL' if data[i][3] == 'NULL' else data[i][3])         # num_annee
            ]
            
            # Vérification des doublons
            if not(temp in done):
                if first:
                    line = f'\n    ('
                    first = False
                else:
                    line = f',\n    ('
                
                line += ', '.join(str(val) for val in temp)
                line += ')'
                
                fichier.write(line)
                done.append(temp)
        
        fichier.write(";\n")

# _______________________________________________ Main _______________________________________________________________________________________________________________________

def premier_import(data: list, communes: list, fichier_destination = "sql/premier_import.sql"):
    import_annee(data, fichier_destination)
    import_installateur(data, fichier_destination)
    import_marque_ondu(data, fichier_destination)
    import_marque_pan(data, fichier_destination)
    import_mois(fichier_destination)
    import_region(communes, fichier_destination)
    print("Premier import SQL généré avec succès !")

def import_intermediaire(data: list, communes: list, fichier_destination = "sql/import_intermediaire.sql"):
    import_departement(communes, fichier_destination)
    import_modele_ondu(data, fichier_destination)
    import_modele_pan(data, fichier_destination)
    import_ville(communes, fichier_destination)
    print("Import intermédiaire SQL généré avec succès !")

def import_final(data: list, communes: list, fichier_destination = "sql/import_final.sql"):
    import_installation(data, communes, fichier_destination)
    print("Import final SQL généré avec succès !")

def main():
    data = nuller_data(parse_csv("dataRessources/cleanData.csv"))
    communes = parse_csv("dataRessources/communes-france-2024-limite.csv")  # Utilise le nouveau fichier
    
    print("Génération des fichiers d'import SQL...")
    premier_import(data, communes)
    import_intermediaire(data, communes)
    import_final(data, communes)
    print("Tous les fichiers d'import SQL ont été générés avec succès !")

if __name__ == "__main__":
    main()