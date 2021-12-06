# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import saludos_pb2
import saludos_pb2_grpc


def RPCSimple(stub):
    response = stub.DecirHola(saludos_pb2.SolicitudSaludo(nombre='Tani'))
    print("Respuesta de saludo recibida: " + response.saludo)


def generarSaludosIterator():
    listaDeAmigos = ["Juan Carlos", "Lupita", "Gabriela", "Nayeli", "Angel"]
    for item in listaDeAmigos:
        saludo = saludos_pb2.SolicitudSaludo(nombre=item)
        yield saludo

def RPCResponseStream (stub):
    listaDeAmigos = ["Juan Carlos", "Lupita", "Gabriela", "Nayeli", "Angel"]
    for respuesta in stub.HolaEnVariosIdiomas(saludos_pb2.SolicitudSaludo(nombre='Tani')):
        print("Respuesta stream:" + respuesta.saludo)

def RPCRequestStream(stub):
    response = stub.SaludaAMisAmigos(generarSaludosIterator())
    print("Petición stream, total de mensajes recibidos: " + str(response.contador_nombres)
                                 + " Mensaje concatenado: " + response.saludo)
def RPCBidireccional(stub):
    for respuesta in stub.SaludaAMisAmigosEnVariosIdiomas (generarSaludosIterator()):
        print("Respuesta bidireccional:" + respuesta.saludo)
def run():

    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = saludos_pb2_grpc.SaludosStub(channel)

        #LLamada a RPC simple
        RPCSimple(stub)
        #Llamada a RCP con respuesta tipo transmisión
        RPCResponseStream(stub)
        #Llamada a RPC con solicitud tipo transmisión
        RPCRequestStream(stub)
        #Llamada a RPC con solicitud y respuesta de tipo transmisión (bidireccional)
        RPCBidireccional(stub)



if __name__ == '__main__':
    logging.basicConfig()
    run()
