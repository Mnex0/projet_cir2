MDP ssh : Joatthieu

Ne sont pas disponibles :
    - La partie back avec visualisation, ajout et modification de données
    - Le graphique par région et par année
    - La recherche d'installation sans champs précisé

Exemple d'import : 
DROP DATABASE IF EXISTS projet_cir2;
CREATE DATABASE projet_cir2
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;
use projet_cir2;
source C:/wamp64/www/projet_cir2/sql/creation_database.sql;
source C:/wamp64/www/projet_cir2/sql/premier_import.sql;
source C:/wamp64/www/projet_cir2/sql/import_intermediaire.sql;
source C:/wamp64/www/projet_cir2/sql/import_final.sql;