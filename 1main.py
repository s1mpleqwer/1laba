numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
a = len(numbers)
b = 0
for i in range(a):
    if (numbers[i] != None):
        b += numbers[i]
c = b/a
for i in range(a):
    if (numbers[i] == None):
        numbers[i] = c
print("Измененный список:", numbers)
