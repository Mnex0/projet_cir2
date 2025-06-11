<?php
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

 function  dbAddValue($db, $login, $text){
    try{
        $request = "INSERT INTO tweets(text, login) VALUES(:text,:login)";
        $statement = $db->prepare($request);
        $statement->bindParam(':login', $login, PDO::PARAM_STR,20);
        $statement->bindParam(':text', $text, PDO::PARAM_STR,80);
        $statement->execute();
    }
    catch (PDOException $exception)
    {
      error_log('Request error: '.$exception->getMessage());
      return false;
    }
    return $result;



}


function dbModifyValue($db, $id, $login, $text){
    try{
        $request = "UPDATE tweets SET text=:text WHERE id=:id AND login=:login";
        $statement = $db->prepare($request);
        $statement->bindParam(':login', $login, PDO::PARAM_STR,20);
        $statement->bindParam(':text', $text, PDO::PARAM_STR,80);
        $statement->bindParam(':id', $id, PDO::PARAM_INT);
        $statement->execute();
    }
    catch (PDOException $exception)
    {
      error_log('Request error: '.$exception->getMessage());
      return false;
    }
    return $result;

}