def distanciaEntreAmbos(palabra1, palabra2):
  d=dict()
  sizePalabra1=len(palabra1)
  sizePalabra2=len(palabra2)
  for i in range(sizePalabra1+1):
     d[i]=dict()
     d[i][0]=i
     
  for i in range(sizePalabra2+1):
     d[0][i] = i
     
  for i in range(1, sizePalabra1+1):
      
     for j in range(1, sizePalabra2+1):
        d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+( palabra1[i-1] != palabra2[j-1]))
        
  return d[sizePalabra1][sizePalabra2]


print (distanciaEntreAmbos("pera","papa"))
