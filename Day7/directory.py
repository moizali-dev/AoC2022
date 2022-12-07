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
        self.prev = None







    

        
