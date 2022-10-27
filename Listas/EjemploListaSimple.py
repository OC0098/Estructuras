# En la siguiente apartado veremos como crear una lista simple para almacenamiento dinámico de datos. 
# Para crear una lista simple necesitamos contar con las siguientes clases:
#   OBJETO (ESPECIAL/NO IMPRENSINDIBLE)
#   NODO
#   LISTA
# Tendrán los siguientes métodos
#   AGREGAR (INICIO Y FINAL)
#   ELIMINAR
#   RECORRER (MOSTRAR LISTA)
#   OBTENER
#   VACIA
#   

'''
La clase estudiante será el modelo del objeto que estaremos almacenando en nuestra lista.
Contará con atributos como:
-> Identificador
-> Nombre
-> Apellido
-> Edad
'''
class Estudiante:
    def __init__(self, id:int, nombre:str, apellido:str, edad:int) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self) -> str:
        return "ID: {} | Nombre: {} | Apellido: {} | Edad: {}".format(str(self.id), self.nombre, self.apellido, str(self.edad))

'''
La clase nodo será la clase que se estará almacenando los atributos necesarios para 
el manejo de la lista simple. 
-> Estudiante
-> Siguiente
'''
class Nodo:
    def __init__(self, estudiante:Estudiante) -> None:
        self.estudiante = estudiante
        self.siguiente = None

'''
La clase Lista es dónde iremos guardando los datos, de la misma manera tendremos los
métodos para recorrer dentro de esta clase.
-> Inicio
-> Tamaño
'''
class Lista:
    def __init__(self) -> None:
        self.inicio = None # Este guardará el primer nodo en la lista. Es de tipo Nodo.
        self.tamanio = 0 # Indicamos que al crear la lista está no tendrá datos guardados.

    # Indica si la lista se encuentra vacía 
    def vacia(self) -> bool:
        return self.tamanio == 0

    # El siguiente método agrega un nodo nuevo con un estudiante al inicio de la lista
    # parámetro: estudiante:Estudiante
    def agregarAlInicio(self, estudiante:Estudiante) -> None:
        # Creamos el objeto nodo con el estudiante que se agregará
        nuevo_nodo = Nodo(estudiante)
        if self.vacia():
            self.inicio = nuevo_nodo
        else:
            # Tomamos el valor que se encuentra al inicio
            nodo_temp = self.inicio
            # Asignamos al inicio su nuevo valor (el valor que estará en frente de la lista)
            self.inicio = nuevo_nodo
            # El siguiente del frente será lo que teníamos ya guardado
            nuevo_nodo.siguiente = nodo_temp
        self.tamanio += 1
    
    # El siguiente método agrega un nodo nuevo con un estudiante al final de la lista.
    # parámetro: estudiante:Estudiante
    def agregarAlFinal(self, estudiante:Estudiante) -> None:
        nuevo_nodo = Nodo(estudiante)
        if self.vacia():
            self.inicio = nuevo_nodo
        else:
            # Tomamos el nodo que está al inicio
            nodo_temp = self.inicio
            # Recorremos los nodos hasta que el siguiente sea un None o nulo.
            while nodo_temp.siguiente is not None:
                # Asignamos a nuestro nodo temporal el siguiente
                nodo_temp = nodo_temp.siguiente
            # Una vez salga del ciclo estaremos en la última posición de nuestros nodos, solamente agregamos
            nodo_temp.siguiente = nuevo_nodo
        self.tamanio += 1

    # Este es el método eliminar de la lista. Elimina mediante un número de identificador
    def eliminar(self, identificador:int) -> Estudiante | None:
        # Validamos primeramente que si halla al menos un elemento en la lista para realizar el recorrido
        if not self.vacia():
            # Asignamos el elemento del inicio
            nodo_actual = self.inicio
            nodo_anterior = None
            while nodo_actual is not None:
                # Si el nodo actual es el que buscamos tendremos dos casos
                if nodo_actual.estudiante.id == identificador:
                    # Nodo actual es igual al inicio
                    if nodo_actual == self.inicio:
                        # El nuevo inicio será el siguiente del inicio
                        self.inicio = nodo_actual.siguiente
                        self.tamanio -= 1
                        return nodo_actual.estudiante
                    # En caso que no sea el nodo del inicio
                    else:
                        # El nodo anterior su siguiente sera el siguiente del actual
                        nodo_anterior.siguiente = nodo_actual.siguiente
                        self.tamanio -= 1
                        return nodo_actual.estudiante
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.siguiente
        return None

    # Este metodo nos permite ver los datos de la lista por medio de la consola
    def cmd_mostrar_lista(self) -> None:
        if self.vacia(): # Validamos si la lista está vacia
            print('La lista se encuentra actualmente vacía.')
        else:
            nodo_actual = self.inicio
            while nodo_actual is not None:
                print(nodo_actual.estudiante)
                nodo_actual = nodo_actual.siguiente

    # Este metodo nos permite obtener la información de un estudiante sin eliminarlo de la lista
    def obtener_estudiante(self, identificador) -> Estudiante | None:
        if not self.vacia():
            nodo_actual = self.inicio
            while nodo_actual is not None:
                if nodo_actual.estudiante.id == identificador:
                    return nodo_actual.estudiante
                nodo_actual = nodo_actual.siguiente
        return None


# Creamos los estudiantes
e1 = Estudiante(1, "Oscar", "Calderón", 24)
e2 = Estudiante(2, "Lesly", "Tzóc", 24)
e3 = Estudiante(3, "Lilian", "Soto", 18)

# Creamos la lista
lista_estudiantes = Lista()

# Mostramos que la lista está vacía
lista_estudiantes.cmd_mostrar_lista()

print('\nIngresamos los datos ahora...\n')

# Agregamos estudiantes a la lista
lista_estudiantes.agregarAlFinal(e1)
lista_estudiantes.agregarAlInicio(e2)
lista_estudiantes.agregarAlFinal(e3)

# Mostramos la lista
lista_estudiantes.cmd_mostrar_lista()

print('\nEliminamos al estudiante con el ID 1\n')
# Eliminamos a un estudiante
estudiante = lista_estudiantes.eliminar(1) # "estudiante =" es opcional, por si en caso usaremos el dato que se eliminará.

print('\nEl usuario que ha sido eliminado es: {}\n'.format(estudiante.nombre))

# Mostramos la lista final
lista_estudiantes.cmd_mostrar_lista()

# Obtener un usuario sin eliminar
estudiante_obtenido = lista_estudiantes.obtener_estudiante(3)

print('\nEl estudiante buscado es: {}\n'.format(estudiante_obtenido.nombre))

# Mostramos que la lista sigue igual
lista_estudiantes.cmd_mostrar_lista()


