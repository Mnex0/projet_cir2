#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------


#------------------------------------------------------------
# Table: mois
#------------------------------------------------------------

CREATE TABLE mois(
        num_mois Int 
	,CONSTRAINT mois_PK PRIMARY KEY (num_mois)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: annee
#------------------------------------------------------------

CREATE TABLE annee(
        num_annee Int 
	,CONSTRAINT annee_PK PRIMARY KEY (num_annee)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: marque_pan
#------------------------------------------------------------

CREATE TABLE marque_pan(
        marque Varchar (50) 
	,CONSTRAINT marque_pan_PK PRIMARY KEY (marque)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: modele_pan
#------------------------------------------------------------

CREATE TABLE modele_pan(
        id_pan         Int NOT NULL ,
        modele_panneau Varchar (50) ,
        marque         Varchar (50) 
	,CONSTRAINT modele_pan_PK PRIMARY KEY (id_pan,modele_panneau)

	,CONSTRAINT modele_pan_marque_pan_FK FOREIGN KEY (marque) REFERENCES marque_pan(marque)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: marque_ondu
#------------------------------------------------------------

CREATE TABLE marque_ondu(
        marque Varchar (50) 
	,CONSTRAINT marque_ondu_PK PRIMARY KEY (marque)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: modele_ondu
#------------------------------------------------------------

CREATE TABLE modele_ondu(
        id_ondu         Int NOT NULL,
        modele_onduleur Varchar (50) ,
        marque          Varchar (50) 
	,CONSTRAINT modele_ondu_PK PRIMARY KEY (id_ondu,modele_onduleur)

	,CONSTRAINT modele_ondu_marque_ondu_FK FOREIGN KEY (marque) REFERENCES marque_ondu(marque)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: installateur
#------------------------------------------------------------

CREATE TABLE installateur(
        nom Varchar (50) 
	,CONSTRAINT installateur_PK PRIMARY KEY (nom)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: region
#------------------------------------------------------------

CREATE TABLE region(
        nom_region Varchar (50) 
	,CONSTRAINT region_PK PRIMARY KEY (nom_region)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: departement
#------------------------------------------------------------

CREATE TABLE departement(
        id_dep          Int  Auto_increment  NOT NULL ,
        numero          Varchar (10) ,
        nom_departement Varchar (50) ,
        nom_region      Varchar (50) 
	,CONSTRAINT departement_PK PRIMARY KEY (id_dep)

	,CONSTRAINT departement_region_FK FOREIGN KEY (nom_region) REFERENCES region(nom_region)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: ville
#------------------------------------------------------------

CREATE TABLE ville(
        code_INSEE Varchar (10) ,
        localite   Varchar (50) ,
        id_dep     Int NOT NULL
	,CONSTRAINT ville_PK PRIMARY KEY (code_INSEE)

	,CONSTRAINT ville_departement_FK FOREIGN KEY (id_dep) REFERENCES departement(id_dep)
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: installation
#------------------------------------------------------------

CREATE TABLE installation(
        id                  Int  Auto_increment  NOT NULL ,
        nb_panneau          Int ,
        nb_onduleur         Int ,
        puissance_crete     Int ,
        surface             Float ,
        pente               Int ,
        pente_optimum       Int ,
        orientation         Varchar (10) ,
        orientation_optimum Varchar (10) ,
        production_pvgis    Int ,
        lat                 Float NOT NULL ,
        lon                 Float NOT NULL ,
        id_pan              Int NOT NULL ,
        modele_panneau      Varchar (50) NOT NULL ,
        id_ondu             Int NOT NULL ,
        modele_onduleur     Varchar (50) NOT NULL ,
        nom                 Varchar (50) NOT NULL ,
        code_INSEE          Varchar (10) NOT NULL ,
        num_mois            Int NOT NULL ,
        num_annee           Int NOT NULL
	,CONSTRAINT installation_PK PRIMARY KEY (id)

	,CONSTRAINT installation_modele_pan_FK FOREIGN KEY (id_pan,modele_panneau) REFERENCES modele_pan(id_pan,modele_panneau)
	,CONSTRAINT installation_modele_ondu0_FK FOREIGN KEY (id_ondu,modele_onduleur) REFERENCES modele_ondu(id_ondu,modele_onduleur)
	,CONSTRAINT installation_installateur1_FK FOREIGN KEY (nom) REFERENCES installateur(nom)
	,CONSTRAINT installation_ville2_FK FOREIGN KEY (code_INSEE) REFERENCES ville(code_INSEE)
	,CONSTRAINT installation_mois3_FK FOREIGN KEY (num_mois) REFERENCES mois(num_mois)
	,CONSTRAINT installation_annee4_FK FOREIGN KEY (num_annee) REFERENCES annee(num_annee)
)ENGINE=InnoDB;

