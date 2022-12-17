import string

with open('input.txt') as file:
    payload = file.readlines()

#Letter-value dict setup
    priority = 1
    PRIORITY_TABLE = {}
    for letter in string.ascii_letters:
        PRIORITY_TABLE[letter] = priority
        priority+=1

#--- 1st star ---#
def first_star(payload):
    global PRIORITY_TABLE
    #Split strings in 2 half
    data = [[s[:len(s)//2], s[len(s)//2:]]for s in payload]

    #Initiate final result
    priority = 0

    #Fetch common letter
    for l in data:
        for ll in l[0]:
            if ll in l[1]:
                priority += PRIORITY_TABLE[ll]
                break

    print(priority)  

#--- 2nd star ---#
def second_star(payload):
    global PRIORITY_TABLE

    #Initiate final result
    priority_badge_items = 0

    for i in range(0, len(payload), 3): #Check strings 3 at a time
        for l in payload[i]:
            if l in payload[i+1] and l in payload[i+2]:
                priority_badge_items += PRIORITY_TABLE[l]
                break
    
    print(priority_badge_items)
    

#--- Main ---#
#first_star(payload)
#second_star(payload)