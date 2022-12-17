#import data + strip format
with open('input.txt') as file:
    file_list = file.readlines()
    payload = [s.strip() for s in file_list]

data = [s.split(",") for s in payload]

data_1st_star = [[s[0].split("-"), s[1].split("-")]for s in data]
for s in data_1st_star:
    for ss in s:
        ss[0], ss[1] = int(ss[0]), int(ss[1])
print(data_1st_star)



def first_star(data):
    full_pair_overlap = 0
    for s in data:
        first_range, second_range = s[0], s[1]
        if (first_range[0]<=second_range[0] and first_range[1]>=second_range[1]) or (first_range[0]>=second_range[0] and first_range[1]<=second_range[1]):
            full_pair_overlap +=1
    return full_pair_overlap
        

def second_star(data):
    partial_pair_overlap = len(data)
    for s in data:
        first_range, second_range = s[0], s[1]
        if first_range[1] < second_range[0] or second_range[1] < first_range[0]:
            partial_pair_overlap -=1
    return partial_pair_overlap


print(second_star(data_1st_star))



