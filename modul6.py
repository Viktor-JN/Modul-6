import os
os.system('cls')
def adding(y, x, op="+"):
    if op == "+":
        together=y+x
        return together
    elif op == "-":
        together=y-x
        return together
    elif op == "*":
        together=y*x
        return together
    elif op == "/":
        together=y/x
        return together
print(adding(1, 4, "+"))

def name(myName=""):
    myName=input("Vad är ditt namn\n")
    print(myName)
name()
def looping():
    x=10
    forTheWorld=input("Vad vill du att världen ska veta 10 gånger om\n")
    print("\n")
    while x>0:
        print(forTheWorld)
        x-=1
looping()

ancestry=[]

def remove():
    while True:
        for x in ancestry:
            y=1
            print(y, x)
            y+=1
        try:
            x=int(input("Vilken i listan\n"))
            break
        except:
            print("Endast nummer")
    try:
        ancestry.pop(x-1)
    except:
        print("Skirv nummret av saken du vill ta bort")

def add():
    x=input("Vad vill du lägga till i listan\n")
    ancestry.append(x)

def sortera():
    ancestry.sort()

while True:
    print(ancestry)
    y=input("""Hur vill du redigera listan
Lägg till/a
Ta bort/r
Sortera/s
Avsluta/q\n""")
    if y.upper() == "A":
        add()
    elif y.upper() == "R":
        if len(ancestry) == 0:
            print("Du kan inte ta bort från en lista som inte har någonting i sig")
        else:
            remove()
    elif y.upper() == "Q":
        print("Hej då!")
        break
    elif y.upper() == "S":
        sortera()
    else:
        print("Välj någonting från listan")