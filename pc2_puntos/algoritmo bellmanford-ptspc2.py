import math 

valores={
    "a":[math.inf,""],
    "b":[math.inf,""],
    "c":[math.inf,""],
    "d":[math.inf,""],
    "e":[math.inf,""],
    "f":[math.inf,""],    
}

ArrCaminos=[
    ["a","b",1],
    ["a","c",2],
    ["a","d",8],
    ["b","e",3],
    ["c","e",3],
    ["c","f",8],
    ["c","d",5],
    ["d","f",12],
    ["e","f",4],    
]

inicio="a"
final="e"
 
 
def ActualizarValores(origen,destino,valor):
    
    if valor<valores[destino][0]: 
     
        valores[destino][0]=valor 
        
        valores[destino][1]=origen
        return True
    return False

valores[inicio][0]=0

while True:
    cancel=True 
    
    for i in ArrCaminos: 
        
        if ActualizarValores(i[0],i[1],valores[i[0]][0]+i[2]):
            cancel=False 
        
        if ActualizarValores(i[1],i[0],valores[i[1]][0]+i[2]):
            cancel=False 
    
    if cancel:
        break 

camino=[final]
 
while True:
    if camino[-1]==inicio:
        break
    camino.append(valores[camino[-1]][1])
 
print(str(camino[::-1]))
