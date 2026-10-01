def cantidad_donas (n):
    return[2**((i-1)/2) for i in range (1, n+1)]
print(cantidad_donas(10))