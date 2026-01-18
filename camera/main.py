import cv2
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread, Condition
import io

class StreamingOutput:
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):  # Начало JPEG-фрейма
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

class StreamingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                pass
        else:
            self.send_error(404)
            self.end_headers()

# Захват видео с USB-камеры
# cap = cv2.VideoCapture('/dev/video0')  # Используйте ваше устройство
cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 24)

output = StreamingOutput()

# Поток для захвата и кодирования кадров
def capture_frames():
    while True:
        ret, frame = cap.read()
        if ret:
            # Кодируем кадр в JPEG
            ret, jpeg = cv2.imencode('.jpg', frame)
            if ret:
                # Имитируем запись, как в оригинальном примере
                output.write(jpeg.tobytes())

capture_thread = Thread(target=capture_frames)
capture_thread.daemon = True
capture_thread.start()

try:
    address = ('', 8000)
    server = HTTPServer(address, StreamingHandler)
    print('Сервер запущен на порту 8000')
    server.serve_forever()
finally:
    cap.release()

