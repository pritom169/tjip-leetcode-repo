class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.contents = []
        self.is_file = False

class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    # TC: O(M + N) for mkdir and readContentFromFile
    # M = The lenth of the path or lenth of the filepath
    # N = Depth of the last layer
    # First we need O(M) time complexity to split the filepath
    # Second we need O(N) time complexity to fo N layer deep which
    # is the last directory.

    # SC: O(N), N = Depth of the last layer.
    # In the worst case, we need to create N layer
    # every single time when those functions are called.

    def ls(self, path: str) -> List[str]:
        node = self.root
        for directory in path.split('/'):
            if not directory: continue
            if directory not in node.children:
                return []
            node = node.children[directory]
        return [directory] if node.is_file else sort(node.children.keys())
    
    # TC: O(M + N) for mkdir and readContentFromFile
    # M = The lenth of the path or lenth of the filepath
    # N = Depth of the last layer
    # First we need O(M) time complexity to split the filepath
    # Second we need O(N) time complexity to fo N layer deep which
    # is the last directory.

    # SC: O(N), N = Depth of the last layer.
    # In the worst case, we need to create N layer
    # every single time when those functions are called.

    def mkdir(self, path: str) -> None:
        self.navigateToDirectory(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.navigateToDirectory(filePath)
        node.is_file = True
        node.contents.append(content)

    # TC: O(M + N + C), M = The lenth of the path or lenth of the filepath
    # N = Depth of the last layer, C = Number of contents in the given directory.
    # First we need O(M) time complexity to split the filepath
    # Second we need O(N) time complexity to go N layer deep which
    # is the last directory.
    # Third, O(C) complexity for adding all the contents in the string

    # SC: O(C), C = Number of contents into the particular directory
    # Since, we do not need to create any new layer the only space 
    # complexity this function has is length of the content.

    def readContentFromFile(self, filePath: str) -> str:
        node = self.navigateToDirectory(filePath)
        return "".join(node.contents)
    
    def navigateToDirectory(self, filePath: str):
        node = self.root
        for directory in filePath.split('/'):
            if not directory: continue
            node = node.children[directory]
        return node


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
