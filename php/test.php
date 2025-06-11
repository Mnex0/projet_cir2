<?php
require_once 'database.php';

$db = dbConnect();
$lat = 43.51;
$long = 1.51;
$marqueondu = 'SMA';
$marquepan = 'Sanyo';
$dep = '31';

var_dump(dbRequestRecherche($db, $marqueondu, $marquepan, $dep));