import uuid
class DirectoryNode:

    def __init__(self, name:str) -> None:
        self.name = name
        self.child = []
        self.prev = None
        self.id = uuid.uuid1()


class FileNode(DirectoryNode):

    def __init__(self, name, size:int, extension:str) -> None:
        super().__init__(name)
        self.size = size
        self.extension = extension

class ParseInput:

    def __init__(self) -> None:
        pass
  
    def readfile(self, file):
        
        with open(file) as f:

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

        return curr_dir









    

        
