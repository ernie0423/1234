consumo = int(input("ingrese su consumo: "))
if consumo < int(100):
    print(1.00, "bs")

if consumo >= int(100) or consumo <= int(499):
    print(1.20, "bs")

if consumo >= int(500) or consumo <= int(999):
    print(1.50, "bs")

if consumo >= int(1000):
        print(2.00, "bs")