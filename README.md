# PersonalClearTools
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
	
To run: execute main.py file

Caution: use at your own risk as it can delete important files and close programs in use. No warranty provided.
