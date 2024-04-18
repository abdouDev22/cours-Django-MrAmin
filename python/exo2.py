def calcul(n,com):
  taux_dollar=1.19
  taux_liver=0.87
  if com =="dollar":
    return n*taux_dollar
  elif com =="livre":
    return n*taux_liver


nb1=float(input("Entrez le motant:"))
com=input("Entrez le type de monnaie:")
print(calcul(nb1,com))

