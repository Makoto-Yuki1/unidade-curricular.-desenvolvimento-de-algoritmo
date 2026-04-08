pão = int(input())
doce = int(input())
bolo = int(input())

total_pontos = (pão * 1) + (doce * 2) + (bolo * 3)

print(total_pontos,"vejamos o que receberá")
if total_pontos >= 150:
    print("B")
elif total_pontos >= 120:
    print("D")
elif total_pontos >= 100:
    print("P")
else:
    print("N")



























