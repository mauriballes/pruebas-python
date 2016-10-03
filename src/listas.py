# Listas
l = [2, "Tres", True, ["Uno", 10]]

l[1] = 4 #Cambiar elementos de la lista

ele = l[1] # Acceder a un elemento por indice
ele = l[3][0] #Acceder a un elemento
			  #que esta en una lista
			  #que esta dentro de otra lista
print ele

# Para seleccionar sublistas
# Copiar ciertos elementos de una lista
l2 = l[0:3] # [indice_ini:cant_ele]
l3 = l[0:3:2] # [ind_ini:cant_ele:salto]
			  # salto = 1-normal,2-saltando 1,etc
l4 = l[1::2] # [ind_ini::salto] copia desde 0, saltando 2
print l4

#Para cambiar varios valores
#Nota: Solo usar listas para asignar
l[0:2] = [1,3]
print l
l[0:2] = [6]
print l

# Acceder a elementos de manera inversa
ele = l[-1] #-1=ultimo, -2=penultimo, etc.