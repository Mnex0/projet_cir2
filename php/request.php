<?php
require_once 'database.php';
$db = dbConnect();

if (!$db) {
  header('HTTP/1.1 503 Service Unavailable');
  exit;
}

$requestMethod = $_SERVER['REQUEST_METHOD'];
$request = substr($_SERVER['PATH_INFO'], 1);
$request = explode('/', $request);
$requestRessource = array_shift($request);


$id = array_shift($request);
if ($id == '')
  $id = NULL;

//parse_str(file_get_contents('php://input'), $_PUT);


//Request les info

if ($requestRessource == "chart1") { // Nb d'installations par années
  $data = dbRequestChart1($db);
}
elseif ($requestRessource == "chart2") { // Nb d'installations par région
  $data = dbRequestChart2($db);
}//pas fait 
elseif ($requestRessource == "carte") {
  $data = dbRequestPos($db, $annee, $dep);
}
elseif ($requestRessource == "statEnr") { // Nb statEnregistrement
  $data = dbRequestStatEnr($db);
}
elseif ($requestRessource == "stat2") { // Nb installateur
  $data = dbRequestStat2($db);
}
elseif ($requestRessource == "stat3") { // Nb marque ondu
  $data = dbRequestStat3($db);
}
elseif ($requestRessource == "stat4") { // Nb marque pan
  $data = dbRequestStat4($db);
}
elseif ($requestRessource == "selectRecherche") { // prendre 20 marque ondu, marque pan, et aléatoitement departement
  $data = dbRequestSelectRecherche($db);
}
elseif ($requestRessource == "selectCarte") { // prendre toutes les annees et 20 departements aléa
  $data = dbRequestSelectCarte($db);
}
elseif ($requestRessource == "ping") { // localité et puissance du panneau
  $data = dbRequestPing($db, $lat, $long);
}

//Envoie les info

if ($data != false) {
  header('HTTP/1.1 200 OK');
  echo json_encode($data);
} else
  header('HTTP/1.1 400 Bad Request');
exit;