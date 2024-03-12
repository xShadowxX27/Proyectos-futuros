import random
w=input("insertar nombre del jugador 1 ->")
c=input("insertar nombre del jugador 2 ->")
Puntos_j1=0
Puntos_j2=0

while Puntos_j1<5 and Puntos_j2<5:
    b=random.randint(0,1)
    if b==0:
        print("salio cara", w, "ganó")
        Puntos_j1+=1
    if b==1:
        print("salio sello", c, "ganó")
        Puntos_j2+=1

if Puntos_j1>Puntos_j2:
    print("Ha ganado la competencia", w, "con un puntaje total de:", Puntos_j1, "-",Puntos_j2)
else:
    print("Ha ganado la competencia", c, "con un puntaje total de:", Puntos_j2, "-", Puntos_j1)