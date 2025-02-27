
class MainWindowInstance:
    def __init__(self):
        from MainMarket import MainWindow  
        self.main_window = MainWindow()

    def get_main_window(self):
        return self.main_window
