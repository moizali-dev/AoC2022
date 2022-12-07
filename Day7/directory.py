class DirectoryNode:

    def __init__(self, name:str) -> None:
        self.name = name
        self.child = []
        self.prev = None


class FileNode(DirectoryNode):

    def __init__(self, name, size:int, extension:str) -> None:
        super().__init__(name)
        self.size = size
        self.extension = extension
        self.prev = None

# if __name__=="__main__":

#     # Input in data structure

#     prev_dir = None
#     curr_dir = DirectoryNode("\\")
#     print(curr_dir.name)
#     curr_dir.child = [DirectoryNode('a'), FileNode('b', 14848514, 'txt'), FileNode('c', 8504156, 'dat'), DirectoryNode('d')]

#     for child in curr_dir.child:
#         if type(child) == DirectoryNode and child.name == 'a':
#             prev_dir = curr_dir
#             curr_dir = child
            

#     curr_dir.prev = prev_dir
#     curr_dir.child = [DirectoryNode('e'), FileNode('f', 29116, ''), FileNode('g', 2557, ''), FileNode('h', 62596, 'lst')]

#     for child in curr_dir.child:
#         if type(child) == DirectoryNode and child.name == 'e':
#             prev_dir = curr_dir
#             curr_dir = child

#     curr_dir.prev = prev_dir
#     curr_dir.child = [FileNode('i', 584, '')]

#     curr_dir = curr_dir.prev
#     curr_dir = curr_dir.prev


#     for child in curr_dir.child:
#         if type(child) == DirectoryNode and child.name == 'd':
#             prev_dir = curr_dir
#             curr_dir = child

#     curr_dir.prev = prev_dir
#     curr_dir.child = [FileNode('j', 4060174, ''), FileNode('d', 8033020, 'log'), FileNode('d', 5626152, 'ext'), FileNode('k', 7214296, '')]

#     # Come back to root directory
#     curr_dir = curr_dir.prev

#     # find directories
#     def DirList(node, directory_lst = []):

#         #base case
#         if type(node) == DirectoryNode:
#             directory_lst.append(node.name)
        
#         for node in node.child:
#             DirList(node, directory_lst)   

#         return directory_lst

#     # Find size of a directory

#     def DirSize(node, directory, sum = [], directory_size = {}):

#         #base case
#         if type(node) == FileNode:
#             sum.append(node.size)
    
        
#         for node in node.child:
#             print(node.name, type(node))
#             DirSize(node, directory, sum,directory_size)   
#             print(node.name, type(node))
#             print(node.prev)
#             if type(node.prev) == DirectoryNode:
#                 directory_size[node.name] = sum
#                 sum = []

#         return directory_size

# DirSize(curr_dir, 'a', sum = [], directory_size = {})

    # directory_lst = DirList(curr_dir, directory_lst= [])
    # for d in directory_lst:
    #     print(DirSize(curr_dir, d, sum = [], trigger_flag = False))







    

        
