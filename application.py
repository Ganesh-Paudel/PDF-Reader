from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QFileDialog
from PyQt6.QtCore import Qt
from pdfViewer import PDFViewer
from pdfEngine import PDFEngine
from databaseManager import DatabaseManager
from uI import MainUI
import os

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
        self.database = DatabaseManager();

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        
        self.ui = MainUI().setupUi(self.centralWidget)
        self.connectSignals()

    def connectSignals(self):
        self.ui.browserButton.clicked.connect(self.handleBrowse)
        self.ui.loadButton.clicked.connect(self.handleLoad)

        self.ui.nextPage.clicked.connect(self.goNextPage)
        self.ui.previousPage.clicked.connect(self.goPreviousPage)


    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Right, Qt.Key.Key_L):
            self.goNextPage()
        elif event.key() in (Qt.Key.Key_Left, Qt.Key.Key_H):
            self.goPreviousPage()

    def goNextPage(self):
        self.updateDisplay(self.engine.getNextPage())

    def goPreviousPage(self):
        self.updateDisplay(self.engine.getPreviousPage())

    def updateDisplay(self,pix):
        self.ui.viewer.displayPage(pix)
        self.ui.pageLabel.setText(f"Page: {self.engine.currentPageNumber + 1}/{self.engine.totalPages}")

    def handleBrowse(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")
        if filePath:
            self.ui.pathInput.setText(filePath)
            self.load_document(filePath)

    def handleLoad(self):
        path = self.ui.pathInput.text().strip()
        if os.path.exists(path):
            self.load_document(path)

    def load_document(self, path):
        pageCount = self.engine.openFile(path)
        if pageCount > 0:
            pix = self.engine.getPageImage(0)
            self.ui.viewer.displayPage(pix)
