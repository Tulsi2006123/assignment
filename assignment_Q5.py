val = 0xCAFE
count = 0
for i in range(4):
    if val & (1 << i):
        count += 1
test = count >= 3

reverse = ((val & 0xFF) << 8) | ((val >> 8) & 0xFF)
rotate = ((val << 4) & 0xFFFF) | (val >> 12)
print(test)
print(hex(reverse))
print(hex(rotate))