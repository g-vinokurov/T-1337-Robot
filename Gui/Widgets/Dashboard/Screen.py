
from PySide6.QtWidgets import QVBoxLayout

from PySide6.QtCore import Qt

from Gui.Widgets.Screen import Screen

from Gui.Widgets.Dashboard.Header import Header
from Gui.Widgets.Dashboard.Body import Body
from Gui.Widgets.Dashboard.Footer import Footer

import Gui.Themes as Themes

from Log import log
from App import app


class DashboardScreen(Screen):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-screen')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._header = Header(self)
        self._body = Body(self)
        self._footer = Footer(self)
        
        self._layout = QVBoxLayout()
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self._layout.addWidget(self._header)
        self._layout.addWidget(self._body)
        self._layout.addWidget(self._footer)

        self._layout.setStretch(1, 1)
        
        self.setLayout(self._layout)

        app.gui.setWindowTitle('T-1337 Control')
        self.restyleUI()
    
    @property
    def header(self):
        return self._header
    
    @property
    def body(self):
        return self._body
    
    @property
    def footer(self):
        return self._footer
    
    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QWidget#dashboard-screen {{
                background-color: {Themes.CurrentTheme.DashboardScreenBackgroundColor};
                border: none;
                outline: none;
                padding: 0px;
            }}
        ''')
        if not recursive:
            return
        self._header.restyleUI(recursive)
        self._body.restyleUI(recursive)
        self._footer.restyleUI(recursive)
