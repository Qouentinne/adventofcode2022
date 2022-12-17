from math import sqrt

with open('input.txt') as file:
    raw = file.readlines()
    data = [l.strip() for l in raw]

def make_order_explicit(raw_order: str):
    return tuple(raw_order.split(" "))

def head_move_rules(instr: str):
    match instr:
        case 'L':
            return [-1, 0]
        case 'U':
            return [0, 1]
        case 'R':
            return [1, 0]
        case 'D':
            return [0, -1]

def dist_head_tail(head_pos, tail_pos):
    return sqrt((head_pos[0] - tail_pos[0])**2 + (head_pos[1] - tail_pos[1])**2)


def tail_move(head_pos: list, tail_pos: list):
    for i in (0, 1):
        if tail_pos[i] != head_pos[i]:
            tail_pos[i] += 1 if head_pos[i] > tail_pos[i] else -1
    return tail_pos

## INIT ##
head_pos = [0,0]
tail_pos = [0,0]
tail_pos_log = {(0, 0)}
rope = [[0,0] for n in range(10)]

## MOVES ##

## 1st star ##
# for order in data:
#     order = make_order_explicit(order)
#     for rep in range(int(order[1])):
#         head_pos = [sum(n) for n in zip(head_pos, head_move_rules(order[0]))]
#         if dist_head_tail(head_pos, tail_pos) >= 2:
#             tail_pos = tail_move(head_pos, tail_pos)
#             tail_pos_log.add(tuple(tail_pos))

## 2nd star ##
for order in data:
    order = make_order_explicit(order)
    for rep in range(int(order[1])):
        rope[0] = [sum(n) for n in zip(rope[0], head_move_rules(order[0]))]
        for i in range(1, len(rope)):
            if dist_head_tail(rope[i-1], rope[i]) >=2:
                rope[i] = tail_move(rope[i-1], rope[i])
        tail_pos_log.add(tuple(rope[-1]))

print(len(tail_pos_log))