with open("input.txt", mode='r') as file:
    contents = file.read()
    #list = file.readlines()
    data = contents.split('\n\n')
    data = [s.split('\n') for s in data]

    end_data = []
    
    for l in data:
        end_data.append(sum([int(val) for val in l]))

    best3 = [end_data[0], end_data[1], end_data[2]]
    best3.sort()
    for val in end_data[3:]:
        if val > best3[0]:
            best3[0] = val
            best3.sort()




    print(best3)
    print(sum(best3))
