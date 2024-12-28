from PyQt5 import QtWidgets
import sys
from calculator import Ui_Calculator

label = ""
number_1 = ""
islem = ""

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)
        self.ui.one_button.clicked.connect(self.calculate)
        self.ui.two_button.clicked.connect(self.calculate)
        self.ui.three_button.clicked.connect(self.calculate)
        self.ui.four_button.clicked.connect(self.calculate)
        self.ui.five_button.clicked.connect(self.calculate)
        self.ui.six_button.clicked.connect(self.calculate)
        self.ui.seven_button.clicked.connect(self.calculate)
        self.ui.eight_button.clicked.connect(self.calculate)
        self.ui.nine_button.clicked.connect(self.calculate)
        self.ui.zero_button.clicked.connect(self.calculate)
        self.ui.minus_button.clicked.connect(self.calculate)
        self.ui.times_button.clicked.connect(self.calculate)
        self.ui.plus_button.clicked.connect(self.calculate)
        self.ui.percent_button.clicked.connect(self.calculate)
        self.ui.equal_button.clicked.connect(self.calculate)
        self.ui.divide_button.clicked.connect(self.calculate)
        self.ui.clear_button.clicked.connect(self.calculate)
        self.ui.backspace_button.clicked.connect(self.calculate)
        self.ui.toggle_button.clicked.connect(self.calculate)
        self.ui.point_button.clicked.connect(self.calculate)
    
    def calculate(self):
        global number_1
        global islem
        global label
        sender = self.sender().text()

        if sender == "✖":
            label = ""
            islem = "✖"

            if number_1 == "":
                number_1 = self.ui.result_label.text()
                self.ui.result_label.setText("")

            else:
                self.ui.result_label.setText(str(float(number_1)*float(self.ui.result_label.text())))
        
        elif sender == "-":
            label = ""
            islem = "-"

            if number_1 == "":
                number_1 = self.ui.result_label.text()

            else:
                self.result_label.setText(str(float(number_1)-float(self.ui.result_label.text())))   
                 
        elif sender == "+":
            label = ""
            islem = "+"

            if number_1 == "":
                number_1 = self.ui.result_label.text()
                self.ui.result_label.setText("")

            else:
                self.ui.result_label.setText(str(float(number_1)+float(self.ui.result_label.text())))
        
        elif sender == "/":
            label = ""
            islem = "/"

            if number_1 == "":
                number_1 = self.ui.result_label.text()
                self.ui.result_label.setText("")

            else:
                self.ui.result_label.setText(str(float(number_1)/float(self.result_label.text())))
        
        elif sender == "%":
            label = ""
            islem = "%"

            if number_1 == "":
                number_1 = self.ui.result_label.text()
                self.ui.result_label.setText("")

            else:
                self.ui.result_label.setText(str(float(number_1)%float(self.result_label.text())))

        elif sender == "=":
            if islem == "✖":
                self.ui.result_label.setText(str(float(number_1)*(float(self.ui.result_label.text()))))
                islem = ""
                number_1 = ""

            elif islem == "-":
                self.ui.result_label.setText(str(float(number_1)-(float(self.ui.result_label.text()))))
                islem = ""
                number_1 = ""

            elif islem == "+":
                self.ui.result_label.setText(str(float(number_1)+(float(self.ui.result_label.text()))))
                islem = ""
                number_1 = ""

            elif islem == "/":
                if self.ui.result_label.text() == "0":
                    pass
                else:
                    self.ui.result_label.setText(str(float(number_1)/(float(self.ui.result_label.text()))))
                    islem = ""
                    number_1 = ""

            elif islem == "%":
                self.ui.result_label.setText(str(float(number_1)*(float(self.ui.result_label.text()))/100))
                islem = ""
                number_1 = ""
            pass

        elif sender == "C":
            self.ui.result_label.setText("")
            label = ""

        elif sender == "+/-":
            self.ui.result_label.setText(f"-{self.ui.result_label.text()}")

        elif sender == "⬅":
            dizi = list(self.ui.result_label.text())
            dizi.remove(dizi[-1])
            label = "".join(dizi)
            self.ui.result_label.setText(label)

        else:
            label += sender
            self.ui.result_label.setText(label)

def run():
    app = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())

run()