import re

with open('input.txt') as file:
    payload=file.readlines()

memory = 0
for s in payload:
    if mem := re.findall('[0-9]+', s):
        memory += int(mem[0])

print(memory)