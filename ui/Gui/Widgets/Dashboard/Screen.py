from PySide6.QtWidgets import QVBoxLayout

from PySide6.QtCore import Qt

from Gui.Widgets.Screen import Screen

from Gui.Widgets.Dashboard.Header import Header
from Gui.Widgets.Dashboard.Body import Body
from Gui.Widgets.Dashboard.Footer import Footer

import Gui.Themes as Themes

from Log import log
from App import app

import requests

HOST = '192.168.4.1'
PORT = 80


class DashboardScreen(Screen):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        self.setObjectName('dashboard-screen')
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

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
        self.setFocus()
    
    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return  # Игнорируем автоповтор
    
        key = event.key()
        
        match key:
            case Qt.Key.Key_W.value:
                self.send_cmd('1')  # Left Forward
            case Qt.Key.Key_S.value:
                self.send_cmd('3')  # Left Backward
            case Qt.Key.Key_Up.value:
                self.send_cmd('0')  # Right Forward
            case Qt.Key.Key_Down.value:
                self.send_cmd('2')  # Right Backward
            case Qt.Key.Key_Left.value:
                self.send_cmd('6')  # Tower Left
            case Qt.Key.Key_Right.value:
                self.send_cmd('7')  # Tower Right
            case _:
                print('Unsupported key')
        super().keyPressEvent(event)
    
    def keyReleaseEvent(self, event):
        if event.isAutoRepeat():
            return  # Игнорируем автоповтор

        key = event.key()
        
        match key:
            case Qt.Key.Key_W.value:
                self.send_cmd('5')  # Left Stop
            case Qt.Key.Key_S.value:
                self.send_cmd('5')  # Left Stop
            case Qt.Key.Key_Up.value:
                self.send_cmd('4')  # Right Stop
            case Qt.Key.Key_Down.value:
                self.send_cmd('4')  # Right Stop
            case Qt.Key.Key_Left.value:
                self.send_cmd('8')  # Tower Stop
            case Qt.Key.Key_Right.value:
                self.send_cmd('8')  # Tower Stop
            case _:
                print('Unsupported key')
        super().keyReleaseEvent(event)
    
    def send_cmd(self, cmd: str):
        url = f'http://{HOST}:{PORT}/api/cmd'
        try:
            r = requests.post(url, data=cmd)
        except Exception as err:
            log.error(err)
        log.info(f'CMD: {cmd}')
