def listarUsuarios(usuarios):
    print("\nUsuarios: \n")

    contador=1
    for i in usuarios:
        datos="{0}. Código: {1} | Nombre: {2} | Apellido: {3} | Fecha Nacimiento: {4} | ID Ocupación: {5} | ID Genero: {6}"
        print(datos.format(contador,i[0],i[1],i[2],i[3],i[4],i[5]))
        contador+=1
    print(" \n")

def pedirDatosUsuario():
    nombreCorrecto = False
    while(not nombreCorrecto):
        nombre = input("Ingrese su nombre: ")
        if len(nombre) > 45 or len(nombre) == 0:
            print("Nombre incorrecto: Ha de tener de 1 a 45 caracteres...")
        else:
            nombreCorrecto = True

    apellidoCorrecto = False
    while(not apellidoCorrecto):
        apellido = input("Ingrese su apellido: ")
        if len(apellido) > 45 or len(apellido) == 0:
            print("Apellido incorrecto: Ha de tener de 1 a 45 caracteres...")
        else:
            apellidoCorrecto = True
    fNacimiento = input("Ingrese su fecha de nacimiento 'YYYY-MM-DD': ")

    ocupacionCorrecto = False
    while(not ocupacionCorrecto):
        idOcupacion = input("Ingrese su código de ocupación: ")
        if idOcupacion.isnumeric():
            if (int(idOcupacion) > 0):
                ocupacionCorrecto = True
                idOcupacion = int(idOcupacion)
            else:
                print("Id incorrecto: Ingrese un número correcto o distinto de 0...")
        else:
            print("Id incorrecto: Debe ser un número correcto...")
    
    generoCorrecto = False
    while(not generoCorrecto):
        idGenero = input("Ingrese su código de género: ")
        if idGenero.isnumeric():
            if (int(idGenero) > 0):
                generoCorrecto = True
                idGenero = int(idGenero)
            else:
                print("Id incorrecto: Ingrese un número correcto o distinto de 0...")
        else:
            print("Id incorrecto: Debe ser un número...")

    usuario=(nombre,apellido,fNacimiento,idOcupacion,idGenero)
    return usuario

def pedirDatosActualizacion(usuarios):
    listarUsuarios(usuarios)
    existeCodigo = False

    idCorrecto = False
    while(not idCorrecto):
        codigoEditar=input("Ingrese el codigo a actualizar: ")
        if codigoEditar.isnumeric():
            if (int(codigoEditar) > 0):
                idCorrecto = True
                codigoEditar = int(codigoEditar)
            else:
                print("Id incorrecto: Ingrese un número correcto o distinto de 0...")
        else:
            print("Id incorrecto: Debe ser un número...")

    for i in usuarios:
        if i[0] == int(codigoEditar):
            existeCodigo = True
            break

    if existeCodigo:
        nombreCorrecto = False
        while(not nombreCorrecto):
            nombre = input("Ingrese su nombre: ")
            if len(nombre) > 45 or len(nombre) == 0:
                print("Nombre incorrecto: Ha de tener de 1 a 45 caracteres...")
            else:
                nombreCorrecto = True

        apellidoCorrecto = False
        while(not apellidoCorrecto):
            apellido = input("Ingrese su apellido: ")
            if len(apellido) > 45 or len(apellido) == 0:
                print("Apellido incorrecto: Ha de tener de 1 a 45 caracteres...")
            else:
                apellidoCorrecto = True
        fNacimiento = input("Ingrese su fecha de nacimiento 'YYYY-MM-DD': ")

        ocupacionCorrecto = False
        while(not ocupacionCorrecto):
            idOcupacion = input("Ingrese su código de ocupación: ")
            if idOcupacion.isnumeric():
                if (int(idOcupacion) > 0):
                    ocupacionCorrecto = True
                    idOcupacion = int(idOcupacion)
                else:
                    print("Id incorrecto: Ingrese un número correcto o distinto de 0...")
            else:
                print("Id incorrecto: Debe ser un número correcto...")
        
        generoCorrecto = False
        while(not generoCorrecto):
            idGenero = input("Ingrese su código de género: ")
            if idGenero.isnumeric():
                if (int(idGenero) > 0):
                    generoCorrecto = True
                    idGenero = int(idGenero)
                else:
                    print("Id incorrecto: Ingrese un número correcto o distinto de 0...")
            else:
                print("Id incorrecto: Debe ser un número...")

        usuario=(nombre,apellido,fNacimiento,idOcupacion,idGenero,codigoEditar)
    else:
        usuario = None

    return usuario

def pedirDatosEliminacion(usuarios):
    listarUsuarios(usuarios)
    existeCodigo = False

    codigoEliminar=input("Ingrese el codigo a eliminar: ")
    for i in usuarios:
        if i[0] == int(codigoEliminar):
            existeCodigo = True
            break
    if not existeCodigo:
        codigoEliminar=""

    return codigoEliminar
