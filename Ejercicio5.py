from datetime import date
from typing import Optional

class ProductoKwikE:
    def __init__(self,descripcion:str,id_producto:int,fecha_vencimiento:date,precio:float,stock:int,):
        self.descripcion:str=descripcion
        self.id_producto:int=int(id_producto)
        self.fecha_vencimiento:date=fecha_vencimiento
        self.precio:float=float(precio)
        self.stock:int=int(stock)

    def actualizar_datos(self,descripcion:Optional[str]=None,fecha_vencimiento:Optional[date]=None,precio:Optional[float]=None,stock:Optional[int]=None)->None:
        if descripcion is not None:
            self.descripcion=descripcion
        if fecha_vencimiento is not None:
            self.fecha_vencimiento=fecha_vencimiento
        if precio is not None:
            self.precio=float(precio)
        if stock is not None:
            self.stock=int(stock)

    def dias_para_expirar(self)->int:
        hoy=date.today()
        dias_restantes=(self.fecha_vencimiento-hoy).days

        if dias_restantes<0:
            self.stock=0
            print(f"Alerta: Producto '{self.descripcion}'(ID:{self.id_producto}) expiró. El Stock está en cero.")
        else:
            return dias_restantes

#Ejercicio 6
def __str__(self) -> str:
        return (f"Producto: {self.descripcion} | " f"ID: {self.id_producto} | " f"Precio: ${self.precio:.2f} | " f"Stock: {self.stock}")

def __eq__(self,otro):
    return(self.id_producto==otro.id_producto and self.descripcion==otro.descripcion)

#Ejemplos

if __name__=="__main__":
    prod1=ProductoKwikE("Donuts Glaseadas",123,date(2026,10,31),1.50,50)
    prod2=ProductoKwikE("Donuts Glaseadas",123,date(2026,9,30),1.00,10)
    prod3=ProductoKwikE("Donuts de Chocolate",124,date(2027,1,1),1.75,30)

print(prod1)
print("¿prod1 es igual que prod2:",prod1==prod2)
prod1.actualizar_datos(precio=1.75,stock=45)
print("Producto 1 actualizado",prod1)
prod2.dias_para_expirar()
prod3.dias_para_expirar()
print("Stock de prod3 tras comprobar vencimiento:",prod3.stock)

#Envío final
