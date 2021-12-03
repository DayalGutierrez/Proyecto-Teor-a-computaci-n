def mdi(dinero):
    return str(dinero),"No se cuenta con el dinero suficiente","","0"
    #las salidas son en orden: dinero, alerta, producto, cambio

def mdm(dinero):
    return str(dinero),"Esta máquina acepta máximo $50","","0"

def mrl(dinero):
    return str(dinero),"Ya cuenta con el dinero suficiente para poder retirar cualquier rato","","0"

def mas5(dinero):
    dinero+=5
    return str(dinero),"","","0"

def mas10(dinero):
    dinero+=10
    return str(dinero),"","","0"

def mas20(dinero):
    dinero+=20
    return str(dinero),"","","0"

def menos5(dinero):
    dinero-=5
    return str(dinero),"","","0"

def menos10(dinero):
    dinero-=10
    return str(dinero),"","","0"

def menos15(dinero):
    dinero-=15
    return str(dinero),"","","0"

def menos20(dinero):
    dinero-=20
    return str(dinero),"","","0"

def menos25(dinero):
    dinero-=25
    return str(dinero),"","","0"

def menos30(dinero):
    dinero-=30
    return str(dinero),"","","0"

def menos35(dinero):
    dinero-=35
    return str(dinero),"","","0"

def menos40(dinero):
    dinero-=40
    return str(dinero),"","","0"

def menos45(dinero):
    dinero-=45
    return str(dinero),"","","0"

def menos50(dinero):
    dinero-=50
    return str(dinero),"","","0"

def rmenos40(dinero):
    dinero-=40
    return str(dinero),"","Red bull 250 ml","0"

def c355menos20(dinero):
    dinero-=20
    return str(dinero),"","Coca-Cola 355 ml","0"

def c235menos15(dinero):
    dinero-=15
    return str(dinero),"","Coca-Cola 235 ml","0"



def salida(dinero,s):
    dinero = int(dinero)
    din,alerta,prod,cambio = globals()[s](dinero)
    return(din,alerta,prod,cambio)


