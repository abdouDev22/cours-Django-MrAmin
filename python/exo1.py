
def calcul(n,s,com):
  if com =="+":
    return n+s
  elif com =="-":
    return n-s

nb1=int(input("Entrez le premier nombre:"))
nb2=int(input("Entrez le deuxieme nombre:"))
com=input("Entrez l'opérateur:")
p=calcul(nb1,nb2,com)
print(p)