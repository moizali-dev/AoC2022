# Part 1
from directory import DirectoryNode, FileNode

with open("day7input.txt") as f:
    
    prev_dir = None
    nodes_lst = []
    node_name = None
    dir_test = []

    for line in f:
        line_input = line.rstrip()

        if "$ cd" in line_input:
            if node_name != "/" and node_name != '..' and node_name != None:
                curr_dir.child = nodes_lst

            node_name = line_input[5:]
            dir_test.append(node_name)

            if node_name != "/" and node_name != '..':
                # curr_dir.child = nodes_lst
                for child in curr_dir.child:
                    if type(child) == DirectoryNode and child.name == node_name:
                        prev_dir = curr_dir
                        curr_dir = child

                curr_dir.prev = prev_dir
                

            elif node_name != "/" and node_name == '..':
                curr_dir = curr_dir.prev

            else:             
                curr_dir = DirectoryNode(node_name)

            nodes_lst = []
            add_list = False

        if add_list == True:
            
            # Check if its is a directory or file
            if "dir" in line_input:
                node_name = line_input[4:]
                dir = DirectoryNode(node_name)
                nodes_lst.append(dir)

            else:
                str_split = line_input.split(' ')
                node_size = int(str_split[0])

                if '.' in str_split:
                    str_split_file = str_split[1].split('.')
                    node_name = str_split_file[0]
                    node_extension = str_split_file[1]
                else:
                    node_name = str_split[1]
                    node_extension = ''

                file = FileNode(node_name, node_size, node_extension)
                nodes_lst.append(file)



        if "$ ls" in line_input:
            add_list = True

    curr_dir.child = nodes_lst

# set curr directory as root directory
while (curr_dir.name != '/'):
    curr_dir = curr_dir.prev


### FUNCTIONS TO TRAVERSE THROUGH THE DATA ###

def DirList(node, directory_lst = []):

        #base case
        if type(node) == DirectoryNode:
            directory_lst.append(node.id)
        
        for node in node.child:
            DirList(node, directory_lst)   

        return directory_lst

def DirSize(node, directory, sum = [], trigger_flag = False):

        #base case
        if type(node) == FileNode and trigger_flag == True:
            sum.append(node.size)
        
        if type(node) == DirectoryNode and node.id == directory:
            trigger_flag = True
        
        #recursive case
        for node in node.child:
            DirSize(node, directory, sum, trigger_flag)   

        return sum

total = 0
directory_lst = list(set(DirList(curr_dir, directory_lst= [])))
# print(len(set(directory_lst)))

for d in directory_lst:
    dir_size_tuple = d, DirSize(curr_dir, d, sum = [], trigger_flag = False)
    if sum(dir_size_tuple[1]) <= 100000:        
        total += sum(dir_size_tuple[1])

print(f'Part1 - Solution: {total}')

##################
## --- PART 2 ----
##################

total_size = sum(DirSize(curr_dir, curr_dir.id, sum = [], trigger_flag = False))
unused_space = 70000000 - total_size
space_reqd = 30000000 - unused_space

min_size_diff = 30000000
for d in directory_lst:
    dir_size_tuple = d, DirSize(curr_dir, d, sum = [], trigger_flag = False)
    if space_reqd - sum(dir_size_tuple[1]) < 0:
        if sum(dir_size_tuple[1]) < min_size_diff:
            min_size_diff = sum(dir_size_tuple[1])

print(f'Part2 - Solution: {min_size_diff}')







        

            

        