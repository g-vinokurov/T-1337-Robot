import pygame
import cv2
import numpy as np
import requests
import threading
from collections import deque

class FastPygameClient:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.width, self.height = self.screen.get_size()
        pygame.display.set_caption("Fast Video Stream")
        
        # Оптимизации Pygame
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN])
        
        # Двойная буферизация
        self.buffer = pygame.Surface((self.width, self.height))
        
        # Кольцевой буфер для кадров
        self.frame_buffer = deque(maxlen=1)  # Хранит 3 последних кадра
        
        # Флаги
        self.running = True
        self.streaming = True
        
        # Запуск потока
        self.thread = threading.Thread(target=self.video_worker, daemon=True)
        self.thread.start()
        
        # Статистика
        self.fps = 0
        self.frame_count = 0
        self.last_time = pygame.time.get_ticks()
        
    def video_worker(self):
        """Рабочий поток для получения видео"""
        session = requests.Session()
        
        try:
            response = session.get("http://192.168.137.144:8000/stream.mjpg", 
                                  stream=True, timeout=5)
            
            jpeg_buffer = bytearray()
            
            while self.running and self.streaming:
                # Читаем большими блоками
                chunk = response.raw.read(16384)
                if not chunk:
                    break
                
                jpeg_buffer.extend(chunk)
                
                # Быстрый поиск JPEG границ
                start = jpeg_buffer.find(b'\xff\xd8')
                if start == -1:
                    if len(jpeg_buffer) > 20000:
                        jpeg_buffer.clear()
                    continue
                
                end = jpeg_buffer.find(b'\xff\xd9', start)
                if end == -1:
                    continue
                
                # Извлекаем и декодируем
                jpeg = bytes(jpeg_buffer[start:end+2])
                jpeg_buffer = jpeg_buffer[end+2:]
                
                if len(jpeg) > 500:
                    # Быстрое декодирование
                    nparr = np.frombuffer(jpeg, np.uint8)
                    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                    
                    if frame is not None:
                        # Конвертация и масштабирование за один проход
                        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        
                        # Масштабируем под размер экрана
                        h, w = frame_rgb.shape[:2]
                        if w != self.width or h != self.height:
                            frame_rgb = cv2.resize(frame_rgb, (self.width, self.height), 
                                                  interpolation=cv2.INTER_LINEAR)
                        
                        # Поворачиваем если нужно
                        frame_rgb = np.rot90(frame_rgb)
                        
                        # Добавляем в буфер
                        self.frame_buffer.append(frame_rgb)
                        
        except Exception as e:
            print(f"Video thread error: {e}")
        finally:
            session.close()
    
    def run(self):
        """Главный цикл"""
        clock = pygame.time.Clock()
        
        while self.running:
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_SPACE:
                        self.streaming = not self.streaming
            
            # Получаем последний кадр
            current_frame = None
            if self.frame_buffer:
                current_frame = self.frame_buffer[-1]
            
            # Отрисовка
            if current_frame is not None:
                # Преобразуем numpy в Pygame surface
                frame_surface = pygame.surfarray.make_surface(current_frame)
                self.screen.blit(frame_surface, (0, 0))
            else:
                self.screen.fill((0, 0, 0))
            
            # Статистика FPS
            self.frame_count += 1
            current_time = pygame.time.get_ticks()
            if current_time - self.last_time > 1000:
                self.fps = self.frame_count
                self.frame_count = 0
                self.last_time = current_time
            
            # Отображение FPS
            font = pygame.font.Font(None, 36)
            fps_text = font.render(f"FPS: {self.fps}", True, (255, 255, 255))
            self.screen.blit(fps_text, (10, 10))
            
            # Обновление экрана
            pygame.display.flip()
            
            # Фиксированный FPS
            clock.tick(60)
        
        pygame.quit()

if __name__ == "__main__":
    app = FastPygameClient()
    app.run()
