a = int(input("Enter first term (a): "))
d = int(input("Enter common difference (d): "))
n = int(input("Enter term number (n): "))

nth_term = a + (n - 1) * d
sum_n = n * (2 * a + (n - 1) * d) / 2

print("Nth term:", nth_term)
print("Sum up to n terms:", sum_n)