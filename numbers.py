from statistics import median, mode, multimode

numbers = [10, 20, 30, 40, 20, 50, 20]


total = sum(numbers)


average = sum(numbers) / len(numbers)


middle = median(numbers)

most_common = multimode(numbers)


print("Numbers:", numbers)
print("Sum:", total)
print("Average (Mean):", average)
print("Median:", middle)
print("Mode:", most_common)