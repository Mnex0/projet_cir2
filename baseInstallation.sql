#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: mois
#------------------------------------------------------------

CREATE TABLE mois(
        num_mois Int NOT NULL
	,CONSTRAINT mois_PK PRIMARY KEY (num_mois)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: annee
#------------------------------------------------------------

CREATE TABLE annee(
        num_annee Int NOT NULL
	,CONSTRAINT annee_PK PRIMARY KEY (num_annee)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: panneau_marque
#------------------------------------------------------------

CREATE TABLE panneau_marque(
        marque Varchar (50) NOT NULL
	,CONSTRAINT panneau_marque_PK PRIMARY KEY (marque)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: panneau_modele
#------------------------------------------------------------

CREATE TABLE panneau_modele(
        modele Varchar (50) NOT NULL ,
        marque Varchar (50) NOT NULL
	,CONSTRAINT panneau_modele_PK PRIMARY KEY (modele)

	,CONSTRAINT panneau_modele_panneau_marque_FK FOREIGN KEY (marque) REFERENCES panneau_marque(marque)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: onduleur_marque
#------------------------------------------------------------

CREATE TABLE onduleur_marque(
        marque Varchar (50) NOT NULL
	,CONSTRAINT onduleur_marque_PK PRIMARY KEY (marque)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: onduleur_modele
#------------------------------------------------------------

CREATE TABLE onduleur_modele(
        modele Varchar (50) NOT NULL ,
        marque Varchar (50) NOT NULL
	,CONSTRAINT onduleur_modele_PK PRIMARY KEY (modele)

	,CONSTRAINT onduleur_modele_onduleur_marque_FK FOREIGN KEY (marque) REFERENCES onduleur_marque(marque)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: installateur
#------------------------------------------------------------

CREATE TABLE installateur(
        nom Varchar (50) NOT NULL
	,CONSTRAINT installateur_PK PRIMARY KEY (nom)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: region
#------------------------------------------------------------

CREATE TABLE region(
        nom_region Varchar (50) NOT NULL
	,CONSTRAINT region_PK PRIMARY KEY (nom_region)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: departement
#------------------------------------------------------------

CREATE TABLE departement(
        numero          Varchar (6) NOT NULL ,
        nom_departement Varchar (50) NOT NULL ,
        nom_region      Varchar (50) NOT NULL
	,CONSTRAINT departement_PK PRIMARY KEY (numero)

	,CONSTRAINT departement_region_FK FOREIGN KEY (nom_region) REFERENCES region(nom_region)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: ville
#------------------------------------------------------------

CREATE TABLE ville(
        codeINSEE Varchar (6) NOT NULL ,
        localite  Varchar (50) NOT NULL ,
        numero    Varchar (6) NOT NULL
	,CONSTRAINT ville_AK UNIQUE (localite)
	,CONSTRAINT ville_PK PRIMARY KEY (codeINSEE)

	,CONSTRAINT ville_departement_FK FOREIGN KEY (numero) REFERENCES departement(numero)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: installation
#------------------------------------------------------------

CREATE TABLE installation(
        id                     Int  Auto_increment  NOT NULL ,
        nb_panneau             Int NOT NULL ,
        nb_onduleur            Int NOT NULL ,
        puissance_crete        Int NOT NULL ,
        surface                Float NOT NULL ,
        pente                  Int NOT NULL ,
        pente_optimum          Int NOT NULL ,
        orientation            Varchar (5) NOT NULL ,
        orientation_optimum    Varchar (5) NOT NULL ,
        production_pvgis       Int NOT NULL ,
        lat                    Float NOT NULL ,
        lon                    Float NOT NULL ,
        modele                 Varchar (50) NOT NULL ,
        modele_onduleur_modele Varchar (50) NOT NULL ,
        nom                    Varchar (50) NOT NULL ,
        codeINSEE              Varchar (6) NOT NULL ,
        num_mois               Int NOT NULL ,
        num_annee              Int NOT NULL
	,CONSTRAINT installation_PK PRIMARY KEY (id)

	,CONSTRAINT installation_panneau_modele_FK FOREIGN KEY (modele) REFERENCES panneau_modele(modele)
	,CONSTRAINT installation_onduleur_modele0_FK FOREIGN KEY (modele_onduleur_modele) REFERENCES onduleur_modele(modele)
	,CONSTRAINT installation_installateur1_FK FOREIGN KEY (nom) REFERENCES installateur(nom)
	,CONSTRAINT installation_ville2_FK FOREIGN KEY (codeINSEE) REFERENCES ville(codeINSEE)
	,CONSTRAINT installation_mois3_FK FOREIGN KEY (num_mois) REFERENCES mois(num_mois)
	,CONSTRAINT installation_annee4_FK FOREIGN KEY (num_annee) REFERENCES annee(num_annee)
)ENGINE=InnoDB;

