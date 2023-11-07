[A, B, C] = [int(n) for n in input().split()]
MaiorAB = (A + B + abs (A - B)) / 2
MaiorABC = (MaiorAB + C + abs (MaiorAB - C)) / 2

print("%i eh o maior" % MaiorABC)