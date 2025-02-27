from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLineEdit, QLabel
from PySide6.QtCore import Qt, QTimer, QSize,QPropertyAnimation, QRect
from PySide6.QtGui import QIcon, QFont, QPixmap, QPainter, QBrush, QColor
from MarketSecondWindow import MainWindow
from StyleSheets import MainWindowStyleConfig
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de mercadorias")
        self.setGeometry(100, 100, 1360, 660)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.is_maximized = False
        QTimer.singleShot(0, self.update)
        self.style_config = MainWindowStyleConfig()
        self.Create_widgets()
        self.widgets_screen1 = [
            self.minimize_button,
            self.toggle_size,
            self.background_widget,
            self.products_gestion,
            self.clients_accounts,
            self.cashier_mode,
            self.products_stock,
            self.open_and_close_cashier,
            self.call_suport,
            self.profit_group,
            self.label1_profit,
            self.label2_profit,
            self.clients_group,
            self.label1_clients,
            self.label2_clients,
            self.products_group,
            self.label1_products,
            self.label2_products,
        ]
        self.widgets_screen2 = [
            self.background_widget
        ]
        self.Postion_widgets()
        self.Connect_functions()

    def Create_widgets(self):
        self.minimize_button = QPushButton(self)
        self.minimize_button.setIcon(QIcon("Icons/window-minimize.png"))
        self.minimize_button.setIconSize(QSize(25, 25))
        self.minimize_button.setStyleSheet(self.style_config.Image_stylesheet())
        self.toggle_size = QPushButton(self)
        self.toggle_size.setIcon(QIcon("Icons/window-restore"))
        self.toggle_size.setIconSize(QSize(25, 25))
        self.toggle_size.setStyleSheet(self.style_config.Image_stylesheet())
        self.background_widget = QWidget(self)
        self.background_widget.setStyleSheet(self.style_config.Background_widgets())
        self.products_gestion = QPushButton("Gestão de\nprodutos", self.background_widget)
        self.products_gestion.setStyleSheet(self.style_config.Upper_buttons_stylesheet())
        self.clients_accounts = QPushButton("Contas de\nclientes", self.background_widget)
        self.clients_accounts.setStyleSheet(self.style_config.Upper_buttons_stylesheet())
        self.cashier_mode = QPushButton("Modo de\ncaixa", self.background_widget)
        self.cashier_mode.setStyleSheet(self.style_config.Upper_buttons_stylesheet())
        self.products_stock = QPushButton("Pagamento de\n funcionarios", self.background_widget)
        self.products_stock.setStyleSheet(self.style_config.Upper_buttons_stylesheet())
        self.open_and_close_cashier = QPushButton("Abrir /\n fechar caixa", self.background_widget)
        self.open_and_close_cashier.setStyleSheet(self.style_config.Upper_buttons_stylesheet())
        self.call_suport = QPushButton("Contatar o\n suporte", self.background_widget)
        self.call_suport.setStyleSheet(self.style_config.Upper_buttons_stylesheet())
        self.profit_group = QWidget(self)
        self.profit_group.setStyleSheet(self.style_config.Groups_stylesheet())
        self.label1_profit = QLabel("Lucro diário", self.profit_group)
        self.label1_profit.setStyleSheet(self.style_config.First_labels_group())
        self.profit_icon = QLabel(self.profit_group)
        self.profit_icon.setPixmap(QPixmap("Icons/usd-circle.png").scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.profit_icon.setStyleSheet(self.style_config.Image_stylesheet())
        self.label2_profit = QLabel("{Valor do lucro diario}", self.profit_group)
        self.label2_profit.setStyleSheet(self.style_config.Second_labels_group())
        self.clients_group = QWidget(self)
        self.clients_group.setStyleSheet(self.style_config.Groups_stylesheet())
        self.label1_clients = QLabel("Clientes registrados", self.clients_group)
        self.label1_clients.setStyleSheet(self.style_config.First_labels_group())
        self.clients_icon = QLabel(self.clients_group)
        self.clients_icon.setPixmap(QPixmap("Icons/user.png").scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.clients_icon.setStyleSheet(self.style_config.Image_stylesheet())
        self.label2_clients = QLabel("{Numero de clientes registrados}", self.clients_group)
        self.label2_clients.setStyleSheet(self.style_config.Second_labels_group())
        self.products_group = QWidget(self)
        self.products_group.setStyleSheet(self.style_config.Groups_stylesheet())
        self.label1_products = QLabel("Produtos registrados", self.products_group)
        self.label1_products.setStyleSheet(self.style_config.First_labels_group())
        self.products_icon = QLabel(self.products_group)
        self.products_icon.setPixmap(QPixmap("Icons/shopping-cart.png").scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.products_icon.setStyleSheet(self.style_config.Image_stylesheet())
        self.label2_products = QLabel("{Numero de produtos registrados}", self.products_group)
        self.label2_products.setStyleSheet(self.style_config.Second_labels_group())
        
    def Postion_widgets(self):
        self.minimize_button.setGeometry(1150, 1, 50, 50)
        self.background_widget.setGeometry(15, 45, 1330, 100)
        self.products_gestion.setGeometry(35, 27, 126, 46)
        self.clients_accounts.setGeometry(191, 27, 126, 46)
        self.cashier_mode.setGeometry(347, 27, 126, 46)
        self.products_stock.setGeometry(860, 27, 126, 46)
        self.open_and_close_cashier.setGeometry(1016, 27, 126, 46)
        self.call_suport.setGeometry(1172, 27, 126, 46)
        self.profit_group.setGeometry(35, 185, 407, 194)
        self.label1_profit.setGeometry(24, 12, 120, 20)
        self.profit_icon.setGeometry(140, 12, 24, 24)
        self.label2_profit.setGeometry(24, 97, 382, 20)
        self.clients_group.setGeometry(472, 185, 407, 194)
        self.label1_clients.setGeometry(24, 12, 180, 20)
        self.clients_icon.setGeometry(210, 12, 24, 24)
        self.label2_clients.setGeometry(24, 97, 382, 20)
        self.products_group.setGeometry(909, 185, 407, 194)
        self.label1_products.setGeometry(24, 12, 200, 20)
        self.products_icon.setGeometry(220, 12, 24, 24)
        self.label2_products.setGeometry(24, 97, 382, 20)

    def Connect_functions(self):
        self.products_gestion.clicked.connect(self.show_screen2)
    def hide_widgets(self, widgets):
        for widget in widgets:
            widget.hide()
    
    def show_widgets(self, widgets):
        for widget in widgets:
            widget.show()

    def show_screen1(self):
        self.hide_widgets(self.widgets_screen2)
        self.show_widgets(self.widgets_screen1)

    def show_screen2(self):
        self.hide_widgets(self.widgets_screen1)
        self.show_widgets(self.widgets_screen2)

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