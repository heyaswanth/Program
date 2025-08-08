a = int(input("Enter a number: "))

for i in range(1, a + 1):
    output = []
    for j in range(1, i + 1):
        output.append(str(2 * j - 1))
    print(f"Input a = {i}, then output: {', '.join(output)}")