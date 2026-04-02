import sys
from PyQt6.QtWidgets import QApplication
from application import DocumentApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DocumentApp()
    window.show()
    sys.exit(app.exec())
