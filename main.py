import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PDFViewer import PDFViewer
from PDFEngine import PDFEngine

'''
This is the main entry point of the application.
It initiatest he application and controls the elements in the window, any UI in the screen
'''
class DocumentApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Reader")
        self.resize(1200, 800)

        self.engine = PDFEngine()

        self.viewer = PDFViewer()
        
        layout = QVBoxLayout()
        layout.addWidget(self.viewer)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_document(self, path):
        page_count = self.engine.open_file(path)
        if page_count > 0:
            pix = self.engine.get_page_image(0, zoom_level=1.5)
            self.viewer.display_page(pix)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DocumentApp()
    window.show()
    sys.exit(app.exec())
