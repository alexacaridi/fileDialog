"""
Program: filedialogdemo.py
Alexa 4/28/2020
GUI-based Python program that uses a file dialog and a text area to create a simple browser that allows the user to view '.py' and '.txt' files.
"""

from breezypythongui import EasyFrame
import tkinter.filedialog

class FileDialogDemo(EasyFrame):
    #demonstrates the use of a file dialog

    def __init__(self):
        #sets up window and widgets
        EasyFrame.__init__(self, title="File Dialog Demo")
        self.outputArea= self.addTextArea(text="", row=0, column=0, width=80, height=25)
        self.addButton(text="Open", row=1, column=0, command=self.openFile)

    #event handling method
    def openFile(self):
        #pops up an open file dialog, and if a file is selected,
        #displays its text in the text area and its pathname inthe title bar
        fList = [("Python files", "*.py"), ("Text files", "*.txt")]
        
        fileName = tkinter.filedialog.askopenfilename(parent = self, filetypes = fList)

        if fileName != "":
            file= open(fileName, 'r')
            text = file.read()
            file.close()
            self.outputArea.setText(text)
            self.setTitle(fileName)
def main():
    FileDialogDemo().mainloop()

main()