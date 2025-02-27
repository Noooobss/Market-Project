from PySide6.QtGui import QColor
class MainWindowStyleConfig:
    def __init__(self):
        pass
    def Upper_buttons_stylesheet(self):
        return """
        QPushButton {
        background-color: #4C5B61;
        font: bold 16px 'Arial';
        border-radius: 12px;
        color: #FFFFFF;
        }
        QPushButton:hover {
        background-color: #3B4A4F;
        }
    """
    
    def Groups_stylesheet(self):
        return (
        "background-color: #949B96;"
        "border-radius: 18px"
        )
    def First_labels_group(self):
        return (
        "font: bold 18px 'Arial'"
        )
    def Second_labels_group(self):
        return (
        "font: bold 20px 'Arial'"
        )
    def Background_widgets(self):
        return (
        "background-color: #829191;"
        "border-radius:12;"
        )
    
    def Image_stylesheet(self):
        return (
        "background-color: transparent;"
        )
    def Header(self):
        return (
        "background-color: #FFFFFF;"
        )
    def Headers_buttons(self):
        return """
        QPushButton {
        background-color: #000000;
        border: none;
        }
        QPushButton:hover {
        background-color: #FFFFFF;
        }
        """
    
class SecondWindowStyleConfig:
    def Return_to_menu(self):
        return """
            QPushButton {
            background-color: #4C5B61;
            font: bold 16px 'Arial';
            border-radius: 12px;
            color: #FFFFFF;
            }
            QPushButton:hover {
            background-color: #3B4A4F;
            }
        """
    def Options_group(self):
        return (
        "background-color: #829191;"
        "border-radius: 12px;"
        )
    def Options_buttons(self):
        return """
        QPushButton {
        background-color: #829191;
        font: bold 16px 'Arial';
        border-radius: 6px;
        color: #FFFFFF;
        text-align: left;
        }
        QPushButton:hover {
        color: #014f4f;
        }
        """
    def Background_widgets(self):
        return (
        "background-color: #829191;"
        "border-radius: 12px;"
        )
    def Buttons_group(self):
        return (
        "background-color: #FFFFFF;"
        "border-radius: 12px;"
        )
    def Circles(self):
        return (
        "background-color: #FFFFFF;"
        "border-radius: 12px;"
        )
    def Products_buttons_group(self):
        return """
        QPushButton {
        background-color: #4C5B61;
        font: bold 16px 'Arial';
        border-radius: 10px;
        color: #FFFFFF;
        }
        QPushButton:hover {
        background-color: #3B4A4F;
        }
        """
    def Search_products(self):
        return """
        QLineEdit {
        background-color: #007281;
        border-radius: 8px;
        font: bold 16px 'Arial';
        color: #FFFFFF;
        text-align: right
        }
        QLineEdit:hover {
        background-color: #008394;
        }
        QLineEdit:placeholder {
        color: #888888;
        }
        """