numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

divisor_counts = {}

for i in range(1, 10): 
    count = 0
    for num in numbers:
        if num % i == 0:
            count += 1
    divisor_counts[i] = count

print(divisor_counts)