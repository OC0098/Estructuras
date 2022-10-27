'''
En este apartado tendremos un ejemplo para una lista doblemente enlazada.
La lista esta compuesta por las siguientes clases:
    -> NODO
    -> ESTUDIANTE
    -> LISTA
Las acciones que se podrán hacer en la lista:
    -> Agregar (inicio o fin)
    -> Recorrer (mostrar por consola)
    -> Eliminar
    -> Obtener
'''

# Clase de Estudiante. Plantilla para los datos de tipo Estudiante
class Estudiante:

    # Constructor de la clase    
    def __init__(self, id:int, nombre:str, apellido:str, edad:int) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    # Método STR del objeto Estudiante.
    def __str__(self) -> str:
        return "ID: {} | Nombre: {} | Apellido: {} | Edad: {}".format(str(self.id), self.nombre, self.apellido, str(self.edad))
    

# Clase nodo, es la que nos ayudará a manejar los punteros y datos.
class Nodo:

    # Constructor
    def __init__(self, estudiante:Estudiante) -> None:
        self.siguiente = None
        self.anterior = None
        self.estudiante = estudiante


# Clase Lista, es donde almacenaremos los nodos y tendremos nuestro metodos
# Para una lista doble tenemos diferentes opciones. Ya sea usando solamente 
# el inicio, o usando un inicio y fin. Esté ejemplo usará el inicio y fin
class ListaDoble:

    # constructor
    def __init__(self) -> None:
        self.inicio = None
        self.fin = None
        self.tamanio = 0

    # Método que nos permite ver si la lista está vacía o llena.
    def vacia(self) -> bool:
        return self.tamanio == 0

    # Método que nos permite agregar un nuevo elemento a la lista, se inserta al inicio
    def agregarAlInicio(self, estudiante:Estudiante) -> None:
        nuevo_nodo = Nodo(estudiante)
        if self.vacia():
            self.inicio = nuevo_nodo
            self.fin = self.inicio
        else:
            nodo_tmp = self.inicio
            nodo_tmp.anterior = nuevo_nodo
            nuevo_nodo.siguiente = nodo_tmp
            self.inicio = nuevo_nodo
        self.tamanio += 1
    
    # Método para agregar un nuevo elemento a la lista, se inserta al final
    def agregarAlFinal(self, estudiante:Estudiante) -> None:
        nuevo_nodo = Nodo(estudiante)
        if self.vacia():
            self.inicio = self.fin = nuevo_nodo
        else:
            nodo_tmp = self.fin
            nodo_tmp.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nodo_tmp
            self.fin = nuevo_nodo
        self.tamanio += 1
    
    # Método para Eliminar un estudiante de la lista
    def eliminar(self, identificador:int) -> Estudiante | None:
        if not self.vacia():
            nodo_actual = self.inicio
            while nodo_actual is not None:
                # Para la eliminación podemos tener 3 posibles casos
                if nodo_actual.estudiante.id == identificador:
                    # Caso 1: El nodo es el inicio
                    if nodo_actual == self.inicio:
                        nodo_actual.siguiente.anterior = None
                        self.inicio = nodo_actual.siguiente
                        self.tamanio -= 1
                        return nodo_actual.estudiante
                    # Caso 2: el nodo es el final
                    elif nodo_actual == self.fin:
                        nodo_actual.anterior.siguiente = None
                        self.fin = nodo_actual.anterior
                        self.tamanio -= 1
                        return nodo_actual.estudiante
                    # Caso 3: no es inicio ni fin
                    else:
                        nodo_temp = nodo_actual
                        nodo_actual.anterior.siguiente = nodo_temp.siguiente
                        nodo_actual.siguiente.anterior = nodo_temp.anterior
                        self.tamanio -= 1
                        return nodo_actual.estudiante                    
                nodo_actual = nodo_actual.siguiente
        return None
    
    # Metodo para obtener un estudiante sin eliminarlo
    def obtener_estudiante(self, identificador:int) -> Estudiante | None:
        if not self.vacia():
            nodo_actual = self.inicio
            while nodo_actual is not None:
                if nodo_actual.estudiante.id == identificador:
                    return nodo_actual.estudiante
                nodo_actual = nodo_actual.siguiente
        return None

    # Método para recorrer la lista
    def cmd_mostrar_lista(self) -> None:
        if self.vacia():
            print('La lista se encuentra actualmente vacía.')
        else:
            nodo_actual = self.inicio
            while nodo_actual is not None:
                print(nodo_actual.estudiante)
                nodo_actual = nodo_actual.siguiente
    

# Creamos los estudiantes
e1 = Estudiante(1, "Oscar", "Calderón", 24)
e2 = Estudiante(2, "Lesly", "Tzóc", 24)
e3 = Estudiante(3, "Lilian", "Soto", 18)

# Instanciamos la lista
lista_estudiantes = ListaDoble()

# Mostramos que la lista está vacia
lista_estudiantes.cmd_mostrar_lista()

print('\nAhora agregaremos datos a la lista...\n')

# Agreamos los estudiantes
lista_estudiantes.agregarAlInicio(e1)
lista_estudiantes.agregarAlFinal(e2)
lista_estudiantes.agregarAlInicio(e3)

# Mostramos la lista
lista_estudiantes.cmd_mostrar_lista()

print('\nVamos a eliminar datos...\nEl estudiante eliminado es: {}\n'.format(lista_estudiantes.eliminar(1)))

lista_estudiantes.cmd_mostrar_lista()
print('\nVamos a buscar un estudiante ahora...\nEl estudiante búscado es: {}\n'.format(lista_estudiantes.obtener_estudiante(3)))

lista_estudiantes.cmd_mostrar_lista()