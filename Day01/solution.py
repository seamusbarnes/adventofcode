filename = "Day01_input.txt"
# filename = 'test_input.txt'

with open(filename, 'r') as file:
    lines = [line.strip() for line in file]

def isNum(c):
    if ord('0') <= ord(c) <= ord('9'):
        return True
    return False

nums = []
for line in lines:
    first, last = None, None
    for c in line:
        if isNum(c):
            if first == None:
                first = int(c)
            else:
                last = int(c)
    if last == None:
        last = first

    num = (first*10)+last
    nums.append(num)

res = sum(nums)

print(res)