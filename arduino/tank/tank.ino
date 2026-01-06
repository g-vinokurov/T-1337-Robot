
#include "Servo.h"
#include "AFMotor_R4.h"

AF_DCMotor motorR1(1);  // Create motor on M1
AF_DCMotor motorL1(2);  // Create motor on M2
AF_DCMotor motorL2(3);  // Create motor on M3
AF_DCMotor motorR2(4);  // Create motor on M4

Servo tower; // Create tower

int speed_l = 225; // Левый борт
int speed_r = 225; // Правый борт
int tower_right = 100; // Right speed (90 + 10)
int tower_left = 80; // Left speed (90 - 10)
int tower_stop = 90;

void setup() {
  Serial.begin(115200); // Для отладки
  Serial1.begin(115200); // Связь с ESP8266 (пины 18/RX1, 19/TX1)

  motorR1.setSpeed(speed_r);  // Set speed (0-255)
  motorR2.setSpeed(speed_r);  // Set speed (0-255)
  motorL1.setSpeed(speed_l);  // Set speed (0-255)
  motorL2.setSpeed(speed_l);  // Set speed (0-255)
  
  motorR1.run(RELEASE);   // Start motor (RELEASED)
  motorR2.run(RELEASE);   // Start motor (RELEASED)
  motorL1.run(RELEASE);   // Start motor (RELEASED)
  motorL2.run(RELEASE);   // Start motor (RELEASED)

  tower.attach(10); // Указываем к какому порту подключен вывод сервопривода
}

void loop() {
  if (Serial1.available() > 0) {
    char cmd = Serial1.read(); // Читаем команду от ESP

    Serial.print("Cmd: ");
    Serial.println(cmd, HEX);
    Serial.print("BIN: ");
    for (int i = 7; i >= 0; i--) {
      Serial.print((cmd >> i) & 1);
    }
    Serial.println();

    switch (cmd) {
      case '0': LForward();  break;
      case '1': RForward();  break;
      case '2': LBackward(); break;
      case '3': RBackward(); break;
      case '4': LRelease();  break;
      case '5': RRelease();  break;
      case '6': TRight();    break;
      case '7': TLeft();     break;
      case '8': TStop();     break;
    }
  }
}

void LForward() {
  motorL1.run(FORWARD);   // Run left-side motors (FORWARD)
  motorL2.run(FORWARD);   // Run left-side motors (FORWARD)
}

void RForward() {
  motorR1.run(FORWARD);   // Run right-side motors (FORWARD)
  motorR2.run(FORWARD);   // Run right-side motors (FORWARD)
}

void LBackward() {
  motorL1.run(BACKWARD);   // Run left-side motors (BACKWARD)
  motorL2.run(BACKWARD);   // Run left-side motors (BACKWARD)
}

void RBackward() {
  motorR1.run(BACKWARD);   // Run right-side motors (BACKWARD)
  motorR2.run(BACKWARD);   // Run right-side motors (BACKWARD)
}

void LRelease() {
  motorL1.run(RELEASE);   // Release left-side motors
  motorL2.run(RELEASE);   // Release left-side motors
}

void RRelease() {
  motorR1.run(RELEASE);   // Release right-side motors
  motorR2.run(RELEASE);   // Release right-side motors
}

void TRight() {
  tower.write(tower_right);
}

void TLeft() {
  tower.write(tower_left);
}

void TStop() {
  tower.write(tower_stop);
}
