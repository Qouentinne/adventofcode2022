with open('input.txt') as file:
    payload = file.readlines()
    data = [s.strip('\n') for s in payload]

def add_visible_trees_coord(coord_sets: set, line: list | str, x: int | None=None, y: int | None=None) -> set :
    max_size_buffer = -1
    for i in range(len(line)):
        if int(line[i]) > max_size_buffer:
            coord_sets.add((x, i)) if type(x)==int else coord_sets.add((i, y))
            max_size_buffer = int(line[i])
        if int(line[i]) == 9:
            break
    
    max_size_buffer = -1
    for i in range(len(line)-1, 0, -1):
        if int(line[i]) > max_size_buffer:
            coord_sets.add((x, i)) if type(x)==int else coord_sets.add((i, y))
            max_size_buffer = int(line[i])
        if int(line[i]) == 9:
            break

    return coord_sets

def parse_visible_trees(data: list) -> set:
    visible_trees_coordinates = set()
    for i, line in enumerate(data):
        visible_trees_coordinates = add_visible_trees_coord(coord_sets=visible_trees_coordinates, line=line, x=i)
    for j in range(len(data[0])):
        col = [line[j] for line in data]
        visible_trees_coordinates=add_visible_trees_coord(coord_sets=visible_trees_coordinates, line=col, y=j)
    return visible_trees_coordinates

### 2nd star ###

def get_tree_size(tree_pos: tuple, data: list) -> int:    
    return int(data[tree_pos[0]][tree_pos[1]])

def get_n_lower_trees(row: list|str) -> int:
    """Returns number of values until equal or bigger is found. Reference height must be at row's index 0"""
    n = 0
    for h in row[1:]:
        if int(h) < int(row[0]):
            n+=1
        else:
            return n+1
    return n    

def get_scenic_score(tree_pos: tuple, data: list) -> int:
    """For a given tree at position tree_pos in forest described by data return scenic score"""
    x, y = tree_pos
    tree_size = get_tree_size(tree_pos, data)
    line = list(data[x])
    col = [t[y] for t in data]

    view_lines = [col[0:x+1][::-1], col[x:], line[0:y+1][::-1], line[y:]]
    dist_views = [0, 0, 0, 0] #init distance view in all 4 directions
    
    for i, view_l in enumerate(view_lines):
        dist_views[i] = get_n_lower_trees(view_l)
        
    return dist_views[0]*dist_views[1]*dist_views[2]*dist_views[3]        

def get_max_scenic_score(data: list) -> int:
    max_scenic_score = 0
    max_loc = (0,0)
    for i in range(len(data)):
        for j in range(len(data[0])):
            curr_score = get_scenic_score((i,j), data)
            if curr_score > max_scenic_score:
                max_scenic_score = curr_score
                max_loc = (i,j)
    print(max_loc)
    return max_scenic_score

#print(get_scenic_score((7,51), data))
print(get_max_scenic_score(data))



