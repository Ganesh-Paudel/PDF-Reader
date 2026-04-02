from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt

class PDFViewer(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)

    def display_page(self, pixmapData):
        self.scene.clear()
        img = QImage(
            pixmapData.samples, 
            pixmapData.width, 
            pixmapData.height, 
            pixmapData.stride, 
            QImage.Format.Format_RGB888
        )
        qPixmap = QPixmap.fromImage(img)
        self.scene.addPixmap(qPixmap)
