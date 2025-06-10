<?php
require_once 'database.php';

$db = dbConnect();

var_dump(dbRequestStat4($db));