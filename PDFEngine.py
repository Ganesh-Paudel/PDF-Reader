import fitz  

'''
This class only reacts with pdf. It handles anything that we need from pdf.
It initializes pdf using fitz (pymupdf) and returns any attributes that we might need. Any get_text_at_pos
attributes needed can be added in the class and be used to return

''''
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
