file = open("numbers.txt", "r")
nums = list(map(int, file.read().split()))

avg = sum(nums) / len(nums)
print("Average =", avg)

file.close()
