import fitz  

'''
This class only reacts with pdf. It handles anything that we need from pdf.
It initializes pdf using fitz (pymupdf) and returns any attributes that we might need. Any get_text_at_pos
attributes needed can be added in the class and be used to return

'''
class PDFEngine:
    def __init__(self):
        self.pdfFile = None
        self.currentPageNumber = 0
        self.zoomLevel = 1.0

    def openFile(self, filePath):
        self.pdfFile = fitz.open(filePath)
        self.totalPages = len(self.pdfFile)
        return len(self.pdfFile)

    def getPageImage(self, pageNum):
        page = self.pdfFile.load_page(pageNum)
        mat = fitz.Matrix(self.zoomLevel, self.zoomLevel)
        pix = page.get_pixmap(matrix=mat)
        return pix

    def getNextPage(self):
        if self.currentPageNumber < self.totalPages - 1:
            self.currentPageNumber += 1
        return self.getCurrentPage()

    def getPreviousPage(self):
        if self.currentPageNumber >- 0:
            self.currentPageNumber -= 1
        return self.getCurrentPage()

    def getCurrentPage(self):
        return self.getPageImage(self.currentPageNumber)

    def updateZoom(self, deltaValue):
        self.zoomLevel = max(0.5, min(3.0, self.zoomLevel + deltaValue))
        return self.getCurrentPage()

