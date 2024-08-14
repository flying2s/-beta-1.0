from PyQt5.QtWidgets import QWidget,QApplication
import sys
from PyQt5.uic import loadUi
import threading
import os
class win(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(390,300)
        loadUi("a.ui",self)
        self.pb.clicked.connect(self.click)
        
        
    def timer(self,t):
       
       for i in range(t):
           self.se.setText(t-i)
           
    def click(self):
       text = self.le.text()
       self.timer(int(text))
       os.system(f'shutdown -s -t {int(text)}')
       t1 = threading.Thread(target=self.timer())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = win()
    w.show()
    sys.exit(app.exec_())
