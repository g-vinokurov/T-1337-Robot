
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QSizePolicy

from Gui.Widgets.Navigator import Navigator


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        size_policy = QSizePolicy()
        size_policy.setHorizontalPolicy(QSizePolicy.Policy.Preferred)
        size_policy.setVerticalPolicy(QSizePolicy.Policy.Preferred)

        self._navigator = Navigator(self)
        self._navigator.setSizePolicy(size_policy)

        self.setCentralWidget(self._navigator)
        self.setSizePolicy(size_policy)

        self.showMaximized()
    
    @property
    def navigator(self):
        return self._navigator
