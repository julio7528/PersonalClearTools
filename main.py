"""
    Purpose: a GUI application to clean up computer by deleting files/folders, emptying the recycle bin, and closing programs
    Technologies used:
        PySide6 for GUI
        xml.etree.ElementTree for parsing XML file
    Main window:
        Three checkboxes for actions selection
        Three buttons: "Check Log Files", "Check XML File", and "Run"
        Progress bar and status bar to display progress and status of cleaning process
    Application structure:
        PersonalClearTools.py defines UI using Qt Designer
        main.py contains main logic
        deleteFiles.py contains mainDeleteFiles function that deletes files and folders
        closeFiles.py contains closeProcesses function that closes programs
        log.py contains log functions to write output to log file

    Form more information, please refer to the README.md file
"""

#Import Library
import xml.etree.ElementTree as ElementTree
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6 import QtWidgets
import sys, os, time
from tkinter import messagebox

#Import Modules
from Modules.deleteFiles import mainDeleteFiles, emptyRecycleBin
from Modules.log import logmessage, logStruct, logSimple
from Modules.closeFiles import listProcesses, closeProcesses
from UI.PersonalClearTools import Ui_PersonalClearTools

#UI
class MainWindow(QMainWindow, Ui_PersonalClearTools):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.vStatusBar.showMessage("Ready")
        #if click in button vBtnCheckLogFiles open file
        self.vBtnCheckLogFiles.clicked.connect(self.showLogFile)
        self.vBtnCheckXMLFile.clicked.connect(self.showXmlFile)
        self.vBtnRun.clicked.connect(self.runProcess)

    def showLogFile(self):
        #Open the Log File
        try:
            os.startfile(".\\Logs\\logStructure.txt")
            self.vStatusBar.showMessage("Log File Opened")
        except:
            messagebox.showerror("Error", "The Log File is not available")

    def showXmlFile(self):
        #Open the XML File
        try:
            os.startfile(".\\parameters.xml")
            self.vStatusBar.showMessage("XML File Opened")
        except:
            messagebox.showerror("Error", "The XML File is not available")

    def progress(self, percent, status, sleep):
        self.progressBar.setValue(percent)
        self.vStatusBar.showMessage(status)
        time.sleep(sleep)

    def runProcess(self):

        #Variables - List of Folders and List of Programs
        folderList = []
        programList = []
        root = ElementTree.parse('parameters.xml').getroot()
        MainWindow.progress(self, 5, "Getting Variable Files and Folders", 1)

        logStruct()
        #********** Main Program **********   
        logmessage("Starting the Program")  
        MainWindow.progress(self, 10, "Initializing Process", 1)

        #######Delete Files and Folders#######
        MainWindow.progress(self, 20, "Check for Delete Files", 2)
        
        if self.vCbxDeleteFiles.isChecked():
            logmessage("Delete Files is checked - Starting the Process")
            #Define Variables - List of folders
            for Folder in root.findall('Folders/Folder'):
                folderList.append(Folder.text)
                logSimple(f"Folder to Delete: {Folder.text}")
            MainWindow.progress(self, 30, "Searching for Files", 3)
            
            #Call the main function from the deleteFiles module
            if __name__ == "__main__":
                mainDeleteFiles(folderList)
            MainWindow.progress(self, 30, "Successfull Deleting Files", 3)
        else:
            logmessage("Delete Files is not checked")


        #######Empty Recycle Bin#######
        MainWindow.progress(self, 40, "Check for Empty Recycle Bin", 1)
        if self.vCbxEmptyRecycleBin.isChecked():
            logmessage("Empty Recycle Bin is checked")
            emptyRecycleBin()
            MainWindow.progress(self, 500, "Successfull Emptying Recycle Bin", 1)
        else:
            logmessage("Empty Recycle Bin is not checked")


        #######Close Programs#######
        MainWindow.progress(self, 60, "Check for Close Programs", 1)
        if self.vCbxClosePrograms.isChecked():            
            logmessage("Close Programs is checked")  
            #List of Processes Running and Close the Program
            listProcesses()
            MainWindow.progress(self, 70, "List of Processes Running", 1)
            if self.vCbxClosePrograms.isChecked():
                for File in root.findall('Files/File'):
                    programList.append(File.text)
                    logSimple(f"Program to Close: {File.text}")
            MainWindow.progress(self, 80, "Closing Programs", 1)
            #Call the main function from the closeFiles module
            if self.vCbxClosePrograms.isChecked():
                if __name__ == "__main__":
                    closeProcesses(programList)
            MainWindow.progress(self, 90, "Successfull Closing Programs", 1)

        else:
            logmessage("Close Programs is not checked")

        MainWindow.progress(self, 100, "Process Completed", 1)
        messagebox.showinfo("Information", "The Process has been completed - check the log file")
        #********** End of Main Program **********
        logmessage("Ending the Program")
        logStruct()

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

"""
Personal Clear Tools is a graphical user interface application that allows users to clean up their computer by deleting files and folders, 
emptying the recycle bin, and closing programs.

This application uses PySide6 for the GUI and xml.etree.ElementTree for parsing an XML file containing the list of files and folders to delete, 
and programs to close.

The main window of the application contains the following elements:
- Three checkboxes to select which actions to perform: delete files and folders, empty the recycle bin, and close programs.
- Three buttons:
    - "Check Log Files" button to open the log file where the program's output is stored.
    - "Check XML File" button to open the XML file where the list of files and folders to delete, and programs to close are defined.
    - "Run" button to start the cleaning process.

The application also contains a progress bar and a status bar that display the progress and status of the cleaning process.

The application is structured in the following way:
- The UI is defined in the PersonalClearTools.py file using Qt Designer.
- The main logic is defined in the main.py file.
- The deleteFiles.py file contains the mainDeleteFiles function that deletes files and folders.
- The closeFiles.py file contains the closeProcesses function that closes programs.
- The log.py file contains the log functions that write the program's output to a log file.

To run the program, simply execute the main.py file.
Be careful in the use of this program, it can delete important files and close programs that are in use.
The program is provided as-is, without any warranty. Use at your own risk.
"""