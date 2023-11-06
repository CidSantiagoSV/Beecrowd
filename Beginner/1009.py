sellersName = str(input())
fixedSalary = float(input())
salesTotal = float(input())
payment = fixedSalary + (salesTotal * 0.15)

print("TOTAL = R$ %.2f" % payment)