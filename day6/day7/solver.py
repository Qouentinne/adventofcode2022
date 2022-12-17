import re
with open('input.txt') as file:
    payload=file.readlines()

file_path=[]
file_sizes=[]
used_memory=0 #2nd star
directory_to_delete_sizes=[] #2nd star
memory_size=0 #1st star

for line in payload:
    if str(line[:4]) == "$ cd":
        if str(line[5:7]) == "..":
            memory_size += file_sizes[-1] if file_sizes[-1]<=100_000 else 0 #1st star
            directory_to_delete_sizes.append(file_sizes[-1])
            file_sizes.pop()
            file_path.pop()
        else:
            file_path.append(str(line[5:]))
            file_sizes.append(0)
    if size_file_match := re.search('[0-9]+', line):
        file_sizes = [size + int(size_file_match.group()) for size in file_sizes]
        used_memory += int(size_file_match.group())

total_size_to_delete = 30000000 - (70000000 - used_memory)

possible_size_directory_to_delete = (s for s in directory_to_delete_sizes if s>=total_size_to_delete)
size_to_delete = next(possible_size_directory_to_delete)
for s in possible_size_directory_to_delete:
    if s < size_to_delete: 
        size_to_delete = s

print(f"""
Total memory size = 70 000 000
Total files size = {used_memory}
Space to free = {total_size_to_delete}
Min repertory size to delete = {size_to_delete}
""")