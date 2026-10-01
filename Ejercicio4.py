def organizar_eventos(eventos:list[str],descendente:bool=False)->list[str]:
    if bool(descendente):
        return sorted(eventos,reverse=True)
    else:
        return sorted(eventos)

#ejemplo:
lista=["Kermés","Concurso de Comida","Reunión del Concejo Municipal"]
print(organizar_eventos(lista))
print(organizar_eventos(lista,True))

#Envío final