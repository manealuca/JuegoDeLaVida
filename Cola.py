class Cola:
    def __init__(self):
        self.__items = []

    def encolar(self,x):
        "Agrega un elemento a la cola"
        self.__items.append(x)
    
    def desencolar(self):
        "Elimina el primer elemto de la cola y devuelve su valor"
        try:
            return self.__items.pop(0)
        except:
            raise ValueError("La cola esta vacia")
    
    def es_vacia(self):
        "Devuelve True si esta vacia, si no devuelve False"
        return self.__items == []
    def mostrar_cola(self):
        for item in self.__items:
            print(item)