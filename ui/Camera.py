import sys
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer
import requests

class VideoClient(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Видео с робота")
        self.setGeometry(100, 100, 800, 600)
        
        # Элементы интерфейса
        self.url_input = QLineEdit("http://192.168.137.144:8000/stream.mjpg")
        self.connect_btn = QPushButton("Подключиться")
        self.connect_btn.clicked.connect(self.start_stream)
        
        self.video_label = QLabel()
        self.video_label.setFixedSize(640, 480)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.url_input)
        layout.addWidget(self.connect_btn)
        layout.addWidget(self.video_label)
        self.setLayout(layout)
        
        # Таймер для обновления видео
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.stream_active = False
        
    def start_stream(self):
        if not self.stream_active:
            self.stream_url = self.url_input.text()
            self.timer.start(40)  # 40 мс
            self.stream_active = True
            self.connect_btn.setText("Остановить")
        else:
            self.timer.stop()
            self.stream_active = False
            self.connect_btn.setText("Подключиться")
    
    def update_frame(self):
        try:
            response = requests.get(self.stream_url, stream=True, timeout=0.5)
            bytes_data = bytes()
            
            for chunk in response.iter_content(chunk_size=1024):
                bytes_data += chunk
                a = bytes_data.find(b'\xff\xd8')
                b = bytes_data.find(b'\xff\xd9')
                
                if a != -1 and b != -1:
                    jpg = bytes_data[a:b+2]
                    bytes_data = bytes_data[b+2:]
                    
                    # Декодируем изображение
                    frame = cv2.imdecode(np.frombuffer(jpg, np.uint8), cv2.IMREAD_COLOR)
                    
                    if frame is not None:
                        # Конвертируем BGR → RGB
                        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        h, w, ch = frame_rgb.shape
                        
                        # Создаем QImage и отображаем
                        qimg = QImage(frame_rgb.data, w, h, ch * w, QImage.Format_RGB888)
                        self.video_label.setPixmap(QPixmap.fromImage(qimg))
                    break
        except:
            pass  # Игнорируем ошибки таймаута

if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = VideoClient()
    client.show()
    sys.exit(app.exec_())

