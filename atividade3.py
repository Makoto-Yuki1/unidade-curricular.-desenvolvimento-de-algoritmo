resp = input("você posssui carteira dde motorista? s/N:").strip().lower()
resultado = resp in ("s","S", "N", "n", "não", "sim")

print("resultado",resultado)
print(type(resultado))