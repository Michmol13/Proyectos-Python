bits = 0
bytes = 0
gigabytes = 0

bits = int(input("Ingrese el número de bits:  "))

bytes = bits / 8

gigabytes = bytes / 1073741824 # un gigabyte tiene 1073741824 bytes

print(f"{bits} bits son {gigabytes: .3f} gigabytes")