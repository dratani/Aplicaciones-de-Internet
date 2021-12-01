from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restringir a una ruta específica
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Crea el servidor RPC
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Regista la función pow(); usa el valor de
    # pow.__name__ como el nombre, que es  'pow'.
    server.register_function(pow)

    # Registra la función con un nombre diferente
    def adder_function(x, y):
        return x + y
    server.register_function(adder_function, 'add')

    # Register an instance; all the methods of the instance are
    # published as XML-RPC methods (in this case, just 'mul').
    class MyFuncs:
        def mul(self, x, y):
            return x * y

        def show_type(self, arg):
            """Illustrates how types are passed in and out of
            server methods.

            Accepts one argument of any type.

            Returns a tuple with string representation of the value,
            the name of the type, and the value itself.

            """
            return (str(arg), str(type(arg)), arg)

    server.register_instance(MyFuncs())

    # Run the server's main loop
    server.serve_forever()