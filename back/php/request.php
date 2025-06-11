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


if ($requestRessource == "modifier") { 
  $data = dbModifyValue($db, $id, $login, $text);
}

if ($requestRessource == "modifier") { 
  $data = dbModifyValue($db, $id, $login, $text);
}
