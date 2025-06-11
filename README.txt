MDP ssh : Joatthieu

Les fichier SQL "Safe" sont des versions fonctionnelles d'import de données, au cas où les dernières versions ne fonctionnent pas, les fichiers safe seront toujours à disposition.

MCD : Vérifier les NULL, dans ville la clé localité
CREATE DATABASE projet_cir2
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;
use projet_cir2;
source C:/wamp64/www/projet_cir2/sql/creation_database.sql;
source C:/wamp64/www/projet_cir2/sql/premier_import.sql;
source C:/wamp64/www/projet_cir2/sql/import_intermediaire.sql;
source C:/wamp64/www/projet_cir2/sql/import_final.sql;