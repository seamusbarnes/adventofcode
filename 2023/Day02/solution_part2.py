def main():
    
    filename = 'Day02_input.txt'
    # filename = 'test_input.txt'

    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    
    nums = []
    for i in range(len(lines)):
        line = lines[i]
        game_id = line.split(':')[0].split(' ')[1]

        turns = line.split(':')[1].split(';')

        def get_counts(turn):
            store = {}
            for count_cube in turn.split(','):
                count, cube = count_cube.split(' ')[1:]
                store[cube] = int(count)
            return store
        
        mins = {}
        for turn in turns:
            store = get_counts(turn)
            for key, value in store.items():
                mins[key] = max(mins.get(key, float(0)), value)
        
        temp = 1
        for key, value in mins.items():
            temp = temp * value
        
        nums.append(temp)
        
    print(sum(nums))

    

if __name__ == '__main__':
    main()
