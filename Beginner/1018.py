amount = int(input())
bills100 = amount / 100
money = amount % 100
bills50 = money / 50
money = money % 50
bills20 = money / 20
money = money % 20
bills10 = money / 10
money = money % 10
bills5 = money / 5
money = money % 5
bills2 = money / 2
money = money % 2
bills1 = money / 1
money = money % 1

print ("%i" % amount)
print ("%i nota(s) de R$ 100,00" % bills100)
print ("%i nota(s) de R$ 50,00" % bills50)
print ("%i nota(s) de R$ 20,00" % bills20)
print ("%i nota(s) de R$ 10,00" % bills10)
print ("%i nota(s) de R$ 5,00" % bills5)
print ("%i nota(s) de R$ 2,00" % bills2)
print ("%i nota(s) de R$ 1,00" % bills1)