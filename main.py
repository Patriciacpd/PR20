import requests
from alimento import Alimento
from bebida import Bebida
from combo import Combo
from crucero import Crucero
import string
from cliente import Cliente
from premium import Premium
from sencilla import Sencilla
from vip import Vip
from tour import Tour
ocupada={}
from datetime import datetime

def api():
    url="https://saman-caribbean.vercel.app/api/cruise-ships"
    result=requests.request("GET",url)
    return result.json()


"""************** RESTAURANTE **********************************"""
def entrar_barco(cruceros):
    

    while True:
        try:
            print("\n Bienvenido, estos son los cruceros: ")
            for cruce in cruceros:
                print(f"\n ({cruceros.index(cruce)+1}) {cruce.name}")
            option=int(input("\n Seleccione según el barco al cual desea acceder a su restaurante: \n(5)Para salir"))
            if option==1:
                menu=[]
                crucero=cruceros[option-1]
                menu=rest(menu)
                crucero.restaurant.append(menu)
                while True:  
                    otra=int(input("\n Desea: (1)Volver al menú anterior (2)Salir"))
                
                    if otra==1:
                        menu=rest(menu)
                        crucero.restaurant.append(menu)
                    elif otra==2:
                        print("¡Gracias por visitarnos!, esperemos que vuelva pronto.")
                        break     
                    else:
                        raise Exception                
            elif option==2:
                menu=[]
                crucero=cruceros[option-1]
                menu=rest(menu)
                crucero.restaurant.append(menu)

                while True:  
                    otra=int(input("\n Desea: (1)Volver al menú anterior (2)Salir"))
                
                    if otra==1:
                        menu=rest(menu)
                        crucero.restaurant.append(menu)
     
                    elif otra==2:
                        print("¡Gracias por visitarnos!, esperemos que vuelva pronto.")
                        break     
                    else:
                        raise Exception
            elif option==3:
                menu=[]
                crucero=cruceros[option-1]
                menu=rest(menu)
                crucero.restaurant.append(menu)

                while True:  
                    otra=int(input("\n Desea: (1)Volver al menú anterior (2)Salir"))
                
                    if otra==1:
                        menu=rest(menu)
                        crucero.restaurant.append(menu)
     
                    elif otra==2:
                        print("¡Gracias por visitarnos!, esperemos que vuelva pronto.")
                        break     
                    else:
                        raise Exception
            elif option==4:
                menu=[]
                crucero=cruceros[option-1]
                menu=rest(menu)
                crucero.restaurant.append(menu)

                while True:

                    otra=int(input("\n Desea: (1)Volver al menú anterior (2)Salir"))
                
                    if otra==1:
                        menu=rest(menu)
                        crucero.restaurant.append(menu)
     
                    elif otra==2:
                        print("¡Gracias por visitarnos!, esperemos que vuelva pronto.")
                        break     
                    else:
                        raise Exception
            elif option==5:
                print("¡Gracias por visitarnos!")
                break

            else:
                raise Exception 
        except:
            print("Ingrese correctamente su elección")
    return cruceros


def eliminar_producto(menu):
    """[Elimina un producto de la lista del menú según su nombre,sólo los de tipo alimento o bebida]

    Args:
        menu ([list]): [Lista de objetos(productos)]
    """    
    nombre=input("Ingrese el nombre del producto que desea eliminar: ").lower()
    for product in menu: 
        if product.nombre == nombre:
            if product.tipo=="bebida" or product.tipo=="alimento":
                menu.remove(product)
                print("Ha sido eliminado correctamente")
                return True
    return False

def eliminar_combo(menu):
    """[Elimina un producto de la lista del menú según su nombre,sólo el de tipo combo]

    Args:
        menu ([list]): [Lista de objetos(productos)]
    """    
    nombre=input("Ingrese el nombre del combo que desea eliminar: ").lower()
    for product in menu: 
        if product.nombre == nombre:
            if product.tipo=="combo":
                menu.remove(product)
                print("Ha sido eliminado correctamente")
                return True
    return False

def check_product(menu,nombre,var):
    """ Verifica si el producto ya existe en el menu"""
    if len(menu)==0:
        return True
    for producto in menu:
        if producto.nombre==nombre and producto.var==var:
            return False
    return True

def registrar_producto(menu):
    """[Registra y verifica los datos (nombre,tipo,precio,tamaño o modo de presentación) de un producto (bebida o alimento) según su tipo, luego lo agrega a una lista llamada "menu"]

    Args:
        menu ([list]): [lista de objetos (productos)]
    """    
    while True:
        try:
            nombre=input("\nIngrese el nombre del producto: ").lower()
            precio=float(input("Ingrese el precio: $"))            
            tipo=input("Ingrese según el tipo: (alimento) o (bebida)  ").lower()         
            if tipo=="alimento": 
                modo=int(input("Su producto es de modo: (1)Empaque (2)Preparación "))
                producto=Alimento(nombre,tipo,precio,modo)
                if modo==1:
                        producto.modo="empaque"
                elif modo==2:                            
                    modo="preparación"
                else:
                    print("Ingrese correctamente el modo ")
                    raise Exception    
                if check_product(menu,nombre,modo):
                    aceptado=True
                else:
                    aceptado=False
                    print("El producto ya existe")
                    raise Exception

            elif tipo=="bebida":
                size=int(input("Ingrese el tamaño de la bebida: (1)Pequeño (2)Mediano (3)Grande "))
                producto=Bebida(nombre,tipo,precio,size)
                if size==1:
                    producto.size="pequeño"
                elif size==2:
                    producto.size="mediano"
                elif size==3:
                    producto.size="grande" 
                else:
                    print("Ingrese correctamente el tamaño de su bebida")
                    raise Exception       
                if check_product(menu,nombre,size):
                    aceptado=True
                else:
                    aceptado=False
                    print("El producto ya existe")
                    raise Exception
                    
            else:
                print("Ingrese correctamente el tipo de producto")
                raise Exception
            if not producto.iva(precio):
                print("Precio inválido")
                raise Exception            
            break
        except:
            print("Error, intente de nuevo")      
    product=producto
    if aceptado==True:
        menu.append(product) 
    print("\n ¡Producto registrado exitosamente!")
    return menu

def modificar_producto(menu):
    """[Verifica que exista el producto en la lista "menu" y que sea de tipo "bebida" o "alimento", para luego
    preguntar cuál de los datos de dicho producto desea modificar, y al modificarlo se actualiza
    dicho producto en la lista "menu"]

    Args:
        menu ([list]): [lista de objetos(productos)]
    """    
    nombre=input("Ingrese el nombre del producto que desea modificar: ").lower()
    for product in menu: 
        if product.nombre == nombre:
            while True:
                try:
                    tipo=int(input("Ingrese si el producto es de tipo: (1)Alimento  (2)Bebida "))
                    if tipo==1:
                        op=int(input("Indique lo que quisiera modificar: (1)Nombre (2)Tipo (3)Precio (4)Modo"))
                        if op==1:
                            nom=input("Ingrese el nuevo nombre: ").lower()
                            product.nombre=nom
                        elif op==2:
                            tip=input("Ingrese el nuevo tipo: ").lower()
                            if tip !="bebida" or tip!="alimento":
                                raise Exception
                            product.tipo=tip    
                        elif op==3:
                            pre=float(input("Ingrese el nuevo precio: "))
                            product.precio=pre
                            if not product.iva(pre):
                                print("Precio inválido")
                                raise Exception                        
                        elif op==4:
                            mod=int(input("Ingrese el nuevo modo:(1)Preparación (2)Empaque "))
                            if mod==1:
                                product.modo="preparación"
                            elif mod==2:
                                product.modo="empaque"
                            else:
                                print("Modo incorrecto")
                                raise Exception
                        else:
                            print("Indique correctamente lo que desea modificar") 
                            raise Exception                        
                    elif tipo==2:
                        op=int(input("Indique lo que quisiera modificar: (1)Nombre (2)Tipo (3)Precio (4)Tamaño"))
                        if op==1:
                            nom=input("Ingrese el nuevo nombre: ").lower()
                            product.nombre=nom
                        elif op==2:
                            tip=input("Ingrese el nuevo tipo: ").lower()
                            if tip !="bebida" or tip!="alimento":
                                raise Exception
                            product.tipo=tip    
                        elif op==3:
                            pre=float(input("Ingrese el nuevo precio: "))
                            product.precio=pre
                            if not product.iva(pre):
                                print("Precio inválido")
                                raise Exception 
                        elif op==4:
                            mod=int(input("Ingrese el nuevo tamaño:(1)Pequeño (2)Mediano (3)Grande"))
                            if mod==1:
                                product.size="pequeño"
                            elif mod==2:
                                product.size="mediano"
                            elif mod==3:
                                product.size="grande"
                            else:
                                print("Modo incorrecto")
                                raise Exception
                        else:
                            print("Indique correctamente lo que desea modificar") 
                            raise Exception                        
                    else:
                        print("Indique correctamente el tipo de producto (Recordatorio: los de tipo combo no tienen opción de ser modificados)")
                        raise Exception 
                    break         
                except:
                    print("Error intente de nuevo")                  
            print("Producto modificado exitosamente!")        
            return True
    return False

def check_existencia(menu,nombre):
    for product in menu:
        if product.nombre==nombre:
            return product
    return False

def check_rango(menu,choice):
    """Verifica los rangos en los que se van a tomar los productos"""
    products=[]
    if choice==1:
        for product in menu:
            if product.precio>=0 and product.precio<=25:
                products.append(product)
        return products
    elif choice==2:
        for product in menu:
            if product.precio>=25 and product.precio<=50:
                products.append(product)
        return products
    elif choice==3:
        for product in menu:
            if product.precio>=50 and product.precio<=100:
                products.append(product)
        return products


def buscar_producto(menu,var):
    """[Busca la disponibilidad de un producto o combo en el menú según lo que indique el segundo parametro ]
    Args:
        menu ([list]): [lista de objetos(productos)]
        var ([str]): [el tipo de producto a buscar]

    """
    while True:
        try:

            forma=int(input("Usted desea buscar según el: \n(1)Nombre \n(2)Rango de precio "))
            if forma==1:
                nombre=input("Ingrese el nombre: ")
                if not check_existencia(menu,nombre):
                    print("\n El producto no existe")
                producto=check_existencia(menu,nombre)
                if var=="combo":
                    if producto.tipo=="combo":
                        print(producto.show())
                        print("\n Producto encontrado!")
                elif var=="producto":
                    if producto.tipo=="alimento" or producto.tipo=="bebida":
                        print(producto.show())
                        print("\n Producto encontrado!")
                    
            elif forma==2:

                rango=int(input("Ingrese el rango por el cual quiere buscar los productos:\n\n(1)0-25 \n(2)25-50 \n(3)50-100"))
                if len(menu)==0:
                    print("\n Aún no hay productos registrados en el menú")
                if rango==1:
                    product=check_rango(menu,rango)  
                    if len(product)==0:
                        print("\n No hay productos registrados en ese rango")    
                    if var=="combo":
                        for pro in product:
                            if pro.tipo=="combo":
                                print(pro.show())
                    elif var=="producto":
                        for pro in product:
                            if pro.tipo=="alimento" or pro.tipo=="bebida":
                                print(pro.show())

                elif rango==2:
                    product=check_rango(menu,rango)  
                    if len(product)==0:
                        print("\n No hay productos registrados en ese rango")    
                    if var=="combo":
                        for pro in product:
                            if pro.tipo=="combo":
                                print(pro.show())
                    elif var=="producto":
                        for pro in product:
                            if pro.tipo=="alimento" or pro.tipo=="bebida":
                                print(pro.show())

                elif rango==3:
                    product=check_rango(menu,rango)  
                    if len(product)==0:
                        print("\n No hay productos registrados en ese rango")    
                    if var=="combo":
                        for pro in product:
                            if pro.tipo=="combo":
                                print(pro.show())
                    elif var=="producto":
                        for pro in product:
                            if pro.tipo=="alimento" or pro.tipo=="bebida":
                                print(pro.show())                    
                else:
                    print("Indique correctamente el rango que desea elegir")
                    raise Exception
            else:                        
                print("\n Indique correctamente la manera por la cual desea buscar el producto ")
                raise Exception
            break 
        except:
            print("\n Error, intente de nuevo \n")                


def cantidades(cantidad):
    """[Verifica que el mínimo de productos sea 2.
    (Tomé 20 de máximo como referencia para establecer un límite) ]

    Args:
        cantidad ([int]): [cantidad (de productos a agregar en el combo)]
    """
    if cantidad <2 or cantidad>20:
        return False
    return True

def check_combito(menu,product):
    for pro in menu:
        if pro.nombre==product:
            return True
    return False

def combito(menu,cantidad):
    """[Ejecuta un ciclo tantas veces como lo indique la cantidad, pidiendo cada vez el nombre de un producto,
    luego los va guardando en una lista]

    Args:
        cantidad ([int]): [cantidad de veces a repetir el ciclo]
    """
    productos=[]
    for x in range(cantidad):
        product=input("Nombre del producto: ").lower()
        if check_combito(menu,product):
            productos.append(product)
        else:
            print("\n Ya que es un nuevo producto, debe registrar primero el producto en nuestra lista de productos, luego se le preguntara inmediatamente el nombre de los siguientes a agregar al combo ")
            menu=registrar_producto(menu)
            product=input("\n Ahora ingrese el nombre del producto recién registrado, luego se le preguntará el nombre del siguiente a agregar al combo de ser el caso: ").lower()
            if check_combito(menu,product):
                productos.append(product)
    return productos,menu

def registrar_combo(menu):
    """[Registra y verifica los datos (nombre,tipo,precio,cantidad,productos) de un producto de tipo "combo" , luego lo agrega a una lista llamada "menu"]

    Args:
        menu ([list]): [lista de objetos (productos)]
    """

    while True:
        try:
            nombre=input("Ingrese el nombre del combo: ").lower()
            precio=float(input("Ingrese el precio: "))
            tipo="combo"
            cantidad=int(input("Ingrese la cantidad de productos que tendrá el combo : "))        
            if not cantidades(cantidad):
                print("\n Error, verifique si introdujo correctamente la cantidad (el combo debe de tener un mínimo de 2 productos, máximo 20) \n ")
                raise Exception
            print("\n A continuación deberá ingresar uno a uno cada producto: ")
            productos,menu= combito(menu,cantidad)
            combo=Combo(nombre,tipo,precio,cantidad,productos)
            if not combo.iva(precio):
                print("Precio inválido")
                raise Exception
            break
        except:
            print("Error, intente de nuevo")      
    comb=combo
    menu.append(comb)
    print("\n ¡Combo registrado exitosamente!")
    return menu


def rest(menu):
    """[Menú de opciones sobre lo que se puede hacer en el restaurante,
    verifica el acceso a cada una según la decisión del cliente]

    Args:
        menu ([list]): [lista de objetos(productos)]
        clients ([list]): [lista de objetos(clientes)]
    """    

    while True:
        try:
            op=int(input("\n 🍽️  Bienvenido al Restaurante de Saman Caribbean, usted desea:\n \n(1)Agregar plato al menú \n(2)Eliminar producto del menú \n(3)Modificar producto del menú \n(4)Agregar combos al menú \n(5)Eliminar combo del menú  \n(6)Buscar producto \n(7)Buscar combo \n(8)Salir \n"))

            if op==1:
                menu=registrar_producto(menu)
            elif op==2:
                if not eliminar_producto(menu):
                    print("\n No existe producto registrado con ese nombre para poder eliminarlo")
                    raise Exception
            elif op==3:
                if not modificar_producto(menu):                    
                    print("\n No existe producto registrado con ese nombre para poder modificarlo")
                    raise Exception
            elif op==4:
                menu=registrar_combo(menu)
            elif op==5:    
                if not eliminar_combo(menu):
                    print("\n No existe combo registrado con ese nombre para poder eliminarlo")
                    raise Exception                
            elif op==6:
                var="producto"
                buscar_producto(menu,var)
            elif op==7:
                var="combo"
                buscar_producto(menu,var)

            elif op==8:
                print("Hasta luego, gracias por ingresar al restaurante")  
                break 
            else:
                raise Exception
            break    
        except: 
            print("Error, intente seleccionar la opción correcta") 
    return menu

"""********************TURISMO************************************"""
def check_cupo(tour,cantidad):
    """Verifica que segun la cantidad de personas que desean ir al tour haya los suficientes cupos disponibles """
    if cantidad<=tour.cupo and tour.cupo!=0:
        return True
    else:
        return False

def check_descuentos(tour,monto_sin,cantidad,posi):
    """Chequea segun la posición en la lista de nuestros tours,si dicho tour cuenta con un descuento, de ser así guarda la cantidad a descontar en una variable y la retorna  
    Args:
        tour ([objeto]): [info del objeto y sus atributos]
        monto_sin ([float]): [monto a pagar (sin descuento)según la cantidad de personas ]
        cantidad ([int]): [cantidad de personas que compran tour]
        posi ([int]): [posición de el tour en mi lista de tours de cada crucero]

    """
    descuento=0
    if posi==2:
        descuento=0
    elif posi==3:
        descuento=0
    elif posi==1 or posi==4:
        if cantidad==1 or cantidad==2:
            descuento=0
        elif cantidad==3:
            descuento=(monto_sin/3)*0.10
        elif cantidad==4:
            descuento=((monto_sin/4)*0.10)*2
    return descuento


def elegir_tour(cruceros,clients):
    """[Menú de "Tours" disponibles que se le ofrecen a los      clientes en todos los destinos, verifica el acceso y/o compra de alguno según la decisión del cliente y si se encuentra previamente registrado,luego retorna los cruceros con sus cupos modificados, en donde el cliente con su atributo tour se iguala a la cantidad que gastó]

        Args:
        clients ([list]): [lista de objetos(clientes)]
        cruceros ([list]): [lista de objetos(cruceros)] """

    while True:
        try:
            print("\n 🗺️  Bienvenido a nuestros tours, estos son los cruceros: ")
            for cruce in cruceros:
                print(f"\n ({cruceros.index(cruce)+1}) {cruce.name}")
            option=int(input("\n Indique en cual se encuentra: \n(5)Para salir"))
            if option==1:
                crucero=cruceros[option-1]
            
            elif option==2:
                crucero=cruceros[option-1]

            elif option==3:
                crucero=cruceros[option-1]
            elif option==4:
                crucero=cruceros[option-1]
            elif option==5:
                print("¡Gracias por visitarnos!")
                break
            else:
                raise Exception 

            dni=int(input("Ingrese su documento de identidad"))
            if dni<=0:
                print("Ingrese correctamente su dni")
                raise Exception
            #if not check_dni(dni,crucero):
                #print("No se encuentra registrado en el crucero")
                #raise Exception
            #client=check_dni(dni,crucero)
                 

            print("\n A continuación verá la información de cada tour: ")
            for tours in crucero.tours:
                print(tours.mostrar())

            for tours in crucero.tours:
                print(f"\n\n ({crucero.tours.index(tours)+1}) {tours.nombre}")

            choice=int(input("\n Ingrese el número del tour que desea adquirir o (5)Para salir: "))
            cantidad=int(input("Ingrese la cantidad de personas en total:"))
            date=datetime.now()
            if choice==1:
                tour=crucero.tours[choice-1]
                posi=1
            elif choice==2:
                tour=crucero.tours[choice-1]
                posi=2
            elif choice==3:
                tour=crucero.tours[choice-1]
                posi=3
            elif choice==4:
                tour=crucero.tours[choice-1]
                posi=4
                
            elif choice==5:
                print("\n Hasta luego")
                break
            else:
                print("Ingrese correctamente la opcion")
                

            if cantidad<=0:
                print("Error ingresando la cantidad de personas")
                raise Exception
            elif cantidad>tour.maxi:
                print("Usted ha sobrepasado el limite de personas admitidas para la compra del tour")

            if not check_cupo(tour,cantidad):
                print("No hay suficientes cupos disponibles ")
                raise Exception   
            if check_cupo(tour,cantidad):
                tour.cupo=tour.cupo-cantidad
            
            monto_sin=tour.precio*cantidad
            descuento=check_descuentos(tour,monto_sin,cantidad,posi)
            monto=monto_sin-descuento
            #client.tour=montototal
            
            #for client in clients:
                #if client.dni==dni:
                    #client.tour=monto


            print(f"\n 📃 Su factura ha sido registrada! \n\n •Documento de identidad:{dni} \n •Cantidad de personas:{cantidad} \n •Hora:{date} \n •Hora del tour: {tour.hora}:00 horas \n •Monto: {monto}")

            while True:  
                otra=int(input("\n Desea: (1)Volver al menú anterior (2)Salir"))

                if otra==1:
                    cruceros=elegir_tour(cruceros)
                elif otra==2:
                    print("¡Gracias por visitarnos!, esperemos que vuelva pronto.")
                    break     
                else:
                    raise Exception       
            break                    
        except:
            print("Ingrese correctamente su elección")
    return cruceros,clients


def check_dni(dni,crucero):
    """ Chequea si la cedula del cliente se encuentra registrada en el crucero correspondiente que selcciono"""
    for client in crucero.clients:
        if client.dni==dni:
            return client
    return False        


"""********************CRUCEROS***********************************"""


def crucero_search(cruceros):
    """[Menú de 'Cruceros' disponibles, verifica el acceso a su información detallada según la decisión del cliente]

    Args:    
    cruceros ([list]): [lista de objetos(cruceros)]"""
    
    for cruce in cruceros:
        print(f"\n ({cruceros.index(cruce)+1}) {cruce.name}")
    while True:
        try:
            option=int(input("\n Indique el crucero del cual desea saber su información: "))
            if option==1:
                cruceros[option-1].muestra()
            elif option==2:
                cruceros[option-1].muestra()
            elif option==3:
                cruceros[option-1].muestra()
            elif option==4:
                cruceros[option-1].muestra()
            else:
                raise Exception                
            break
        except:
            print("Intente de nuevo")
    return cruceros


def registrar_cruceros(cruceros):
    """[Menú de 'Cruceros' disponibles que se le ofrecen a los  clientes en todos los destinos, verifica el acceso a alguno según la decisión del cliente]
    
    Args:    
    cruceros ([list]): [lista de objetos(cruceros)]

    """
    while True:
        try:
            op=int(input("🚢  Bienvenido a los Cruceros de Saman Caribbean, usted desea: \n\n(1)Ver cruceros disponibles \n(2)Salir"))
            if op==1:
                crucero_search(cruceros)
            elif op==2:
                print("\n ¡Hasta luego!")
                break
            else:
                raise Exception        
            break
        except:
            print("Error, intente seleccionar la opción correcta")       
    return cruceros

    
    

"""********************HABITACIONES*******************************"""
def abc():
    """Importa y agrega todas las letras del abecedario en mayúscula a una lista"""
    abc=[]
    alphabet_mayus = string.ascii_uppercase
    alphabet_mayus = list(alphabet_mayus)
    for f in alphabet_mayus:
        abc.append(f)
    return abc

def mostrar_piso(crucero,f,c,posicion,abecedario,ocupadas):
    """  Muestra segun el piso su disponibilidad, 0 desocupada y x si esta ocupada, luego pregunta la que el cliente quiere comprar """
    print("                   PISO                            ")
    numeros = [i for i in range(c + 1)]

    for n in numeros:
        print(f"{n}", end=" || ", flush=True)

    print(
    )  

    for i in range(f):
        print(abecedario[i], end=" || ", flush=True)

        for j in range(c):
            print(check_room(crucero, abecedario[i], j+1, posicion), end=" || ")

            #chequear ocupada ono
            #print('0', end=" || ")
        print()
    print(" ")    
    if f==1:
        letricas=abecedario[0]
    else:
        letricas=abecedario[0:f]

    while True:
        try:
            letra=input("\n Ingrese el pasillo a seleccionar: ").upper()
            numero=int(input("Ingrese el número de habitación: "))

            if letra not in letricas or numero not in numeros:
                print('Ingrese pasillo y numero correctamente')

                raise Exception
            for hab in ocupadas:
                if letra==hab.letra and numero==hab.numero:
                    print("Ya se encuentra ocupada!")
                    raise Exception
                else:
                    print("Habitación disponible!")    
            #if check_room(crucero, letra, numero, posicion)=='X':
                #print('Habitación ocupada')
                #raise Exception
            #else:
                #save_room(crucero, letra, numero,posicion)
            break
        except:
            print("Intente de nuevo")
    return letra,numero
    
def check_room(crucero,letra, numero, posicion):
    """retorna x si la habitacion esta ocupada"""
    crucero_ocupacion = ocupada.get(crucero.name)
    if crucero_ocupacion:
        piso_ocupacion = crucero_ocupacion.get(crucero.rooms[posicion-1].name)
        if piso_ocupacion:
            letra_ocupacion = piso_ocupacion.get(letra)
            if letra_ocupacion:
                numeros_reservados = letra_ocupacion
                if numero in numeros_reservados:
                    return 'X'      
    return '0'


def save_room(crucero,letra, numero, posicion):
    crucero_ocupacion = ocupada.get(crucero.name)
    if crucero_ocupacion:
        piso_ocupacion = crucero_ocupacion.get(crucero.rooms[posicion-1].name)
        if piso_ocupacion:
            letra_ocupacion = piso_ocupacion.get(letra)
            if letra_ocupacion:
                numeros_reservados = letra_ocupacion
                if numero not in numeros_reservados:
                    numeros_reservados.append(numero)
                    ocupada[crucero.name] = {crucero.rooms[posicion-1].name: {letra: numeros_reservados}}
            else:
                ocupada[crucero.name][crucero.rooms[posicion-1].name][letra] = [numero]
        else:
            ocupada[crucero.name][crucero.rooms[posicion-1].name] = {letra: [numero]} 
    else:
        ocupada[crucero.name] = {crucero.rooms[posicion-1].name:{letra: [numero]} }





def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

def abundante(n):
    if n<0:
        return False
    count =  1
    suma = 0
    while (count<n):
        if (n%count==0):
            suma+=count
        count = count + 1
    if (suma>(n)):
        return True
    else:
        return False

def upgrade(habitacion):
    
    if habitacion=="sencilla":
        habitacion="premium"
    elif habitacion=="premium:":
        habitacion="vip"                
    return habitacion

def chequear_dni(crucero,dni):
    for client in crucero.clients:
        if client.dni==dni:       
            return False
    return True

def registrar_cliente(crucero,habitacion,clients,cantidad,monto_total):
    """Registra todos los datos del cliente y calcula su respectivo descuento, luego imprime la factura y retorna los clientes """
    while True:
        try:
            descuento_discapacitado=0
            descuento_primo=0
            descuento_abundante=0
            upgrade=0
            tour=0
            nombre=input("\n Ingrese su nombre completo: ")
            dni=int(input("Ingrese su documento de identidad: "))
            if not chequear_dni(crucero,dni):
                print("Ya existe una compra registrada con ese documento de identidad en este crucero")
            edad=int(input("Ingrese su edad: "))
            if edad<=16 or edad>140:
                print("Edad inválida")
                raise Exception
            discapacidad=input("¿Tiene alguna discapacidad? : ").lower()
            if discapacidad=="si":
                descuento_discapacitado=monto_total*0.30
            elif discapacidad=="no":
                descuento_discapacitado=0
            else:
                raise Exception    

            if not is_prime(dni):
                descuento_primo=0
            if is_prime(dni):
                descuento_primo=monto_total*0.10
            if abundante(dni):
                descuento_abundante=monto_total*0.15
            if not abundante(dni):
                descuento_abundante=0
            
            descuento=descuento_abundante+descuento_primo+descuento_discapacitado
            con_descuento=round(monto_total-descuento,2) 
            
            impuestos=round(con_descuento*0.16,2)
            total=round(con_descuento+impuestos,2)
            if edad>=65:
                de=int(input("\n Desea un upgrade: (1)Si (2)No ")) 
                if de==1:
                    print("Upgrade de habitacion sin costo")
                    #habitacion=upgrade(habitacion)
                elif de==2:
                    print("Correcto, gracias.")
                else:
                    print("\n Error, ingrese correctamente")
                    raise Exception    
            break
        except:
            print("\n Error, intente de nuevo")     
    client= Cliente(nombre,dni,edad,discapacidad,habitacion,monto_total,con_descuento,impuestos,total,tour)         
    clients.append(client)
    client.mostrar_factura()
    return clients,client

def hab_disponibles(habitaciones,clients,crucero,ocupadas):
    """ Según su elección se le pregunta la cantidad de personas que irán con el cliente a la habitación, luego se les muestra el mapa de habitaciones segun el piso y registra los datos del cliente  """
    while True:
        try:
            abecedario=abc() 
            habitacion=input("\n Ingrese el tipo de habitación que desea \n\n((simple)/(vip)/(premium)) : ").lower()
            cantidad=int(input("\n Cantidad de personas que viajan:"))
            if cantidad<=0 or cantidad>20:
                print("Cantidad de personas inválida")
                raise Exception
            
            if habitacion=="simple":
                monto_total=crucero.cost['simple']
                if cantidad<=crucero.capacity['simple']:
                    posicion=1
                    vendo=1
                    simple=crucero.rooms['simple']
                    
                    letra,numero=mostrar_piso(crucero,simple[0],simple[1],posicion,abecedario,ocupadas)  
                    
                    referencia=input("Referencia que aportar sobre la habitación: ")
                    capacidad=crucero.capacity['simple']
                    habitacion=Sencilla(letra,numero,capacidad,referencia)
                    ocupadas=ocupadas.append(habitacion)
                    misma_hab=[]
                    for x in range(cantidad):
                        clients,cada_cliente=registrar_cliente(crucero,habitacion,clients,cantidad,monto_total)
                        misma_hab.append(cada_cliente)
                        (crucero.clients).append(cada_cliente)
            elif habitacion=="vip":
                monto_total=crucero.cost['vip']
                if cantidad<=crucero.capacity['vip']:
                    vendo=1
                    posicion=3
                    vip=crucero.rooms['vip']
                    letra,numero=mostrar_piso(crucero,vip[0],vip[1],posicion,abecedario,ocupadas)  
                    referencia=input("Referencia que aportar sobre la habitación: ")
                    capacidad=crucero.capacity['vip']
                    habitacion=Vip(letra,numero,capacidad,referencia)
                    ocupadas=ocupadas.append(habitacion)
                    misma_hab=[]
                    for x in range(cantidad):
                        clients,cada_cliente=registrar_cliente(crucero,habitacion,clients,cantidad,monto_total)
                        misma_hab.append(cada_cliente)
                        (crucero.clients).append(cada_cliente)
                    
            elif habitacion=="premium":
                monto_total=crucero.cost['premium']
                if cantidad<=crucero.capacity['premium']:
                    vendo=1
                    posicion=2
                    premium=crucero.rooms['premium']
                    letra,numero=mostrar_piso(crucero,premium[0],premium[1],posicion,abecedario,ocupadas)
                    referencia=input("Referencia que aportar sobre la habitación: ")
                    capacidad=crucero.capacity['premium']
                    habitacion=Premium(letra,numero,capacidad,referencia)
                    ocupadas=ocupadas.append(habitacion)
                    misma_hab=[]
                    for x in range(cantidad):
                        clients,cada_cliente=registrar_cliente(crucero,habitacion,clients,cantidad,monto_total)
                        misma_hab.append(cada_cliente)
                        (crucero.clients).append(cada_cliente)

            else:
                print("Ingrese correctamente el tipo de habitación")
                raise Exception
            
            break
        except:
            print("\n ERROR intente de nuevo")           
    return clients,ocupadas,crucero


def comprar_habitacion(cruceros,clients,ocupadas):
    """Selecciona el crucero en el cual el cliente hará su compra de habitación y devuelve una lista de las habitaciones ocupadas y de los clientes     """
    while True:
        try:
            op=int(input("\n Usted desea comprar un boleto en base al: \n\n(1)Barco \n(2)Destino"))
            if op==1:
                for cruce in cruceros:
                    print(f"\n ({cruceros.index(cruce)+1}) {cruce.name}")
                option=int(input("\n Seleccione según el barco en que desea comprar: "))
                if option==1:
                    crucero=cruceros[option-1]
                elif option==2:
                    crucero=cruceros[option-1]
                elif option==3:
                    crucero=cruceros[option-1]
                elif option==4:
                    crucero=cruceros[option-1]
                else:
                    raise Exception 
                

            elif op==2:
                for cruce in cruceros:
                    print(f"\n ({cruceros.index(cruce)+1}) {cruce.route}")
                option=int(input("\n Seleccione según el destino que desea comprar: "))
                if option==1:
                    crucero=cruceros[option-1]
                elif option==2:
                    crucero=cruceros[option-1]
                elif option==3:
                    crucero=cruceros[option-1]
                elif option==4:
                    crucero=cruceros[option-1]
                else:
                    raise Exception  
            else:
                raise Exception   
            break     
        except:
            print(" ERROR Intente de nuevo")
    clients,ocupadas,crucero=hab_disponibles(habitaciones,clients,crucero,ocupadas)

    return clients,ocupadas,cruceros

def desocupar_hab(ocupadas):
    desocupo=input("Ingrese cual habitación desea desocupar")
    print("la desocupo")
    return ocupadas

def buscar_hab(cruceros):
    while True:
        try:
            op = input("Buscar habitacion segun: \n 1. Tipo \n 2. Capacidad \n 3. Tipo + Pasillo + Numero (EJ: SA9 (SIMPLE PASILLO A HABITACION 9)) \n 4. Salir ")
            if op == "1":
                

                print("Tipo de habitacion: sencilla/premium/vip")
            elif op == "2":
                print("Capacidad de Hab")
            elif op == "3":
                print("Tipo + Pasillo + Numero")
            elif op == "4":
                print("Hasta luego")
                break
            else:
                print("Ingrese correctamente los datos")
            break    
        except:
            print("Intente de nuevo")
    return cruceros

def habitaciones(cruceros,clients,ocupadas):
    """[Menú de opciones sobre las habitaciones de cada crucero,verifica el acceso a cada una según la decisión del cliente]

    Args:
        cruceros ([list]): [lista de objetos(cruceros)]
        clients ([list]): [lista de objetos(clientes)]"""

    while True:
        try:
            op=int(input("\n 🛎️  Bienvenido a Saman Caribbean-Habitaciones, usted desea: \n\n(1)Comprar habitación \n(2)Desocupar habitación \n(3)Buscar habitación \n(4)Salir"))
    
            if op==1:
                clients,ocupadas,cruceros=comprar_habitacion(cruceros,clients,ocupadas)
                
            elif op==2:
                print("desocupar")
                #ocupadas=desocupar_hab()
            elif op==3:
                print("buscar")
                #buscar_hab()
            elif op==4:
                print("\n ¡Hasta luego!")
                break
            else:
                raise Exception            

            break
        except:
            print("\n Error, intente seleccionar la opción correcta") 
    return clients,ocupadas,cruceros    


"""********************ESTADÍSTICAS*******************************"""

def estadisticas(clients,consumo,cruceros):
    """[Menú de estadísticas de la línea de cruceros Saman Caribbean,verifica el acceso a cada una según la decisión del usuario]

    Args:
        consumo([list]):[lista de objetos(productos consumidos)]
        cruceros ([list]): [lista de objetos(cruceros)]
        clients ([list]): [lista de objetos(clientes)]"""
     
    while True:
        try:
            op=int(input("\n 📊  Bienvenido a las 'Estadísticas' de Saman Caribbean,usted desea saber: \n\n(1)Promedio de gasto de un cliente en el crucero \n(2)Porcentaje de clientes que no compran tour \n(3)Top 3 clientes de mayor fidelidad en la línea \n(4)Top 3 cruceros con más ventas en tickets \n(5)Top 5 productos más vendidos del restaurante \n(6)Gráfico de estadísticas \n(7)Salir"))
            if op==1:
            

                print("promedio")
            elif op==2:
                print("no compran")
                #suma=0
                #for client in clients:
                    #if client.tour==0:
                        #suma+=1
                #total=round((suma*100)/len(clients),1)
                #print(f"\n El porcentaje de clientes que no compran tour es de: {total} % ")    

            elif op==3:

                print("fidelidad")

            elif op==4:
                print("3 cruceros ventas")

            elif op==5:

                ventas=[]
                for cruce in cruceros:
                    ventas.append(cruce.sells)
                print(ventas)
                
                #venticas=[]
                #for comida in ventas:
                    #venticas.append(comida['amount'])
                #print(venticas)    

                #lista=[2,7,9,101,56,5]
                #ordenados = sorted(lista, reverse=True)
                #top=ordenados[0:5]
                #print(top)
                print(f"Los 5 productos mas vendidos fueron: \n\n {1}\n {2} \n {3} \n {4} \n {5}")
            elif op==6:   
                print("grafico")

            elif op==7:
                print("\n ¡Hasta luego!")
                break
            else:
                raise Exception                    
            break
        except:
            print("Error, intente seleccionar la opción correcta") 
        
   

archivo=open("informacion.txt",'a')


def main():
    tour_1=Tour("Tour en el puerto",30,4,7,10)
    tour_2=Tour("Degustación de comida local",100,2,12,100)
    tour_3=Tour("Trotar por el pueblo/ciudad",0,1000000000000,6)
    tour_4=Tour("Visita a lugares históricos",40,4,10,15)

    cruceros=[]
    info=api()
    for crucero in info:
        name=crucero["name"]
        route=crucero["route"]
        departure=crucero["departure"]
        cost=crucero["cost"]
        rooms=crucero["rooms"]
        capacity=crucero["capacity"]
        sells=crucero["sells"]
        clients=[]
        restaurant=[]
        tours=[tour_1,tour_2,tour_3,tour_4]
        barco=Crucero(name,route,departure,cost,rooms,capacity,sells,clients,tours,restaurant)
        cruceros.append(barco)
    menu=[]
    clients=[]
    consumo=[]
    ocupadas=[]
 
    while True:
        try:
            opcion=int(input("\n 🚢  Bienvenido a Saman Caribbean, usted desea acceder a: \n\n(1)Cruceros \n(2)Habitaciones \n(3)Tours \n(4)Restaurante \n(5)Estadísticas \n(6)Salir \n"))
            if opcion==1:
                registrar_cruceros(cruceros)
                while True:
                    otra=int(input("\n Desea: (1)Volver al menú anterior (2)Salir"))
                    if otra==1:
                        cruceros(cruceros)
                    elif otra==2:
                        print("¡Gracias por visitarnos!, esperemos que vuelva pronto.")
                        break
                    else:
                        raise Exception
            elif opcion==2:
                clients,ocupadas,cruceros= habitaciones(cruceros,clients,ocupadas)
                while True:
                    otra=int(input("\n Desea: (1)Volver al menú anterior (2)Salir"))
                    if otra==1:
                        clients,ocupadas,cruceros=habitaciones(cruceros,clients,ocupadas)
                    elif otra==2:
                        print("¡Gracias por visitarnos!, esperemos que vuelva pronto.")
                        break
                    else:
                        raise Exception

            elif opcion==3:
                cruceros,clients=elegir_tour(cruceros,clients)
            elif opcion==4:
                cruceros=entrar_barco(cruceros)
            elif opcion==5:
                estadisticas(clients,consumo,cruceros)
                while True:
                    otra=int(input("\n Desea: (1)Volver al menú anterior (2)Salir"))
                    if otra==1:
                        print("hola")
                        estadisticas(clients,consumo,cruceros)
                    elif otra==2:
                        print("¡Gracias por visitarnos!, esperemos que vuelva pronto.")
                        break   
                    else:
                        raise Exception      
            elif opcion==6:
                print("¡Gracias por visitar Saman Caribbean, hasta luego!")
                break
            else:
                raise Exception   

            #dnis=[]
            #for client in clients:
                    #dnis.append(client.dni)
            #cadena = f' Documentos de identidad de personas registradas: {",".join(str(x)for x in dnis)}' 
            #archivo.write(cadena)                 
            archivo=open('informacion.txt','r')
            datos=archivo.read()
            archivo.close()
            print(datos)
            break
        except:
            print("\n Ingrese correctamente su elección")                       
main()
