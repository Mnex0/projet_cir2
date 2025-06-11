<?php
require_once 'constants.php';

function dbConnect()
/* Conexion a la BDD */
{
  try {
    $db = new PDO('mysql:host=' . DB_SERVER . ';dbname=' . DB_NAME . ';charset=utf8;' .
      'port=' . DB_PORT, DB_USER, DB_PASSWORD);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  } catch (PDOException $exception) {
    error_log('Connection error: ' . $exception->getMessage());
    return false;
  }
  return $db;
}
function dbRequestChart1($db)
{
  /*Request pour le premier graphique, installations par années*/
  try {
    $request = 'SELECT COUNT(*) as count, num_annee FROM installation GROUP BY num_annee;';
    $statement = $db->prepare($request);
    $statement->execute(); // Exécute la requête
    $result = $statement->fetchAll(PDO::FETCH_ASSOC); // Récupère les résultats
  } catch (PDOException $exception) {
    error_log('RequestChart1 error: ' . $exception->getMessage());
    return false;
  }
  return $result;/*
array (size=30)
0 => 
array (size=2)
'count' => int 3
'num_annee' => int 1990*/
}

function dbRequestChart2($db)
{
  /*Request pour le deuxième graphique, installations par régions*/
  try {
    $request = '
      SELECT COUNT(*) as count, departement.nom_region
      FROM installation
      INNER JOIN ville ON installation.code_INSEE = ville.code_INSEE
      INNER JOIN departement ON ville.id_dep = departement.id_dep
      GROUP BY departement.nom_region;
    ';
    $statement = $db->prepare($request);
    $statement->execute();
    $result = $statement->fetchAll(PDO::FETCH_ASSOC);
  } catch (PDOException $exception) {
    error_log('RequestChart2 error: ' . $exception->getMessage());
    return false;
  }
  return $result;/*
array (size=16)
0 => 
array (size=2)
'count' => int 1034
'nom_region' => string 'Occitanie' (length=9)*/
}


function dbRequestStatEnr($db)
{
  /*Request pour le nombre d'enregistrement en base*/
  try {
    $request = 'SELECT DISTINCT COUNT(*) AS count FROM installation';
    $statement = $db->prepare($request);
    $statement->execute();
    $result = $statement->fetchAll(PDO::FETCH_ASSOC);
  } catch (PDOException $exception) {
    error_log('Request error: ' . $exception->getMessage());
    return false;
  }
  return $result;/*
array (size=1)
0 => 
array (size=1)
'COUNT(*)' => int 24276*/
}

function dbRequestStat2($db)
{
  /* Request pour le Nombre d'installateurs */
  try {
    $request = 'SELECT DISTINCT COUNT(*) AS count FROM installateur';
    $statement = $db->prepare($request);
    $statement->execute();
    $result = $statement->fetchAll(PDO::FETCH_ASSOC);
  } catch (PDOException $exception) {
    error_log('Request error: ' . $exception->getMessage());
    return false;
  }
  return $result;/*
array (size=7308)
0 => 
array (size=1)
'nom' => string 'ED' (length=40)*/
}

function dbRequestStat3($db)
{
  /* Request pour le Nombre de marques d'onduleurs */
  try {
    $request = 'SELECT DISTINCT COUNT(*) AS count FROM marque_ondu ';
    $statement = $db->prepare($request);
    $statement->execute();
    $result = $statement->fetchAll(PDO::FETCH_ASSOC);
  } catch (PDOException $exception) {
    error_log('Request error: ' . $exception->getMessage());
    return false;
  }
  return $result;/*
array (size=154)
0 => 
array (size=1)
'marque' => string 'ABB' (length=3)*/
}

function dbRequestStat4($db)
{
  /*Request pour le Nombre de marques de panneaux solaires : */
  try {
    $request = 'SELECT DISTINCT COUNT(*) AS count FROM marque_pan ';
    $statement = $db->prepare($request);
    $statement->execute();
    $result = $statement->fetchAll(PDO::FETCH_ASSOC);
  } catch (PDOException $exception) {
    error_log('Request error: ' . $exception->getMessage());
    return false;
  }
  return $result;/*
array (size=425)
0 => 
array (size=1)
'marque' => string '3A Energies' (length=11)*/
}

function dbRequestSelectRecherche($db) // renvoie 20 valeurs aléatoire de marques d'ondu et de panneaux et de départements
{
  try {
    $request = 'SELECT DISTINCT modele_pan.marque AS marque_pan, modele_ondu.marque AS marque_ondu, departement.numero, departement.nom_departement FROM installation 
    INNER JOIN ville ON installation.code_INSEE = ville.code_INSEE 
    INNER JOIN departement ON ville.id_dep = departement.id_dep 
    INNER JOIN modele_pan ON installation.id_pan = modele_pan.id_pan 
    INNER JOIN modele_ondu ON installation.id_ondu = modele_ondu.id_ondu 
    ORDER BY RAND() 
    LIMIT 20;';
    $statement = $db->prepare($request);
    $statement->execute();
    $result = $statement->fetchAll(PDO::FETCH_ASSOC);
  } catch (PDOException $exception) {
    error_log('Request error: ' . $exception->getMessage());
    return false;
  }
  return $result;/*
  array (size=20)
  0 => 
    array (size=3)
      'marque' => string 'SMA' (length=3)
      'numero' => string '67' (length=2)
      'nom_departement' => string 'Bas-Rhin' (length=8)*/
}

function dbRequestSelectCarte($db) // renvoie toutes les annees et 20 departements aléa
{
  try {
    $request1 = 'SELECT DISTINCT num_annee FROM installation';
    $statement1 = $db->prepare($request1);
    $statement1->execute();
    $result1 = $statement1->fetchAll(PDO::FETCH_ASSOC);
    $request2 = 'SELECT DISTINCT departement.numero, departement.nom_departement FROM installation
    INNER JOIN ville ON installation.code_INSEE = ville.code_INSEE 
    INNER JOIN departement ON ville.id_dep = departement.id_dep 
    INNER JOIN modele_pan ON installation.id_pan = modele_pan.id_pan 
    INNER JOIN modele_ondu ON installation.id_ondu = modele_ondu.id_ondu 
    ORDER BY RAND() 
    LIMIT 20;';
    $statement2 = $db->prepare($request2);
    $statement2->execute();
    $result2 = $statement2->fetchAll(PDO::FETCH_ASSOC);
  } catch (PDOException $exception) {
    error_log('Request error: ' . $exception->getMessage());
    return false;
  }
  return [$result1, $result2];/*
  array (size=2)
  0 => 
    array (size=30)
      0 => 
        array (size=1)
          'num_annee' => int 1990
  1 => 
    array (size=20)
      0 => 
        array (size=2)
          'numero' => string '38' (length=2)
          'nom_departement' => string 'Is├¿re' (length=9)*/
}

function dbRequestPos($db, $annee, $dep)
/*Request pour la carte  */
{
  try {
    $request = 'SELECT lat, lon, puissance_crete AS puissance, ville.localite AS localite FROM installation 
    RIGHT JOIN ville ON installation.code_INSEE = ville.code_INSEE 
    RIGHT JOIN departement ON ville.id_dep = departement.id_dep
    WHERE num_annee=:annee AND departement.numero=:dep;';
    $statement = $db->prepare($request);
    $statement->bindParam(':annee', $annee, PDO::PARAM_INT);
    $statement->bindParam(':dep', $dep, PDO::PARAM_STR, 20);
    $statement->execute();
    $result = $statement->fetchAll(PDO::FETCH_ASSOC);
  } catch (PDOException $exception) {
    error_log('Request error: ' . $exception->getMessage());
    return false;
  }
  return $result;
  /*
  array (size=24389)
  0 => 
    array (size=4)
      'lat' => null
      'lon' => null
      'puissance' => 1000
      'localite' => 'Paris'
      */
}

function dbRequestRechercheAll($db, $m_ondu, $m_pan, $dep) {
  try {
    $request = 'SELECT id, num_mois AS mois, num_annee AS annee, nb_panneau, puissance_crete AS puissance, surface, puissance_crete, ville.localite AS localite FROM installation 
    RIGHT JOIN ville ON installation.code_INSEE = ville.code_INSEE 
    RIGHT JOIN departement ON ville.id_dep = departement.id_dep
    RIGHT JOIN modele_pan ON installation.modele_panneau = modele_pan.modele_panneau
    RIGHT JOIN modele_ondu ON installation.modele_onduleur = modele_ondu.modele_onduleur
    RIGHT JOIN marque_pan ON modele_pan.marque = marque_pan.marque
    RIGHT JOIN marque_ondu ON modele_ondu.marque = marque_ondu.marque
    WHERE marque_ondu.marque=:mondu AND marque_pan.marque=:mpan AND departement.numero=:dep;';
    $statement = $db->prepare($request);
    $statement->bindParam(':mondu', $m_ondu, PDO::PARAM_STR, 50);
    $statement->bindParam(':mpan', $m_pan, PDO::PARAM_STR, 50);
    $statement->bindParam(':dep', $dep, PDO::PARAM_STR, 50);
    $statement->execute();
    $result = $statement->fetchAll(PDO::FETCH_ASSOC);
  } catch (PDOException $exception) {
    error_log('Request error: ' . $exception->getMessage());
    return false;
  }
  return $result;
}

function dbRequestDetails($db, $id) {
  try {
    $request = 'SELECT id, num_mois AS mois_installation, num_annee AS an_installation, nb_panneau, modele_pan.marque AS marque_pan, modele_pan.modele_panneau AS modele_pan, nb_onduleur, modele_ondu.marque, modele_ondu.modele_onduleur, puissance_crete, surface, pente, pente_optimum, orientation, orientation_optimum, nom AS installatur, production_pvgis, lat, lon, installation.code_INSEE, ville.localite AS localite, departement.numero, departement.nom_departement, departement.nom_region  FROM installation 
    JOIN ville ON installation.code_INSEE = ville.code_INSEE 
    JOIN departement ON ville.id_dep = departement.id_dep
    JOIN modele_pan ON installation.modele_panneau = modele_pan.modele_panneau
    JOIN modele_ondu ON installation.modele_onduleur = modele_ondu.modele_onduleur
    WHERE installation.id=:id;';
    $statement = $db->prepare($request);
    $statement->bindParam(':id', $id, PDO::PARAM_STR);
    $statement->execute();
    $result = $statement->fetchAll(PDO::FETCH_ASSOC);
  } catch (PDOException $exception) {
    error_log('Request error: ' . $exception->getMessage());
    return false;
  }
  return $result;
}