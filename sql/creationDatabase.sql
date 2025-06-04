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
# Table: marque_pan
#------------------------------------------------------------

CREATE TABLE marque_pan(
        marque Varchar (50) NOT NULL
	,CONSTRAINT marque_pan_PK PRIMARY KEY (marque)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: modele_pan
#------------------------------------------------------------

CREATE TABLE modele_pan(
        modele_panneau Varchar (50) NOT NULL ,
        marque         Varchar (50) NOT NULL
	,CONSTRAINT modele_pan_PK PRIMARY KEY (modele_panneau)

	,CONSTRAINT modele_pan_marque_pan_FK FOREIGN KEY (marque) REFERENCES marque_pan(marque)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: marque_ondu
#------------------------------------------------------------

CREATE TABLE marque_ondu(
        marque Varchar (50) NOT NULL
	,CONSTRAINT marque_ondu_PK PRIMARY KEY (marque)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: modele_ondu
#------------------------------------------------------------

CREATE TABLE modele_ondu(
        modele_ondulateur Varchar (50) NOT NULL ,
        marque            Varchar (50) NOT NULL
	,CONSTRAINT modele_ondu_PK PRIMARY KEY (modele_ondulateur)

	,CONSTRAINT modele_ondu_marque_ondu_FK FOREIGN KEY (marque) REFERENCES marque_ondu(marque)
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
        code_INSEE Varchar (6) NOT NULL ,
        localite   Varchar (50) NOT NULL ,
        numero     Varchar (6) NOT NULL
	,CONSTRAINT ville_AK UNIQUE (localite)
	,CONSTRAINT ville_PK PRIMARY KEY (code_INSEE)

	,CONSTRAINT ville_departement_FK FOREIGN KEY (numero) REFERENCES departement(numero)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: installation
#------------------------------------------------------------

CREATE TABLE installation(
        id                  Int  Auto_increment  NOT NULL ,
        nb_panneau          Int NOT NULL ,
        nb_onduleur         Int NOT NULL ,
        puissance_crete     Int NOT NULL ,
        surface             Float NOT NULL ,
        pente               Int NOT NULL ,
        pente_optimum       Int NOT NULL ,
        orientation         Varchar (5) NOT NULL ,
        orientation_optimum Varchar (5) NOT NULL ,
        production_pvgis    Int NOT NULL ,
        lat                 Float NOT NULL ,
        lon                 Float NOT NULL ,
        modele_panneau      Varchar (50) NOT NULL ,
        modele_ondulateur   Varchar (50) NOT NULL ,
        nom                 Varchar (50) NOT NULL ,
        code_INSEE          Varchar (6) NOT NULL ,
        num_mois            Int NOT NULL ,
        num_annee           Int NOT NULL
	,CONSTRAINT installation_PK PRIMARY KEY (id)

	,CONSTRAINT installation_modele_pan_FK FOREIGN KEY (modele_panneau) REFERENCES modele_pan(modele_panneau)
	,CONSTRAINT installation_modele_ondu0_FK FOREIGN KEY (modele_ondulateur) REFERENCES modele_ondu(modele_ondulateur)
	,CONSTRAINT installation_installateur1_FK FOREIGN KEY (nom) REFERENCES installateur(nom)
	,CONSTRAINT installation_ville2_FK FOREIGN KEY (code_INSEE) REFERENCES ville(code_INSEE)
	,CONSTRAINT installation_mois3_FK FOREIGN KEY (num_mois) REFERENCES mois(num_mois)
	,CONSTRAINT installation_annee4_FK FOREIGN KEY (num_annee) REFERENCES annee(num_annee)
)ENGINE=InnoDB;

