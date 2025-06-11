<?php
require_once 'database.php';

$db = dbConnect();
$lat = 43.51;
$long = 1.51;

var_dump(dbRequestSelectCarte($db));