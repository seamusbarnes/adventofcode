def main():
    filename = 'Day03_input.txt'

    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]

    if not lines:
        print("The file is empty or does not exist.")
        return

    # Assuming the last line is not needed as per your original logic
    del lines[-1]

    def is_num(c):
        return ord('0') <= ord(c) <= ord('9')

    def is_valid(lines, row, col, ROWS, COLS):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= row + i < ROWS and 0 <= col + j < COLS:
                    if not is_num(lines[row + i][col + j]) and lines[row + i][col + j] != '.':
                        return True
        return False

    def create_number(array):
        return sum(digit * 10**i for i, digit in enumerate(reversed(array)))

    nums = []
    ROWS, COLS = len(lines), len(lines[0])

    for row in range(ROWS):
        temp, valid = [], False
        for col in range(COLS):
            if is_num(lines[row][col]):
                temp.append(int(lines[row][col]))
                if valid is False:
                    valid = is_valid(lines, row, col, ROWS, COLS)
            else:
                if valid and temp:
                    nums.append(temp)
                valid, temp = False, []

        # Check if the last number in the row is valid and should be added
        if valid and temp:
            nums.append(temp)

    # Convert arrays of numbers into actual numbers and sum them
    total = sum(create_number(num) for num in nums)

    print(total)


if __name__ == '__main__':
    main()
