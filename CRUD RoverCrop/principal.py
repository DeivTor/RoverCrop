from BD.Conexion import DAO
import funciones

def menuPrincipal():
    flag=True
    while(flag):
        opcionCorrecta=False
        while(not opcionCorrecta):
            print("\n=========== MENÚ PRINCIPAL ===========")
            print("1- Listar usuarios")
            print("2- Registrar usuario")
            print("3- Actualizar usuario")
            print("4- Eliminar usuario")
            print("5- Salir")
            print("========================================")
            opcion = int(input("\nSeleccione una opción: "))
            print("")

            if opcion < 1 or opcion > 5:
                print("\nOpción incorrecta, ingrese otra opción: ")
            elif opcion == 5:
                flag=False
                print("Gracias por usar este sistema")
                break
            else:
                opcionCorrecta=True
                ejecutarOpcion(opcion)
            
def ejecutarOpcion (opcion):
    dao = DAO()

    if opcion == 1:
        try:
            usuarios = dao.listarUsuarios()
            if len(usuarios)> 0:
                funciones.listarUsuarios(usuarios)
            else:
                print("No se encontraron usuarios...")
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        usuario = funciones.pedirDatosUsuario()
        try:
            dao.registrarUsuario(usuario)
        except:
            print("Ocurrió un error...")
    elif opcion == 3:
        print("Actualización")
        try:
            usuarios = dao.listarUsuarios()
            if len(usuarios)> 0:
                usuario = funciones.pedirDatosActualizacion(usuarios)
                if usuario:
                    dao.actualizarUsuario(usuario)
                else:
                    print("Código de usuario no encontrado\n")
            else:
                print("No se encontraron usuarios...")
        except:
            print("Ocurrió un error...")
    elif opcion == 4:
        print("Eliminación")
        try:
            usuarios = dao.listarUsuarios()
            if len(usuarios)> 0:
                codigoEliminar = funciones.pedirDatosEliminacion(usuarios)
                if not(codigoEliminar == ""):
                    dao.eliminarUsuario(codigoEliminar)
                else:
                    print("Código no encontrado...\n")
            else:
                print("No se encontraron usuarios...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida")

menuPrincipal()