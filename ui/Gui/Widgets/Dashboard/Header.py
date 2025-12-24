
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QHBoxLayout

from PySide6.QtCore import Qt

import Gui.Themes as Themes

from Log import log
from App import app


class Header(QWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-header')

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._layout = QHBoxLayout()
        self._layout.setContentsMargins(16, 16, 16, 16)
        self._layout.setSpacing(32)
        self._layout.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.setLayout(self._layout)
        self.restyleUI()

    def restyleUI(self, recursive: bool = False):
        self.setStyleSheet(f'''
            QWidget#dashboard-header {{
                background-color: {Themes.CurrentTheme.DashboardHeaderBackgroundColor};
                border-bottom: 1px solid {Themes.CurrentTheme.DashboardHeaderBorderColor};
                border-top: 1px solid {Themes.CurrentTheme.DashboardHeaderBorderColor};
                outline: none;
                padding: 0px;
            }}
        ''')
        if not recursive:
            return
