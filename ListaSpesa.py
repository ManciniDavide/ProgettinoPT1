listaSpesa = []

def aggiunta(listaSpesa):
    listaSpesa.append(input("aggiungi valore"))
def visualizza(listaSpesa):
    for i in range(len(listaSpesa)):
        print(f"{i + 1}. {listaSpesa[i]}")
def rimuovere(listaSpesa):
    listaSpesa.pop(input("metti indice del elemento da rimuovere"))
def conta(listaSpesa):
    print(len(listaSpesa))
def svuota(listaSpesa):
    listaSpesa.clear()
while True:
    print("premi 0 per uscire,\npremi 1 per aggiungerre un elemento,\npremi 2 per visualizzare la lista,\n premi 3 per eliminare un elemento,\n premi 4 per contare gli elementi della lista,\n premi 5 per eliminare un elemento")
    x=int(input(""))
    if x == 0:
        break
    elif x == 1:
        aggiunta(listaSpesa)
    elif x == 2:
        visualizza(listaSpesa)
    elif x == 3:
        rimuovere(listaSpesa)
    elif x == 4:
        conta(listaSpesa)
    elif x == 5:
        svuota(listaSpesa)