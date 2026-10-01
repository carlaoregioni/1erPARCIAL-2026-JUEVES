def total_interrupciones(a:int,b:int)->int:
    if b==0:
        return 0
    return a+total_interrupciones(a,b-1)

#ejemplo: 2 interrupciones/hora cada 3 horas -> total 6 interrupciones
print(total_interrupciones(2,3))