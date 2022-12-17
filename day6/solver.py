with open('input.txt') as file:
    payload = file.read()

for i in range(len(payload)):
    if len(payload[i:i+14]) == len(set(payload[i:i+14])):
        print(str(payload[i:i+14]))
        print(i+14)
        break

