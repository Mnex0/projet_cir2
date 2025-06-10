<?php
require_once 'database.php';

$db = dbConnect();

var_dump(dbRequestPos($db, 2012, '02'));