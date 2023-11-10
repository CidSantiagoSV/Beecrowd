num = float(input())

n100 = num / 100
num = num % 100
n50 = num / 50
num = num % 50
n20 = num / 20
num = num % 20
n10 = num / 10
num = num % 10
n5 = num / 5
num = num % 5
n2 = num / 2
num = num % 2

m_1 = num / (1/1.0)
num = num % (1/1.0)
m50 = num / (1/2.0)
num = num % (1/2.0)
m25 = num / (1/4.0)
num =  num % (1/4.0)
m10 = num / (1/10.0)
num = num % (1/10.0)
m5 = num / (1/20.0)
num = num % (1/20.0)
m1 = num / (1/100.0)

print ("NOTAS:")
print ("%i nota(s) de R$ 100.00" % n100)
print ("%i nota(s) de R$ 50.00" % n50)
print ("%i nota(s) de R$ 20.00" % n20)
print ("%i nota(s) de R$ 10.00" % n10)
print ("%i nota(s) de R$ 5.00" % n5)
print ("%i nota(s) de R$ 2.00" % n2)

print ("MOEDAS:")
print ("%i moeda(s) de R$ 1.00" % m_1)
print ("%i moeda(s) de R$ 0.50" % m50)
print ("%i moeda(s) de R$ 0.25" % m25)
print ("%i moeda(s) de R$ 0.10" % m10)
print ("%i moeda(s) de R$ 0.05" % m5)
print ("%i moeda(s) de R$ 0.01" % m1)