# Part 1
from utils import DirectoryNode, FileNode, ParseInput

Pi = ParseInput()
curr_dir = Pi.readfile("day7sampleinput.txt")

#############################################
### FUNCTIONS TO TRAVERSE THROUGH THE DATA ##
#############################################

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

##################
## --- PART 1 ----
##################

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







        

            

        