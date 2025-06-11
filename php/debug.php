<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

echo "=== TEST DE CONNEXION PDO ===<br><br>";

require_once 'constants.php';

echo "Configuration:<br>";
echo "- User: " . DB_USER . "<br>";
echo "- Host: " . DB_SERVER . "<br>";
echo "- Database: " . DB_NAME . "<br>";
echo "- Port: " . DB_PORT . "<br><br>";

try {
    $dsn = "mysql:host=" . DB_SERVER . ";dbname=" . DB_NAME . ";port=" . DB_PORT . ";charset=utf8";
    echo "DSN: " . $dsn . "<br><br>";
    
    $pdo = new PDO($dsn, DB_USER, DB_PASSWORD, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
    ]);
    
    echo "✅ Connexion PDO réussie !<br>";
    
    // Test d'une requête simple
    $stmt = $pdo->query("SELECT COUNT(*) as total FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'projet_cir2'");
    $result = $stmt->fetch();
    echo "Nombre de tables dans la base: " . $result['total'] . "<br>";
    
} catch (PDOException $e) {
    echo "❌ Erreur PDO:<br>";
    echo "Message: " . $e->getMessage() . "<br>";
    echo "Code: " . $e->getCode() . "<br>";
    echo "Ligne: " . $e->getLine() . "<br>";
}