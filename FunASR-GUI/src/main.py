import sys
import os
from PySide6 import QtWidgets

sys.path.append(os.path.join(os.path.dirname(__file__), 'ui'))
sys.path.append(os.path.dirname(__file__)) 

from MainProcess import MainProcess

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('FunASR-GUI')
    MainWindow = MainProcess()
    MainWindow.show()
    sys.exit(app.exec())
