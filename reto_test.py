# Ejercicio 1. Contar caracteres
def contar_caracteres(lista):
  contador = 0
  for letra in lista:
    contador += 1
  return contador

cadena1 = "¡Hola alumnos! Bienvenidos a clase"
cadena2 = 3
print(contar_caracteres(cadena1))
# print(contar_caracteres(cadena2))

# Ejercicio 2. Calcular promedio
def calcular_promedio(lista_numeros):
  promedio = float((sum(lista_numeros)) / len(lista_numeros))
  return promedio 

numeros1 = [1, 2, 3, 4, 5]
numeros2 = []
print(calcular_promedio(numeros1))
# print(calcular_promedio(numeros2))

# Ejercicio 3. Encontrar duplicado
def encontrar_duplicado(numeros):
  duplicados = []
  lista = []
  for numero in numeros:
    if numero in lista:
      duplicados.append(numero)
    else:
      lista.append(numero)
  return duplicados

numeros1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3]
numeros2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(encontrar_duplicado(numeros1))
print(encontrar_duplicado(numeros2))

# Ejercicio 4. Enmascarado datos
def enmascarado_datos(cadena):
  cadena_datos = str(cadena)
  return '#' * (len(cadena_datos) - 4) + cadena_datos[-4:]

contraseña1 = "Micontraseña1234"
contraseña2 = 123456789
print(enmascarado_datos(contraseña1))
print(enmascarado_datos(contraseña2))

#Ejercicio 5. Es anagrama
def es_anagrama(palabra1, palabra2):
  palabra_ordenada_1 = sorted(palabra1.lower())
  palabra_ordenada_2 = sorted(palabra2.lower())
  if palabra_ordenada_1 == palabra_ordenada_2:
    return True
  else:
    return False

palabra1 = "Roma"
palabra2 = "lana"
palabra3 = " hola"
palabra4 = "amor"

print(es_anagrama(palabra1,palabra2))
print(es_anagrama(palabra1,palabra3))
print(es_anagrama(palabra2,palabra4))
print(es_anagrama(palabra1,palabra4))

# Ejercicio 6. Buscar nombre

#def buscar_nombre():
    # lista_nombres = input("Introduzca una lista de nombres: ")
    # nombre_buscado = input("Introduzca el nombre que quiere buscar en la lista: ")
    # if nombre_buscado in lista_nombres:
    #     print(f"¡El nombre {nombre_buscado} fue encontrado con éxito!")
    # else:
    #     print("No se encontró el nombre en la lista")
# buscar_nombre()

# Ejercicio 7. Fibonacci
def fibonacci(numero):
  if numero == 1 or numero == 2:
        return 1
  else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)
print(fibonacci(10))

# Ejercicio 8. Encontrar puesto empleado

def encontrar_puesto_empleado(nombre_completo, lista_empleados):
   try:
    nombre, apellido = nombre_completo.split()
   except:
        return f"{nombre_completo} no trabaja aquí"
   for elemento in lista_empleados: # elemento es cada diccionario dentro de la lista
      if nombre == elemento["nombre"] and apellido == elemento["apellido"]:
         return elemento["puesto"]
      
   return (f"{nombre_completo} no trabaja aquí")

empleados = [{'nombre': "Juan", 'apellido': "García", 'puesto': "Secretario"},
{'nombre': "Mabel", 'apellido': "García", 'puesto': "Product Manager"},
{'nombre': "Isabel", 'apellido': "Martín", 'puesto': "CEO"}]

print(encontrar_puesto_empleado("Juan García", empleados))
print(encontrar_puesto_empleado("Mabel García", empleados))
print(encontrar_puesto_empleado("Isabel Martín", empleados))
print(encontrar_puesto_empleado("Alejandro Martín", empleados))

# Ejercicio 9. Cubo número
cubo_numero = lambda x:x**3
print(cubo_numero(3))

# Ejercicio 10. Resto divisón
resto_division = lambda x,y: x%y
print(resto_division(10,2))

# Ejercicio 11. Números pares
lista_numeros =[24, 56, 2.3, 19, -1, 0]
numeros_pares = list(filter(lambda numero:numero%2 == 0, lista_numeros))
print(numeros_pares)

# Ejercicio 12. Suma números

numeros_suma = list(map(lambda x:x+3, lista_numeros))
print(numeros_suma)

# Ejercicio 13. Sumar listas
lista_numeros_1 = [1, 4, 5, 6 , 7 , 7]
lista_numeros_2 = [3, 11, 34, 56]
sumar_listas = lambda lista1,lista2: lista1 + lista2 #lambda lista1, lista2: [x + y for x,y in zip(lista1, lista2)]
print(sumar_listas(lista_numeros_1, lista_numeros_2))

# Ejercicio 14. No te vayas por las ramas
class Arbol():
   def __init__(self):
      self.tronco = 1
      self.ramas = []

   def crecer_tronco(self):
    self.tronco += 1

   def nueva_rama(self):
      self.ramas.append(1)

   def crecer_ramas(self):
      self.ramas = [rama + 1 for rama in self.ramas]

   def quitar_rama(self, n):
      if n <= 0 or n>len(self.ramas):
         print(f"No se eliminó ninguna rama")
      else:
         del self.ramas[n]

   def info_arbol(self):
    if len(self.ramas) == 0:
                return f"El árbol tiene una longitud de {self.altura_tronco} y no tiene ninguna rama"
    else:
      info_ramas = [f"rama_{i + 1}: {longitud}" for i, longitud in enumerate(self.ramas)]
      return print(f"El árbol tiene una longitud de {self.tronco}, tiene {len(self.ramas)} ramas, con las siguientes longitudes: {', '.join(info_ramas)}")

arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)
arbol.info_arbol()


# Ejercicio 15. Usuario banco

class UsuarioBanco():
   def __init__(self, nombre, saldo, cuenta_corriente=False):
      self.nombre = nombre
      self.saldo = saldo
      self.cuenta_corriente = cuenta_corriente
   def retirar_dinero(self):
    dinero = int(input("Ingrese el dinero que desea sacar: "))
    if dinero > self.saldo:
      print("Error. No hay suficiente saldo")
    else:
      self.saldo -= dinero
      print(f"El usuario {self.nombre} tiene el siguiente saldo: {self.saldo} €")
      print("\n")
   
   def transferir_dinero(self, otro_usuario, dinero_transferido):
    if not otro_usuario.cuenta_corriente:
        ValueError(f"{otro_usuario.nombre}no tiene cuenta corriente")
    if dinero_transferido > otro_usuario.saldo:
        ValueError (f"{otro_usuario.nombre} no tiene sufucuente saldo")
    self.saldo += dinero_transferido
    otro_usuario.saldo -= dinero_transferido
    print(f"El usuario {self.nombre} tiene el siguiente saldo: {self.saldo} €. Y el usuario {otro_usuario.nombre} tiene el siguiente saldo: {otro_usuario.saldo}")

   def agregar_dinero(self, dinero):
      self.saldo += dinero 
      print(f"El saldo actual de {self.nombre} es {self.saldo}")

usuario1= UsuarioBanco("Alicia", 100, cuenta_corriente=True)
usuario2= UsuarioBanco("Bob", 50, cuenta_corriente=True)

# usuario1.agregar_dinero(20)
# usuario2.transferir_dinero(usuario1, 80)
# usuario1.retirar_dinero()

# Ejercicio 16. Procesar texto

def contar_palabras(texto):
   palabras_contadas = {}
   palabras = texto.lower().split()
   for palabra in palabras: 
      palabras_contadas[palabra] = palabras_contadas.get(palabra, 0) + 1
   return palabras_contadas

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
  resultado = []
  palabras = texto.lower().split()
  for palabra in palabras:
     if palabra == palabra_original:
        resultado.append(palabra_nueva)
     else:
        resultado.append(palabra)
  return ' '.join(resultado) # esto tiene que ver con el split creo

def eliminar_palabra(texto, palabra_eliminada):
  resultado = []
  palabras = texto.lower().split()
  for palabra in palabras:
     if palabra != palabra_eliminada:
        resultado.append(palabra)
  return ' '.join(resultado)


def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError(f"Se esperan dos argumentos para reemplazar. Argumentos pasados: {len(args)}")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError(f"Se espera un argumento para eliminar. Argumentos pasados: {len(args)}")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError(f"Opción no válida")

texto1 = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."
conteo_palabras = procesar_texto(texto1, "contar")
print(conteo_palabras)
reemplazo = procesar_texto(texto1, "reemplazar", "texto", "relato")
print(reemplazo)
eliminacion = procesar_texto(texto1, "eliminar", "ejemplo")
print(eliminacion)
