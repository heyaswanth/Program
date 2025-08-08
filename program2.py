a = int(input("Enter a number: "))


odd_numbers = []
for i in range(1, a + 1):
    odd_numbers.append(2 * i - 1)


print(f"input = {a},then Output:", ", ".join(map(str, odd_numbers)))