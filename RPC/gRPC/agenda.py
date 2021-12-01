import agenda_pb2
import sys


def datosParaAgenda(Persona):
    Persona.id = int(input("Introduce el número ID de la persona:"))
    Persona.nombre = input("Introduce el nombre:")
    email = input("Introduce el email de la persona (en blanco para ninguno):")
    if email != "":
        Persona.email = email
    while True:
        numero = input("Introduce un número telefónico (o dejar en blanco para finalizar):")
        if numero == "":
            break
        numeroTelefonico = Persona.telefonos.add()
        numeroTelefonico.numero = numero

        tipo = input("Es un teléfono movil, de casa o de trabajo?")
        if tipo == "movil":
            numeroTelefonico.tipo = agenda_pb2.Persona.TipoDeTelefono.Value('MOVIL')
        elif tipo == "casa":
            numeroTelefonico.tipo = agenda_pb2.Persona.TipoDeTelefono.Value('CASA')
        elif tipo == "trabajo":
            numeroTelefonico.tipo = agenda_pb2.Persona.TipoDeTelefono.Value('TRABAJO')
        else:
            print("Tipo de teléfono desconocido, se establece el valor por defecto")

def listaDePersonas (agenda):
    for Persona in agenda.alguien:
        print("Id de Persona:",Persona.id)
        print("Nombre:",Persona.nombre)
        if Persona.HasField('email'):
            print("Email:",Persona.email)

        for numeroDeTelefono in Persona.telefonos:
            if numeroDeTelefono.tipo == agenda_pb2.Persona.TipoDeTelefono.Value('MOVIL'):
                print("Teléfono móvil:")
            elif numeroDeTelefono.tipo == agenda_pb2.Persona.TipoDeTelefono.Value('CASA'):
                print("Teléfono casa:")
            elif numeroDeTelefono.tipo == agenda_pb2.Persona.TipoDeTelefono.Value('TRABAJO'):
                print("Teléfono trabajo:")
            print(numeroDeTelefono.numero)

agenda = agenda_pb2.Agenda()

try:
     f = open("agenda.txt", "rb")
     agenda.ParseFromString(f.read())
     f.close()
except IOError:
    print("Error en el archivo")

datosParaAgenda(agenda.alguien.add())

f = open("agenda.txt", "wb")
f.write(agenda.SerializeToString())
f.close()

listaDePersonas(agenda)
