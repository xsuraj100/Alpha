nums = list(map(int, input("Enter numbers: ").split()))

even_file = open("even.txt", "w")
odd_file = open("odd.txt", "w")

for n in nums:
    if n % 2 == 0:
        even_file.write(str(n) + " ")
    else:
        odd_file.write(str(n) + " ")

even_file.close()
odd_file.close()
