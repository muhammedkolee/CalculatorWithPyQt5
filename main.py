from PyQt5 import QtWidgets
import sys
import math
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
        self.ui.squareroot_button.clicked.connect(self.calculate)
        self.ui.cot_button.clicked.connect(self.calculate)
        self.ui.tan_button.clicked.connect(self.calculate)
        self.ui.cos_button.clicked.connect(self.calculate)
        self.ui.sin_button.clicked.connect(self.calculate)
        self.ui.one_divide_button.clicked.connect(self.calculate)
        self.ui.log_button.clicked.connect(self.calculate)
        self.ui.ln_button.clicked.connect(self.calculate)
        self.ui.x_square_button.clicked.connect(self.calculate)
        self.ui.square_button.clicked.connect(self.calculate)
        self.ui.e_us_button.clicked.connect(self.calculate)
        self.ui.e_button.clicked.connect(self.calculate)
        self.ui.pi_button.clicked.connect(self.calculate)
        self.ui.abs_button.clicked.connect(self.calculate)


    def calculate(self):
        sender = self.sender().text()
        global number_1
        global label
        global islem

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
                label = ""
                number_1 = ""

            elif islem == "-":
                self.ui.result_label.setText(str(float(number_1)-(float(self.ui.result_label.text()))))
                islem = ""
                label = ""
                number_1 = ""

            elif islem == "+":
                self.ui.result_label.setText(str(float(number_1)+(float(self.ui.result_label.text()))))
                islem = ""
                label = ""
                number_1 = ""

            elif islem == "/":
                if self.ui.result_label.text() == "0":
                    pass
                else:
                    self.ui.result_label.setText(str(float(number_1)/(float(self.ui.result_label.text()))))
                    islem = ""
                    label = ""
                    number_1 = ""

            elif islem == "%":
                self.ui.result_label.setText(str(float(number_1)*(float(self.ui.result_label.text()))/100))
                islem = ""
                label = ""
                number_1 = ""

            elif islem == "xʸ":
                self.ui.result_label.setText(str(float(number_1)**(float(self.ui.result_label.text()))))
                islem = ""
                label = ""
                number_1 = ""

        elif sender == "C":
            self.ui.result_label.setText("")
            number_1 = ""
            islem = ""
            label = ""

        elif sender == "+/-":
            self.ui.result_label.setText(f"-{self.ui.result_label.text()}")

        elif sender == "⬅":
            dizi = list(self.ui.result_label.text())
            
            dizi.remove(dizi[-1])
            if len(dizi) != 0:
                if dizi[-1] == ".":
                    dizi.remove(dizi[-1])

            label = "".join(dizi)
            self.ui.result_label.setText(label)

        elif sender == "|x|":
            if self.ui.result_label.text() == "":
                pass

            else:
                self.ui.result_label.setText(abs(float(self.ui.result_label.text())))
        
        elif sender == "𝞹":
            self.ui.result_label.setText(str(math.pi))

        elif sender == "e":
            self.ui.result_label.setText(str(math.e))

        elif sender == "eˣ":
            self.ui.result_label.setText(str(math.e))

        elif sender == "x^2":
            if self.ui.result_label.text() == "":
                pass

            else:
                current_number = float(self.ui.result_label.text())
                self.ui.result_label.setText(str(current_number*current_number))

        elif sender == "xʸ":
            if self.ui.result_label.text() == "":
                pass

            else:
                number_1 = self.ui.result_label.text()
                islem = "xʸ"
                label = ""
                self.ui.result_label.setText("")

        elif sender == "ln":
            if self.ui.result_label.text() == "":
                pass

            else:
                self.ui.result_label.setText(str(math.log(float(self.ui.result_label.text()))))
        
        elif sender == "log":
            if self.ui.result_label.text() == "":
                pass

            else:
                self.ui.result_label.setText(str(math.log10(float(self.ui.result_label.text()))))

        elif sender == "1/x":
            if self.ui.result_label.text() == "":
                pass

            else:
                self.ui.result_label.setText(str(1/float(self.ui.result_label.text())))

        elif sender == "sin":
            if self.ui.result_label.text() == "":
                pass

            else:
                self.ui.result_label.setText(str(math.sin(math.radians(float(self.ui.result_label.text())))))

        elif sender == "cos":
            if self.ui.result_label.text() == "":
                pass

            else:
                self.ui.result_label.setText(str(math.cos(math.radians(float(self.ui.result_label.text())))))

        elif sender == "tan":
            if self.ui.result_label.text() == "":
                pass

            else:
                self.ui.result_label.setText(str(math.tan(math.radians(float(self.ui.result_label.text())))))

        elif sender == "cot":
            if self.ui.result_label.text() == "":
                pass

            else:
                self.ui.result_label.setText(str(1/math.tan(math.radians(float(self.ui.result_label.text())))))

        elif sender == "x!":
            if self.ui.result_label.text() == "":
                pass

            else:
                self.ui.result_label.setText(str(math.factorial(int(self.ui.result_label.text()))))

        elif sender == "√":
            if self.ui.result_label.text() == "":
                pass
            
            else:
                self.ui.result_label.setText(str(math.sqrt(float(self.ui.result_label.text()))))
        
        else:
            label += sender
            self.ui.result_label.setText(label)

def run():
    app = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(app.exec_())

run()