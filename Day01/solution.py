def main():
    filename = "Day01_input.txt"
    # filename = 'test_input.txt'

    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]

    def isNum(c):
        if ord('0') <= ord(c) <= ord('9'):
            return True
        return False

    def parse_line(line):
        first, last = None, None
        for c in line:
            if isNum(c):
                if first == None:
                    first = int(c)
                else:
                    last = int(c)
            if last == None:
                last = first
        return (first, last)
    
    nums = []
    for line in lines:
        first, last = parse_line(line)
        nums.append((first*10)+last)
    
    print(sum(nums))

if __name__ == '__main__':
    main()