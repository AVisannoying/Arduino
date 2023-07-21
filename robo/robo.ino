#include <Servo.h>

// Define servo objects for each motor
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;

// Define the pins for each servo motor
int servo1Pin = 2;
int servo2Pin = 3;
int servo3Pin = 4;
int servo4Pin = 5;
int servo5Pin = 6;
int servo6Pin = 7;

void setup() {
  // Attach each servo to its respective pin
  servo1.attach(servo1Pin);
  servo2.attach(servo2Pin);
  servo3.attach(servo3Pin);
  servo4.attach(servo4Pin);
  servo5.attach(servo5Pin);
  servo6.attach(servo6Pin);
}

void loop() {
  // Move the robotic arm to a specific position
  moveArm(90, 90, 90, 90, 90, 90);
  delay(1000);
  
  // Move the robotic arm to another position
  moveArm(0, 0, 0, 0, 0, 0);
  delay(1000);
}

void moveArm(int angle1, int angle2, int angle3, int angle4, int angle5, int angle6) {
  // Move each servo to the specified angle
  servo1.write(angle1);
  servo2.write(angle2);
  servo3.write(angle3);
  servo4.write(angle4);
  servo5.write(angle5);
  servo6.write(angle6);
}
