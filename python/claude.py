import csv
from io import StringIO

def parse_csv_file(file_path):
    temp = []
    
    try:
        with open(file_path, 'r', encoding='utf-8', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                temp.append(row)
        return temp
        
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} n'a pas été trouvé.")
        return []
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return []

def parse_csv_string(csv_string):
    """Parse une chaîne CSV et retourne une liste de listes."""
    temp = []
    csvfile = StringIO(csv_string)
    reader = csv.reader(csvfile)
    
    for row in reader:
        temp.append(row)
        
    return temp

# Exemple d'utilisation
if __name__ == "__main__":
    # Données d'exemple
    sample_csv = '''"761","1137","03","2009","14","Sanyo","HIP-210 NKHE1","1","Sputnik","SOLARMAX SM3000S","2940","18","20",,"Sud",,"BASE, bois, air, soleil, eau","0","46.19","4.74","France","71570",,,"RomanÃ¨che-Thorins","Bourgogne Franche-ComtÃ©","SaÃ´ne-et-Loire",,,'''
    
    # Parse depuis une chaîne
    temp = parse_csv_string(sample_csv)
    
    # Parse depuis un fichier (remplacez par votre chemin)
    temp = parse_csv_file("data.csv")
    
    print(f"Résultat : liste de {len(temp)} lignes")
    print("temp =", temp)