from http.server import BaseHTTPRequestHandler
from urllib import parse
import cgi
import io

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        ruta_analizada = parse.urlparse(self.path)
        partes_del_mensaje = [
            'Valores del cliente:',
            'Dirección={} ({})'.format(
                self.client_address,
                self.address_string()),
            'Comando={}'.format(self.command),
            'Ruta={}'.format(self.path),
            'Ruta real={}'.format(ruta_analizada.path),
            'Consulta={}'.format(ruta_analizada.query),
            'Version de petición={}'.format(self.request_version),
            '',
            'Valores del servidor:',
            'Versión del servidor={}'.format(self.server_version),
            'versión del sistema={}'.format(self.sys_version),
            'Versión del protocolo={}'.format(self.protocol_version),
            '',
            'Encabezados Recibidos:',
        ]
        for name, value in sorted(self.headers.items()):
            partes_del_mensaje.append(
                '{}={}'.format(name, value.rstrip())
            )
        partes_del_mensaje.append('')
        mensaje = '\r\n'.join(partes_del_mensaje)
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(mensaje.encode('utf-8'))
    def do_POST(self):
        # Analiza los datos publicados en el  formulario
        formulario = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'Método de solicitud': 'POST',
                'Tipo de contenido': self.headers['Content-Type'],
            }
        )

        # Begin the response
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()

        out = io.TextIOWrapper(
            self.wfile,
            encoding='utf-8',
            line_buffering=False,
            write_through=True,
        )

        out.write('Cliente: {}\n'.format(self.client_address))
        out.write('Agente - Usuario: {}\n'.format(
            self.headers['user-agent']))
        out.write('Ruta: {}\n'.format(self.path))
        out.write('Datos del formulario:\n')

        # Echo back information about what was posted in the formulario
        for campo in formulario.keys():
            elemento = formulario[campo]
            if elemento.filename:
                # Si el elemento es un archivo
                datosDelArchivo = elemento.file.read()
                longitud_archivo = len(datosDelArchivo)
                del datosDelArchivo
                out.write(
                    '\tPublicado {} como {!r} ({} bytes)\n'.format(
                        campo, elemento.filename, longitud_archivo)
                )
            else:
                # Valor de formulario regular
                out.write('\t{}={}\n'.format(
                    campo, formulario[campo].value))

        # Desconectar el wrapper
        out.detach()

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), Handler)
    print('Iniciando servidor, usar <Ctrl-C> para detener')
    server.serve_forever()