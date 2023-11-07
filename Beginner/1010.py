[code, units, price] = input().split()
[code2, units2, price2] =  input().split()
amount = int(units) * float(price) + int(units2) * float(price2)

print("VALOR A PAGAR: R$ %.2f" % amount)