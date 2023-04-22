#Import Library
import os, traceback, subprocess

#Import Modules - log.py funtion logmessage
from Modules.log import logmessage, logSimple

class DeleteFiles:
    """
    Class Name: DeleteFiles
    How it Works: This class takes a list of folder paths and deletes all files and subfolders within
    each folder using the `_privateMethod()` function. The `publicMethod()` function is a wrapper
    that calls the `_privateMethod()` function.
    Attributes: - folderList: a list of folder paths to delete files and subfolders from.
    """
    def __init__(self, folderList):
        self.folderList = folderList

    def _privateMethod(self):
        """
        Function Name: _privateMethod
        How it Works: This is a private function that iterates over each folder in the `folderList` attribute and deletes all files and subfolders
        using `os.walk()` and `os.remove()` or `os.rmdir()`, respectively. It logs the success or failure of each deletion attempt using the
        `logSimple()` function from the `log` module.
        Attributes: None
        """
        for item in self.folderList:
            logSimple(f"Folder: {item}")                
            for root, dirs, files in os.walk(item, topdown=False):
                for name in files:
                    try:
                        os.remove(os.path.join(root, name))
                        logSimple(f"File: {name} - Deleted")
                    except Exception as e:
                        logmessage(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
                        print(e)
                for name in dirs:
                    try:
                        os.rmdir(os.path.join(root, name))
                        logSimple(f"Folder: {name} - Deleted")
                    except Exception as e:
                        logmessage(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
                        print(e)                
                
    def publicMethod(self):
        self._privateMethod()

def mainDeleteFiles(folderList):
    """
    Function Name: mainDeleteFiles
    How it Works: This function is the main entry point for the `DeleteFiles` class. 
    It takes a list of folder paths, instantiates the `DeleteFiles` class, and calls the `publicMethod()` 
    function to delete all files and subfolders within each folder.
    Attributes: - folderList: a list of folder paths to delete files and subfolders from.
    """
    try:
        logmessage("Starting Delete Files")
        deleteFiles = DeleteFiles(folderList)
        deleteFiles.publicMethod()
        logmessage("Ending Delete Files")
    except Exception as e:
        logmessage(f"An Error Ocurred While Executing the File: {os.path.basename(__file__)} - Message: {e} - Line: {traceback.extract_tb(e.__traceback__)[0][1]}")
        print(e)
        
def emptyRecycleBin():
    """
    Function Name: emptyRecycleBin
    How it Works: This function uses `subprocess` to run a PowerShell command that empties the Recycle Bin. 
    It logs the success or failure of the attempt using the `logSimple()` function from the `log` module.
    Attributes: None
    """
    
    logmessage("Starting Empty Recycle Bin")
    try:
        powershell_cmd = "Clear-RecycleBin -Force"
        process = subprocess.Popen(["powershell", "-Command", powershell_cmd], stdout=subprocess.PIPE)
        result = process.communicate()[0]
        logSimple(f"Recycle Bin - Emptied = {result}")
    except:
        logSimple("Recycle Bin - Not Emptied")
    logmessage("Ending Empty Recycle Bin")