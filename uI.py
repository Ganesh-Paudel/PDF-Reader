from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLineEdit, QLabel, QFrame
)
from pdfViewer import PDFViewer 
class MainUI:
    def setupUi(self, central_widget):
        """
        Takes a QWidget and populates it with the application's layout.
        """
        mainLayout = QVBoxLayout(central_widget)
        
        self.controlsFrame = QFrame()
        controlsLayout = QHBoxLayout(self.controlsFrame)
        
        self.pathInput = QLineEdit()
        self.pathInput.setPlaceholderText("Paste PDF path or click Browse...")
        
        self.browserButton = QPushButton("Browse")
        self.loadButton = QPushButton("Load PDF")
        self.previousPage = QPushButton('←')
        self.nextPage = QPushButton('→')
        self.pageLabel = QLabel("Page: 0/0")
        
        controlsLayout.addWidget(QLabel("File:"))
        controlsLayout.addWidget(self.pathInput)
        controlsLayout.addWidget(self.browserButton)
        controlsLayout.addWidget(self.loadButton)
        controlsLayout.addWidget(self.previousPage)
        controlsLayout.addWidget(self.nextPage)
        controlsLayout.addWidget(self.pageLabel)
        
        self.viewer = PDFViewer()
        
        mainLayout.addWidget(self.controlsFrame)
        mainLayout.addWidget(self.viewer)
        
        return self 
