import sys
import os
from PySide6 import QtWidgets

# 添加ui文件夹到系统路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'ui'))
sys.path.append(os.path.dirname(__file__))  # 添加src目录到系统路径

from MainProcess import MainProcess

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainProcess()
    MainWindow.show()
    sys.exit(app.exec())
