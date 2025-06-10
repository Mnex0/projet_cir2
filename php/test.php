<?php
require_once 'database.php';

$db = dbConnect();

var_dump(dbRequestSelectCarte   ($db));