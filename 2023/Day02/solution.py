def main():
    filename = 'test_input_part1.txt'

    with open(filename, 'r') as file:
        lines = [line for line in file]

    allowed = {'red': 12,
                'green': 13,
                'blue': 14}

    nums = []

    def calculate_valid(rounds, game):
        
        valid = True
        
        for round in rounds:
            for cubes in round.split(','):

                count, cube = cubes.split(' ')[1:]      
                
                if int(count) > allowed[cube.split()[0]]:
                    valid = False
        
        if valid == False: return
        else: nums.append(int(game))

    for line in lines:
        game = line.split(':')[0].split(' ')[1]
        rounds = line.split(':')[1].split(';')

        calculate_valid(rounds, game)

    print(sum(nums))

if __name__ == '__main__':
    main()