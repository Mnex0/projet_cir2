<?php
require_once 'database.php';

$db = dbConnect();

var_dump(dbRequestStat3   ($db));