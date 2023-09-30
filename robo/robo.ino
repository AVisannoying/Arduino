#include <SoftwareSerial.h>


#include <Servo.h>

SoftwareSerial mySerial =  SoftwareSerial(0, 1);
// Define servo objects for each motor
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;


// Define the pins for each servo motor
int servo1Pin = 5;
int servo2Pin = 6;
int servo3Pin = 9;
int servo4Pin = 10;
// int servo5Pin = 10;


void setup() {
  // Attach each servo to its respective pin
mySerial.begin(9600);//for the connection

  servo1.attach(servo1Pin);
  servo2.attach(servo2Pin);
  servo3.attach(servo3Pin);
  servo4.attach(servo4Pin);
}

void loop() {
  // Move the robotic arm to a specific position
  moveArm(90, 90, 90, 90 );
  delay(1000);
  
  // Move the robotic arm to another position
  moveArm(0, 0, 0, 0);
  delay(1000);
}

void moveArm(int angle1, int angle2, int angle3, int angle4) {
  // Move each servo to the specified angle i.e. 90 degrees or pi/2 rad
  servo1.write(angle1);
  servo2.write(angle2);
  servo3.write(angle3);
  servo4.write(angle4);

}
