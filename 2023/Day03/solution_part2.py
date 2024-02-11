def main():
    filename = 'Day03_input.txt'
    filename = 'test_input.txt'

    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]

    # del lines[-1]
        
    def is_number(c):
        if ord('0') <= ord(c) <= ord('9'):
            return True
        return False
    
    def find_number(lines, row, col, ROWS, COLS):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= row + i < ROWS and 0 <= col < COLS:
                    if is_number(lines[row+i][col+j]):
                        number = build_number(lines, row+i, col+j, ROWS, COLS)
    
    def number_to_int(number):
        num = 0
        for i, n in enumerate(reversed(number)):
            num += int(n)*10**i
        return num


    def build_number(lines, row, col, ROWS, COLS):
        line = lines[row]
        l, r = col, col
        while 0 <= l < COLS and is_number(line[l]):
            l -= 1
        while 0 <= r < COLS and is_number(line[r]):
            r += 1
        
        number =line[l+1:r]
        number = number_to_int(number)
        print(number)
        return number


    ROWS, COLS = len(lines), len(lines[0])
    for row in range(ROWS):
        for col in range(COLS):
            if lines[row][col] == '*':
                find_number(lines, row, col, ROWS, COLS)




if __name__ == '__main__':
    main()