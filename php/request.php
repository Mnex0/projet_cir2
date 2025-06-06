<?
 require_once('database.php');
 $db=dbConnect();
 
 
 if(!$db){
    header('HTTP/1.1 503 Service Unavailable');
    exit;
 }

 
 $requestMethod = $_SERVER['REQUEST_METHOD'];
 $request = substr($_SERVER['PATH_INFO'],1);
 $request = explode('/', $request);
 $requestRessource=array_shift($request);


$id=array_shift($request);
if($id=='')
   $id=NULL;

parse_str(file_get_contents('php://input'), $_PUT);


//Request les info

if($requestRessource=="chart1" ){$data=dbRequestChart1($db);}

if($requestRessource=="carte" ){$data=dbRequestPos($db,$annee,$dep);}

if($requestRessource=="stat1" ){$data=dbRequestStat1($db);}
if($requestRessource=="stat2" ){$data=dbRequestStat2($db);}
if($requestRessource=="stat3" ){$data=dbRequestStat3($db);}
if($requestRessource=="stat4" ){$data=dbRequestStat4($db);}

//Envoie les info


if ($data !== false)
 {
   header('HTTP/1.1 200 OK');
   echo json_encode($data);
 }
 else
   header('HTTP/1.1 400 Bad Request');
 exit;

 ?>