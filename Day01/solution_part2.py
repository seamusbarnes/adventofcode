def main():
    # filename = 'test_input_part2.txt'
    filename = 'Day01_input.txt'

    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]

    def parse_line(line):

        numDict = {'one': 1,
                   'two': 2,
                   'three': 3,
                   'four': 4,
                   'five': 5,
                   'six': 6,
                   'seven': 7,
                   'eight': 8,
                   'nine': 9}

        def char_num(line, i):
            num = None
            for key in numDict.keys():
                if i < len(line)-len(key)+1:
                    word = line[i:i+len(key)]
                    if word == key:
                        num = numDict[key]
            if num is not None:
                return num
            else: return None
        
        def is_num(c):
            if ord('0') <= ord(c) <= ord('9'):
                return True
            return False
        
        def get_first_last(line):
            first, last = None, None
            for i in range(len(line)):
                if is_num(line[i]):
                    if first == None:
                        first = int(line[i])
                    else:
                        last = int(line[i])
                else:
                    num = char_num(line, i)
                    if num is not None:
                        if first == None:
                            first = num
                        else:
                            last = num
            if last == None:
                last = first

            return first, last
        
        first, last = get_first_last(line)
        return (first, last)
        
    nums = []
    for i in range(len(lines)):
        first, last = parse_line(lines[i])
        nums.append((first*10)+last)

    print(sum(nums))
if __name__ == '__main__':
    main()