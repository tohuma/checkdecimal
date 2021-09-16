# (3 + √5)5 = 3935.73982... [393]
# (3 + √5)2 = 27.4164079... [027]
import math

raiz = math.sqrt(5);
qty = int(input("Cuantos números desea analizar: "));
for n in range(qty):
    num = float(input("Escriba el número a analizar: "));

    suma = 3 + raiz;
    potencia = pow(suma, num);
    
    string = str(potencia);
    split = string.split(".");
    first = split[0];

    if len(first) > 3:
        result = first[-3:];
    else:
        result = first.zfill(3);

    print (result);
