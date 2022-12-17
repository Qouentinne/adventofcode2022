with open('input.txt') as file:
    raw = file.readlines()
    payload = [line.strip() for line in raw]

x = 1
turns_check = [20, 40, 60, 100, 140, 180, 220]
sum_x = 0

for n, instr in enumerate(payload):
    n+=1
    instr = instr.split(" ")
    if instr[0] == "addx":
        

