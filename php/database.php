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
    $request = 'SELECT lat,lon FROM installation';
    $request .= ' WHERE annee=:annee';
    $request .= ' AND WHERE dep=:dep ';
    $statement = $db->prepare($request);
    $statement->bindParam(':annee', $annee, PDO::PARAM_STR, 20);
    $statement->bindParam(':dep', $dep, PDO::PARAM_STR, 20);
    $statement->execute();
    $result = $statement->fetchALl(PDO::FETCH_ASSOC);
  } catch (PDOException $exception) {
    error_log('Request error: ' . $exception->getMessage());
    return false;
  }
  return $result;
}

function dbRequestChart1($db)
{
  /*Request pour le premier graphique, installations par années*/
  try {
    $request = 'SELECT COUNT(*), annee FROM installation GROUP BY annee ';
    $statement = $db->prepare($request);
    $result = $statement->fetchALl(PDO::FETCH_ASSOC);
  } catch (PDOException $exception) {
    error_log('RequestChart1 error: ' . $exception->getMessage());
    return false;
  }
  return $result;
}

function dbRequestChart2($db)
{
  /*Request pour le premier graphique, installations par régions*/
  try {
    $request = 'SELECT COUNT(*), region FROM installation GROUP BY region';
    $statement = $db->prepare($request);
    $result = $statement->fetchALl(PDO::FETCH_ASSOC);
  } catch (PDOException $exception) {
    error_log('RequestChart2 error: ' . $exception->getMessage());
    return false;
  }
  return $result;
}

function dbRequestStat1($db)
{
  /*Request pour le  nombre d’enregistrement en base*/
  try {
    $request = 'SELECT COUNT(*)FROM installation ';
    $statement = $db->prepare($request);
    $result = $statement->fetchALl(PDO::FETCH_ASSOC);
  } catch (PDOException $exception) {
    error_log('Request error: ' . $exception->getMessage());
    return false;
  }
  return $result;
}

function dbRequestStat2($db)
{
  /* Request pour le Nombre d’installateurs */
  try {
    $request = 'SELECT nom FROM installateur ';
    $statement = $db->prepare($request);
    $result = $statement->fetchALl(PDO::FETCH_ASSOC);
  } catch (PDOException $exception) {
    error_log('Request error: ' . $exception->getMessage());
    return false;
  }
  return $result;
}

function dbRequestStat3($db)
{
  /* Request pour le Nombre de marques d’onduleurs */
  try {
    $request = 'SELECT marque FROM marque_ondu ';
    $statement = $db->prepare($request);
    $result = $statement->fetchALl(PDO::FETCH_ASSOC);
  } catch (PDOException $exception) {
    error_log('Request error: ' . $exception->getMessage());
    return false;
  }
  return $result;
}

function dbRequestStat4($db)
{
  /*Request pour le Nombre de marques de panneaux solaires : */
  try {
    $request = 'SELECT marque FROM marque_pan ';
    $statement = $db->prepare($request);
    $result = $statement->fetchALl(PDO::FETCH_ASSOC);
  } catch (PDOException $exception) {
    error_log('Request error: ' . $exception->getMessage());
    return false;
  }
  return $result;
}