#34 condiciones if else.

a=8
b=4

print("a={}>b={} ({})".format(a,b,a>b))

print("---------------")

print("a={}<b={} ({})".format(a,b,a<b))

print("---------------")

if(a>b):
    print("a={} es mayor que b={}".format(a,b))

if(a<b):
    print("a es mayor que b")

print("--------------------")        

a=8
b=4
c=2
d=6

if(a>c)and(b<d):
    print("la primera exprecion es correcta")

if(a>c)and(b>d):
    print("la primera exprecion es correcta") 

print("--------------------")         

if(a>c)and(b>d):
    print("la primera exprecion es correcta")
else:
    print("la primera exprecion NO es correcta")   

print("--------------------")       

a=8
b=4

if(a>b):
    print("a={} es mayor que b={}".format(a,b))
elif (a==b):
    print("a={} es igual a b={}".format(a,b))
else:
    print("ninguna exprecion anterior es correcta")

print("--------------------")       

a=8
b=8

if(a>b):
    print("a={} es mayor que b={}".format(a,b))
elif (a==b):
    print("a={} es igual que b={}".format(a,b))
else:
    print("ninguna exprecion anterior es correcta")   

print("--------------------")        

a=8
b=10

if(a>b):
    print("a={} es mayor que b{}".format(a,b))
elif (a==b):
    print("a={} es igual a b={}".format(a,b))
else:
    print("ninguna exprecion anterior es correcta")     

print("--------------------")        