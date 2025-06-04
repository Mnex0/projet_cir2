<?php
 require_once('constants.php');

function dbConnect()
 {
   try
   {
     $db = new PDO('mysql:host='.DB_SERVER.';dbname='.DB_NAME.';charset=utf8;'.
       'port='.DB_PORT, DB_USER, DB_PASSWORD);
     $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); 
   }
   catch (PDOException $exception)
   {
     error_log('Connection error: '.$exception->getMessage());
     return false;
   }
   return $db;
 }
  
 
function dbRequestPos($db)
{

    try
    {
      $request = 'SELECT l FROM tweets';
      if($login != '')
        $request .= ' WHERE login=:login';
      $statement = $db->prepare($request);
      if($login != '')
        $statement->bindParam(':login', $login, PDO::PARAM_STR,20);
      $statement->execute();
      $result = $statement->fetchALl(PDO::FETCH_ASSOC);
    }
    catch (PDOException $exception)
    {
      error_log('Request error: '.$exception->getMessage());
      return false;
    }
    return $result;
}

?>