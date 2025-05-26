
n = int(input("Bir sayı gir: "))
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
d = {}
toplam_kare = 0
toplam_fibonacci = 0
for x in range(1, n + 1):
    kare = x * x
    fib = fibonacci(x)
    d[x] = {'kare': kare, 'fibonacci': fib}
    toplam_kare += kare
    toplam_fibonacci += fib

print("değeer:", d)
print(" kare Topplamı:", toplam_kare)
print("Fibonacci Toplamı:", toplam_fibonacci)