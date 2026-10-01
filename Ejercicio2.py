def total_donas_consumidas(a:int,b:int) -> int:
    total=0
    for _ in range (b):
        total +=a
    return total

#ejemplo: 2 donas por persona para 4 personas -> total 8 donas consumidas
print(total_donas_consumidas(2,4))

#Envío final