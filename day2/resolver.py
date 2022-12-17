MATCHER = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors',
}

MATCHER2 = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 0,
    'Y': 3,
    'Z': 6,
}

SCORING = {
    'Rock':[1,
            {
                'Rock': 3,
                'Paper': 0,
                'Scissors': 6,    
            }
        ],
    'Paper':[2,{
                'Rock': 6,
                'Paper': 3,
                'Scissors': 0,    
            }],
    'Scissors':[3,{
                'Rock': 0,
                'Paper': 6,
                'Scissors': 3,    
            }]
}


with open('input.txt') as file:
    a = file.read().splitlines()
    payload = [s.replace(" ", "") for s in a]

result = 0

# --- 1st star ---
# for dual in payload:
#     match = [MATCHER[dual[0]], MATCHER[dual[1]]]
#     result += SCORING[match[1]][0] + SCORING[match[1]][1][match[0]]


# --- 2nd star ---
for dual in payload:
    outcome = MATCHER2[dual[1]] #Outcome of duel (pts)
    result += outcome
    dic = SCORING[MATCHER[dual[0]]][1] #Get the dictionary related to other player sign
    for key, val in dic.items(): #Given the outcome, what was played (and what score did it give)
        if val == abs(outcome - 6): #SCORING is made to match my result w/ other player, the small calculation make it work the other way around            
            result += SCORING[key][0]
            break

print(result)
    
    




