from Ejercicio5 import ProductoKwikE
from datetime import date, timedelta
class KwikEMart:
    def __init__(self):
        self.bebidas=[]
        self.snacks=[]
        self.conveniencia=[]
    
    def agregar_producto(self,pasillo:str,producto:ProductoKwikE):
        if not isinstance(producto,ProductoKwikE):
            raise TypeError("El elemento no forma parte de la clase ProductoKwikE")
        getattr(self,pasillo.lower()).append(producto)
    
    def remover_producto(self,id_producto:int):
        for lista in (self.bebidas,self.snacks,self.conveniencia):
            for prod in lista:
                if prod.id_producto==id_producto:
                    lista.remove(prod)
                return True
        return False

    def actualizar_stock(self, id_producto:int,nuevo_stock:int):
        for lista in(self.bebidas,self.snacks,self.conveniencia):
            for prod in lista:
                if prod.id_producto==id_producto:prod.stock=nuevo_stock
                return True
        return False

    def desechar_expirados_24h(self):
        limite=date.today()+timedelta(days=1)
        total_desechados=[]

        for nombre_pasillo in ("bebidas","snacks","conveniencia"):
            lista=getattr(self,nombre_pasillo)
            vigentes=[]
            for p in lista:
                if p.fecha_vencimiento<=limite: 
                    total_desechados.append(p)
                else: vigentes.append(p)
            setattr(self,nombre_pasillo,vigentes)
        return total_desechados

#Ejemplos
tienda=KwikEMart()
dona=ProductKwikE("Donuts Glaseadas",123,date.today(),1.50,50)
leche=ProductKwikE("Leche Descremada",125,date.today()+timedelta(days=5),2.00,10)

print(dona)

tienda.agregar_producto("Snacks",dona)
tienda.agregar_producto("Bebidas",leche)
tienda.actualizar_stock(125,8)

desechados=tienda.desechar_expirados_24h()
for item in desechados:
    print(f"Producto eliminado: {item.descripcion}")

#Envío final