arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Add2 = []
Multiply_by_2 = []
Shift_2 = []

for i in range(len(arr)):
    Add2.append(arr[i] + 2)
    Multiply_by_2.append(arr[i]*2)
    Shift_2.append(arr[(i + 2) % len(arr)])

print('Originals:', arr)
print('Add 2:', Add2)
print('Multiply by 2:', Multiply_by_2)
print('Shift 2:', Shift_2)