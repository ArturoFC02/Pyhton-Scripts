from datetime import date
from datetime import datetime
import statistics

Edades=[] #Listas auxiliares
lista=list()

#Definimos la función para calcular la edad a partir de la fecha de nacimiento
def calcular_edad(fecha):
    fecha_actual=date.today()
    fecha_nacimiento= datetime.strptime(fecha, "%Y, %m, %d")
    edad = fecha_actual.year- fecha_nacimiento.year
    edad -= ((fecha_actual.month, fecha_actual.day) < ( fecha_nacimiento.month,  fecha_nacimiento.day))
    return edad
    
    
class Contacto:
    def __init__(self, name, number, birthdate):
        self.name = name
        self.number = number
        
        #Calculamos la edad a partir de la fecha de nacimiento introducida
        self.age= calcular_edad(birthdate)
        
        Edades.append(self.age) #Creamos la lista de todas las edades
        lista.append(self) #Creamos una lista con todos las instancias
        
    def __str__(self):
        return f'El nombre del contacto es {self.name}. El número del contacto es {self.number}. La edad del contacto es {self.age}'
        
        
        
class Agenda(Contacto):
    @classmethod 
    def edad_prom(self):
        print(statistics.mean(Edades))
    
    @classmethod
    def contacto_mayor(self):
        maximo= max(Edades)
        for n in lista: 
            if n.age==maximo:
                print(n)
                break
    
    @classmethod
    def contacto_menor(self):
        minimo= min(Edades)
        for n in lista: 
            if n.age==minimo:
                print(n)
                break 
    
    @classmethod
    def busqueda_nombre(self,nombre):
        for n in lista:
            if n.name == nombre:
                print(n)
                break
        else:
            print('Dicho nombre no se encuentra registrado en la agenda. ')
            
    @classmethod
    def busqueda_numero(self,numero):
        for n in lista:
            if n.number == numero:
                print(n)
                break
        else:
            print('Dicho número no se encuentra registrado en la agenda. ')
    
    @classmethod 
    def nuevo_contacto(self):
        name= input('Ingresa el nombre del nuevo contacto.  ') 
        number = input('Ingresa el número del contacto.  ') 
        birthdate = input('Ingresa la fecha de nacimeinto del contacto. (YYYY, M, D)  ')
        
        contact=Contacto(name, number, birthdate)
     
    @classmethod
    def borrar_contacto(self):
        nombre=input('Ingresa el nombre del contacto a borrar  ')
        for n in lista:
            if n.name == nombre :
                lista.remove(n)
                del n
                break
        else:
            print('Dicho nombre no se encuentra registrado en la agenda. ')
        
        
    @classmethod 
    def mostrar_agenda(self):
        for n in lista:
            print(n)
            
    @classmethod
    def actualizacion_contacto(self):
        nombre=input('Ingresa el nombre del contacto a modificar  ')
        
        for n in lista: 
            if n.name == nombre:               
                print('¿Qué deseas hacer?')
                print('1. Nombre')
                print('2. Número')
                print('3. Fecha de nacimiento')
                op= int(input('Digita la opción deseada.  '))
                
                if op == 1 : 
                    n.name= input('Nuevo nombre:  ')
                elif op == 2: 
                    n.number= input('Nuevo número:  ')
                elif op==3 : 
                    birthdate= input('Nueva fecha de nacimiento  ')
                    n.age=calcular_edad(birthdate)
                else:
                    print('Número fuera de rango')
                    
                break
                
        else:
            print('Dicho nombre no se encuentra registrado en la agenda. ')
       
        
    @classmethod
    def menu(self):
        print('Menú')
        print('1. edad_prom() \n Calcula la edad promedio de entre todos los contactos existentes en la agenda.')
        print('2. contacto_mayor() \n Regresa el los datos del contacto con mayor edad de entre todos los existentes en la agenda. ')
        print('3. contacto_menor() \n Regresa el los datos del contacto con menor edad de entre todos los existentes en la agenda. ')
        print('4. busqueda_nombre() \n Recibe un nombre y de existir dicho nombre en la agenda, regresa el contacto asociado. ')
        print('5. busqueda_numero() \n Recibe un número y de existir dicho número en la agenda, regresa el contacto asociado.')
        print('6. nuevo_contacto() \n Recibe los datos necesarios para crear un nuevo contacto en la agenda. ')
        print('7. borrar_contacto() \n Recibe el nombre de un contacto y de existir en la agenda, lo elimina. ')
        print('8. mostrar_agenda() \n Muestra los datos de todos los contactos existentes en la agenda.  ')
        print('9.actualizacion_contacto() \n Recibe un nombre, de estar registrado en la agenda, pide información acerca de la actualización de los datos. ')
        

C1=Contacto('José', 32, "2002, 8, 9")
C2=Contacto('Sofia', 55, "2020, 8, 8")
C3= Contacto('Luis', 66, '2010, 8, 10')
C4= Contacto('Daniela', 54, '1900, 11, 18')
    
Agenda.edad_prom()
Agenda.contacto_mayor()
Agenda.contacto_menor()
Agenda.busqueda_nombre('Daniela')
Agenda.busqueda_numero(66)
Agenda.nuevo_contacto()
Agenda.borrar_contacto()

Agenda.actualizacion_contacto()

Agenda.mostrar_agenda()