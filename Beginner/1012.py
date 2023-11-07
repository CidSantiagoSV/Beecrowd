[A, B, C] = input().split()
rT = float(A) *  float(C) / 2
pi = 3.14159
rC = (float(C) * float(C)) * pi
aT = (float(A) +  float(B)) * float(C) / 2
aS = float(B) * float(B)
aR = float(A) * float(B)

print("TRIANGULO: %.3f" % rT)
print("CIRCULO: %.3f" % rC)
print("TRAPEZIO: %.3f" % aT)
print("QUADRADO: %.3f" % aS)
print("RETANGULO: %.3f" % aR)