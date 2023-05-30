import os


class FileSearch:
    def __init__(self, fileName, rootDir=None):
        self.fileName = fileName
        self.rootDir = rootDir
        
    def Search(self, advanced=False):
        if not self.rootDir:
            self.rootDir = os.getcwd()
        walked = os.walk(self.rootDir)
        advancedResult = []
        
        for path, _, files in walked:
            if self.fileName in files and not advanced:
                result = [f"{path}/{self.fileName}"]
                return result
                
            if self.fileName in files and advanced:
                result = f"{path}/{self.fileName}"
                advancedResult.append(result)
        return advancedResult