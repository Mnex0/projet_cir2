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

function dbRequestPos($db, $annee, $dep) 
/*Request pour la carte  */
{
  try {
    $request = 'SELECT lat,lon FROM installation 
    RIGHT JOIN ville ON installation.code_INSEE = ville.code_INSEE 
    RIGHT JOIN departement ON ville.id_dep = departement.id_dep;';
    $request .= 'WHERE num_annee=:annee AND departement.numero=:dep;';
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
    array (size=2)
      'lat' => null
      'lon' => null*/
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
  /*Request pour le nombre d’enregistrement en base*/
  try {
    $request = 'SELECT DISTINCT COUNT(*) FROM installation';
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
  /* Request pour le Nombre d’installateurs */
  try {
    $request = 'SELECT DISTINCT nom FROM installateur ';
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
  /* Request pour le Nombre de marques d’onduleurs */
  try {
    $request = 'SELECT DISTINCT marque FROM marque_ondu ';
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
    $request = 'SELECT DISTINCT marque FROM marque_pan ';
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