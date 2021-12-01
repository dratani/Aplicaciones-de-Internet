use strict;
use warnings FATAL => 'all';
use warnings;
use Frontier::Client;

# Crear un objeto para representar el servidor XML-RPC
$server_url = 'http://localhost:8000/RPC2';
$server = Frontier::Client->new(url => $server_url);

# Llamar al servidor remoto e imprimir los resultados
$result = $server->call('add', 5, 3);
$sum = $result;

print "Sum: $sum\n";