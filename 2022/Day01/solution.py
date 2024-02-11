def main():
    filename = 'input.txt'

    with open(filename, 'r') as file:
        output = [line.strip() for line in file]

    def isNum(string):
        try:
            num = int(string)
            return True
        except:
            return False

    def countCalories(output):    
        temp = []
        elves = []
        for number in output:
            if isNum(number):
                temp.append(int(number))
            else:
                elves.append(temp)
                temp = []
        
        return elves

    def findMax(elves):
        cur_max = 0
        for elf in elves:
            temp_max = sum(elf)
            cur_max = max(cur_max, temp_max)
        return cur_max

    elves = countCalories(output)
    cur_max = findMax(elves)
    print(f'Max calories: {cur_max}')  

    def topThreeMaxes(elves):
        cur_maxxes = [sum(elves[0]), sum(elves[1]), sum(elves[2])]
        for elf in elves[2:]:
            if sum(elf) > min(cur_maxxes):
                temp1 = max(cur_maxxes)
                temp2 = max([x for x in cur_maxxes if x < temp1])
                cur_maxxes = [temp1, temp2, sum(elf)]
        return cur_maxxes

    cur_maxxes = topThreeMaxes(elves)
    print(sum(cur_maxxes))



if __name__ == '__main__':
    main()