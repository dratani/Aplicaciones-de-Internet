use Frontier::Client;

# Make an object to represent the XML-RPC server.
$server_url = 'http://localhost:8000/RPC2';
$server = Frontier::Client->new(url => $server_url);

# Call the remote server and get our result.
$result = $server->call('add', 5, 3);
$sum = $result;

print "Sum: $sum\n";