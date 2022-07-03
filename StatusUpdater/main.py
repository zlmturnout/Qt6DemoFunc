import PySide6
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow
    
from status_updater import *

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=StatusUpdater()
    win.show()
    sys.exit(app.exec())