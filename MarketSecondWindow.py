from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLineEdit, QLabel
from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QIcon, QFont, QPixmap, QPainter, QBrush, QColor
from StyleSheets import SecondWindowStyleConfig
from SharedModules import MainWindowInstance
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de mercadorias")
        self.setGeometry(100, 100, 1360, 660)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        QTimer.singleShot(0, self.update)
        self.style_config = SecondWindowStyleConfig()
        self.class_mainwindow_instance = MainWindowInstance()
        self.class_mainwindow_martket = self.class_mainwindow_instance.get_main_window()
        self.Create_widgets()
        self.Postion_widgets()

    def Create_widgets(self):
        self.minimize_button = QPushButton(self)
        self.minimize_button.setIcon(QIcon("Icons/window-minimize.png"))
        self.minimize_button.setIconSize(QSize(25, 25))
        self.minimize_button.setStyleSheet(self.style_config.Image2_stylesheet())
        self.toggle_size = QPushButton(self)
        self.toggle_size.setIcon(QIcon("Icons/window-restore"))
        self.toggle_size.setIconSize(QSize(25, 25))
        self.toggle_size.setStyleSheet(self.style_config.Image2_stylesheet())
        self.close_window = QPushButton(self)
        self.close_window.setIcon(QIcon("Icons/cross.png"))
        self.close_window.setIconSize(QSize(25, 25))
        self.close_window.setStyleSheet(self.style_config.Image2_stylesheet())
        self.background_widget = QWidget(self)
        self.background_widget.setStyleSheet(self.style_config.Background_widgets())
        self.return_button = QPushButton("Retornar ao\nmenu", self.background_widget)
        self.return_button.setStyleSheet(self.style_config.Return_to_menu())
        self.options_group = QWidget(self)
        self.options_group.setStyleSheet(self.style_config.Options_group())
        self.buttons_group = QWidget(self)
        self.buttons_group.setStyleSheet(self.style_config.Buttons_group())
        self.suppliers_button = QPushButton("Fornecedores",self)
        self.suppliers_button.setStyleSheet(self.style_config.Options_buttons())
        self.circle1 = QLabel(self)
        self.circle1.setStyleSheet(self.style_config.Circles())
        self.propriety_rent = QPushButton("Aluguel da propriedade", self)
        self.propriety_rent.setStyleSheet(self.style_config.Options_buttons())
        self.circle2 = QLabel(self)
        self.circle2.setStyleSheet(self.style_config.Circles())
        self.automatic_verification = QPushButton("Verificação automática de produtos", self)
        self.automatic_verification.setStyleSheet(self.style_config.Options_buttons())
        self.circle3 = QLabel(self)
        self.circle3.setStyleSheet(self.style_config.Circles())
        self.products_list = QPushButton("Lista de produtos", self)
        self.products_list.setStyleSheet(self.style_config.Options_buttons())
        self.circle4 = QLabel(self)
        self.circle4.setStyleSheet(self.style_config.Circles())
        self.add_product = QPushButton("Adicionar\nproduto ao\n estoque", self)
        self.add_product.setStyleSheet(self.style_config.Products_buttons_group())
        self.remove_product = QPushButton("Remover\nproduto do\n estoque", self)
        self.remove_product.setStyleSheet(self.style_config.Products_buttons_group())
        self.search_products = QLineEdit(self)
        self.search_products.setStyleSheet(self.style_config.Search_products())
        self.search_products.setPlaceholderText("Buscar produto")
        self.search_products.setAlignment(Qt.AlignCenter)

    def Postion_widgets(self):
        self.minimize_button.setGeometry(1150, 1, 50, 50)
        self.toggle_size.setGeometry(1215, 1, 50, 50)
        self.close_window.setGeometry(1280, 1, 50, 50)
        self.background_widget.setGeometry(15, 45, 1330, 100)
        self.return_button.setGeometry(25, 17, 166, 60)
        self.options_group.setGeometry(15, 170, 350, 455)
        self.buttons_group.setGeometry(370, 170, 975, 455)
        self.suppliers_button.setGeometry(68, 200, 140, 20)
        self.circle1.setGeometry(36, 195, 25, 25)
        self.propriety_rent.setGeometry(68, 242, 283, 20)
        self.circle2.setGeometry(36, 239, 25, 25)
        self.automatic_verification.setGeometry(68, 288, 283, 20)
        self.circle3.setGeometry(36, 283, 25, 25)
        self.products_list.setGeometry(68, 332, 175, 20)
        self.circle4.setGeometry(36, 327, 25, 25)
        self.add_product.setGeometry(420, 195, 150, 60)
        self.remove_product.setGeometry(590, 195, 150, 60)
        self.search_products.setGeometry(1070, 195, 250, 60)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor("#001A2C")))
        painter.setPen(Qt.NoPen)
        rect = self.rect()
        painter.drawRoundedRect(rect, 20, 20)

    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton):
            self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if (hasattr(self, "old_pos")):
            self.delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.pos() + self.delta)
            self.old_pos = event.globalPosition().toPoint()

if (__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())