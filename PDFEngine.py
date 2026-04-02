import fitz  

class PDFEngine:
    def __init__(self):
        self.pdfFile = None
        self.currentPageNumber = 0

    def open_file(self, filePath):
        self.pdfFile = fitz.open(filePath)
        return len(self.pdfFile)

    def get_page_image(self, pageNum, zoomLevel=1.0):
        page = self.pdfFile.load_page(pagenum)
        mat = fitz.Matrix(zoomLevel, zoomLevel)
        pix = page.get_pixmap(matrix=mat)
        return pix

    def get_text_at_pos(self, pageNum, x, y):
        page = self.doc.load_page(pageNum)
        words = page.get_text("words")  
        for w in words:
            if w[0] <= x <= w[2] and w[1] <= y <= w[3]:
                return w[4]
        return None
