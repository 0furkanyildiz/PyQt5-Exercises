# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import string
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 421)
        MainWindow.setMinimumSize(QtCore.QSize(690, 421))
        MainWindow.setMaximumSize(QtCore.QSize(690, 421))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, -10, 381, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 60, 347, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.uppercase_check = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.uppercase_check.setFont(font)
        self.uppercase_check.setObjectName("uppercase_check")
        self.gridLayout.addWidget(self.uppercase_check, 3, 1, 1, 1)
        self.number_check = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.number_check.setFont(font)
        self.number_check.setObjectName("number_check")
        self.gridLayout.addWidget(self.number_check, 2, 1, 1, 1)
        self.special_check = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.special_check.setFont(font)
        self.special_check.setObjectName("special_check")
        self.gridLayout.addWidget(self.special_check, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.length_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.length_edit.setFont(font)
        self.length_edit.setObjectName("length_edit")
        self.gridLayout.addWidget(self.length_edit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lowercase_check = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lowercase_check.setFont(font)
        self.lowercase_check.setObjectName("lowercase_check")
        self.gridLayout.addWidget(self.lowercase_check, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.push_button = QtWidgets.QPushButton(self.centralwidget)
        self.push_button.setGeometry(QtCore.QRect(90, 340, 201, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.push_button.setFont(font)
        self.push_button.setObjectName("push_button")

        self.push_button.clicked.connect(self.generate_password) # Connecting the action of the push button to the function that generates a new password

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(400, 60, 271, 90))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.output = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.output.setFont(font)
        self.output.setObjectName("output")

        self.output.setReadOnly(True)                       # Setting the output line to read only so that it cannot be changed

        self.verticalLayout.addWidget(self.output)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Password Generator"))
        self.uppercase_check.setText(_translate("MainWindow", "(e.g. T, A)"))
        self.number_check.setText(_translate("MainWindow", "(e.g. 1, 6)"))
        self.special_check.setText(_translate("MainWindow", " (e.g. ?, %)"))
        self.label_5.setText(_translate("MainWindow", "Uppercase Letters:"))
        self.label_6.setText(_translate("MainWindow", "Lowercase Letters:"))
        self.label_3.setText(_translate("MainWindow", "Special Characters:   "))
        self.label_4.setText(_translate("MainWindow", "Numbers:"))
        self.lowercase_check.setText(_translate("MainWindow", "(e. g. r, t)"))
        self.label_2.setText(_translate("MainWindow", "Length: "))
        self.push_button.setText(_translate("MainWindow", "Generate New Password"))
        self.label_7.setText(_translate("MainWindow", "Your New Password"))

    def generate_password(self):           

        include_uppercase = self.uppercase_check.isChecked()        # Taking inputs from the user
        include_lowercase = self.lowercase_check.isChecked()
        include_special = self.special_check.isChecked()
        include_number = self.number_check.isChecked()
        length_input = self.length_edit.text()

        setting_list = [include_lowercase, include_uppercase, include_number, include_special]  # List to check the number of True values

        if length_input == "":
            print("Do not leave the length input empty") 

        if setting_list.count(True) < 1:                    # User should tick at least one checkbox
            print("Tick at least one")

        else:
            if length_input.isdigit():                      # Checking whether the length input is an integer or not
                length_input = int(length_input)
                if length_input > 50:
                    print("Length cannot be bigger than 50")
                elif length_input < 1:
                    print("Length cannot be smaller than 1")
                elif setting_list.count(True) > length_input:   # A password cannot be generated if the desired length is less than the number of the checked boxes
                    print("Increase your desired length or undone some of your choices.")
                else:
                    generator.new_password(include_uppercase, include_lowercase, include_special, include_number, length_input) # A new password is generated if the conditions are OK
            else:
                if length_input.lstrip("-").isdigit():         
                    print("Length cannot be negative")
                else:
                    print("Length should be an integer")
        
    def give_output(self, output):
        self.output.setText(output)                 # Changing the text in the output line

class Password():                                   # Class to handle the generation of the password only
    def __init__(self):
            
        self.uppercase = string.ascii_uppercase     # All posibilities of the strings are retrieved from the string module
        self.lowercase = string.ascii_lowercase
        self.numbers = string.digits
        self.specials = string.punctuation

    def new_password(self, include_uppercase, include_lowercase, include_special, include_number, length_input):
        
        self.characters = ""            # String which contains all of the possible choices of characters
        self.pwd = ""                   # Core password

        """
        Below, we make sure that our password contains at least one of the choices.
        We also add all of our options to the characters string so that we can complete the whole password.
        """

        if include_uppercase:
            self.pwd += random.choice(self.uppercase)
            self.characters += self.uppercase
        if include_lowercase:
            self.pwd += random.choice(self.lowercase)
            self.characters += self.lowercase
        if include_special:
            self.pwd += random.choice(self.specials)
            self.characters += self.specials
        if include_number:
            self.pwd += random.choice(self.numbers)
            self.characters += self.numbers

        if len(self.pwd) < length_input:                
            self.create_password(length_input)
        else:                  # If the length of the password is already satisfied, there is no need to complete the core password
            self.send_password()
        
    def create_password(self, desired_length):        

        while len(self.pwd) < desired_length:               # We add new random characters from our string that contains all possible characters we can use until we reach the desired length
            new_char = random.choice(self.characters)
            self.pwd += new_char
        
        self.send_password()

    def send_password(self):            # Since we created the core password to a certain order, we should shuffle our last password
        char_list = list(self.pwd)      
        random.shuffle(char_list)
        self.pwd = "".join(char_list)
        ui.give_output(self.pwd)        

if __name__ == "__main__":
    import sys
    generator = Password()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())