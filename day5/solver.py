with open("initial_state.txt") as file:
    payload = file.readlines()

data = payload[:-1][::-1]
data_list = []
for i in range(len(data[0])): 
    buffer_list = [s[i] for s in data if s[i] not in ("[", " ", "]", "\n")]
    if buffer_list != []:
        data_list.append(buffer_list)

with open("input.txt") as file:
    raw_instructions = file.readlines()


instructions = [line.replace("move ","").replace(" from","").replace("to ","").split() for line in raw_instructions]

### First Star Process ###
# for instruction in instructions:
#     for _ in range(int(instruction[0])):
#         data_list[int(instruction[2])-1].append(data_list[int(instruction[1])-1].pop())
        
### Second Star Process ###
for instruction in instructions:
    ncrates = int(instruction[0])
    giving_pile = data_list[int(instruction[1])-1]
    receiving_pile = data_list[int(instruction[2])-1]   

    receiving_pile += giving_pile[-ncrates:]
    data_list[int(instruction[1])-1] = giving_pile[:-ncrates]

result = [pile.pop() for pile in data_list if len(pile)>0]
print(''.join(result))