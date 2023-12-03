amount = int(input())
half = amount // 2
if amount % 2 == 1:
    half += 1
numbers = sorted([int(i) for i in input().split()])
high_nums = numbers[:half][::-1]
low_nums = numbers[half:]

output = []
for i in range(half):
    output.append(str(high_nums[i]))
    output.append(str(low_nums[i]))

print(" ".join(output))

