#Import Library
import psutil
from PySide6.QtWidgets import QMainWindow, QApplication
from tkinter import messagebox
import time

#Import Modules - log.py function logmessage
from Modules.log import logmessage, logSimple
from UI.PersonalClearTools import Ui_PersonalClearTools

#**********************************************************************************************************************

def listProcesses():
    """
    Function Name: listProcesses

    How it Works:
    This function uses `psutil` to get a list of running processes, extracts their names, logs the list, and prints each process name to the log file.

    Attributes: None
    """
    process_list = []
    for process in psutil.process_iter(['name']):
        try:
            process_info = process.as_dict(attrs=['name'])
            process_name = process_info['name']
            if process_name not in process_list:
                process_list.append(process_name)
        except:
            pass
    process_list = sorted(process_list)
    logmessage("List of Processes Running")
    for process in process_list:
        logSimple(f"Process: {process}")
    logmessage("End of List of Processes Running")

#**********************************************************************************************************************

def closeProcesses(programList):
    """
    Function Name: closeProcesses

    How it Works:
    This function takes a list of program names, attempts to close matching running processes using `psutil`, and logs the success or failure of each attempt.

    Attributes:
    - programList: a list of program names that need to be closed.
    """    
    logmessage("Starting Close Process")
    for program in programList:
        for proc in psutil.process_iter():
            if proc.name() == program:
                try:                    
                    proc.kill()
                    logSimple(f"Process: {program} - Closed")
                except:
                    logSimple(f"Process: {program} - Not Closed")
    logmessage("Ending Close Process")

