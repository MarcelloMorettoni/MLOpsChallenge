/***********************************************************
File name: Potentiometer_control.ino
Description: Potentiometer controls the rotation angle of the servo.
Website: www.adeept.com
E-mail: support@adeept.com
Author: Tomp
Date: 2020/12/12
***********************************************************/
#include <Servo.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#define OLED_RESET     4
Adafruit_SSD1306 display(128, 64, &Wire, OLED_RESET);

Servo servo1;//create servo object to control a servo
Servo servo2;//create servo object to control a servo
Servo servo3;//create servo object to control a servo
Servo servo4;//create servo object to control a servo
Servo servo5;//create servo object to control a servo
//The following can be modified according to your specific needs
int dataServo1 = 90; // Servo 1 rotation range(dataServo1=0~180)
int dataServo2 = 90; // Servo 2 rotation range(dataServo2=0~180) 
int dataServo3 = 90; // Servo 3 rotation range(dataServo3=0~180)
int dataServo4 = 90; // Servo 4 rotation range(dataServo4=0~180)
int dataServo5 = 90; // Servo 5 rotation range(dataServo5=35~90)

float dirServo1Offset = 10;    // define a variable for deviation(degree) of the servo
float dirServo2Offset = -10;    // define a variable for deviation(degree) of the servo
float dirServo3Offset = 5;    // define a variable for deviation(degree) of the servo
float dirServo4Offset = -10;    // define a variable for deviation(degree) of the servo
float dirServo5Offset = 20;    // define a variable for deviation(degree) of the servo
int val1;
int val2;
int val3;
int val4;
int val5;

void resetServo()
{
  servo1.write(dataServo1+dirServo1Offset);//goes to dataServo1 degrees 
  servo2.write(dataServo2+dirServo2Offset);//goes to dataServo2 degrees 
  servo3.write(dataServo3+dirServo3Offset);//goes to dataServo3 degrees 
  servo4.write(dataServo4+dirServo4Offset);//goes to dataServo4 degrees 
  servo5.write(dataServo5+dirServo5Offset);//goes to dataServo5 degrees
    // Print the servo positions to the Serial Monitor
  Serial.println("Servo Positions After Reset:");
  Serial.print("Servo 1: "); Serial.println(dataServo1 + dirServo1Offset);
  Serial.print("Servo 2: "); Serial.println(dataServo2 + dirServo2Offset);
  Serial.print("Servo 3: "); Serial.println(dataServo3 + dirServo3Offset);
  Serial.print("Servo 4: "); Serial.println(dataServo4 + dirServo4Offset);
  Serial.print("Servo 5: "); Serial.println(dataServo5 + dirServo5Offset);  
}

void moveServoGradually(Servo& servo, int targetAngle, int step = 2, int delayTime = 100) {
    int currentAngle = servo.read(); // Get the current position of the servo

    if (currentAngle < targetAngle) {
        // Incrementally move the servo to the target angle
        for (int angle = currentAngle; angle <= targetAngle; angle += step) {
            servo.write(angle);
            delay(delayTime);
        }
    } else {
        // Decrementally move the servo to the target angle
        for (int angle = currentAngle; angle >= targetAngle; angle -= step) {
            servo.write(angle);
            delay(delayTime);
        }
    }
    // Ensure the servo reaches the exact target angle
    servo.write(targetAngle);
    Serial.print("Servo moved:"); Serial.println(targetAngle);
}

void pickUpCube()
{
    // Move servos to specific angles
    //moveServoGradually(servo1, 45); // Example: servo1 moves to 45 degrees
    moveServoGradually(servo5, 90);
    moveServoGradually(servo2, 10); // Example: servo2 moves to 30 degrees
    moveServoGradually(servo3, 158); // Example: servo3 moves to 90 degrees
    moveServoGradually(servo5, 110);
    servo5.write(130);
    delay(500);
    servo2.write(50);
    //moveServoGradually(servo2, 50);

}

void pointCubeLocation()
{
    moveServoGradually(servo5, 90);
    moveServoGradually(servo2, 10); // Example: servo2 moves to 30 degrees
    moveServoGradually(servo3, 158); // Example: servo3 moves to 90 degrees 
}

void dontPickItUp()
{
  servo4.write(110);
  delay(200);
  servo4.write(50);
  delay(200);
  servo4.write(110);
  delay(200);
  servo4.write(50);
  delay(200);
  servo4.write(110);
  delay(200);
  servo4.write(50);
  resetServo();
}

void iWantThis()
{
  servo3.write(120);
  delay(200);
  servo3.write(95);
  delay(200);
  servo3.write(120);
  delay(200);
  servo3.write(95);
  delay(200);
  servo3.write(120);
  delay(200);
  servo3.write(95);
  resetServo();
}

void setup()
{
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.setTextColor(WHITE);//Sets the font display color
  display.clearDisplay();//cls

  servo1.attach(9);//attachs the servo1 on pin 9 to servo object
  servo2.attach(6);//attachs the servo2 on pin 6 to servo object
  servo3.attach(5);//attachs the servo3 on pin 5 to servo object
  servo4.attach(3);//attachs the servo4 on pin 3 to servo object
  servo5.attach(11);//attachs the servo5 on pin 11 to servo object
  
  resetServo();

  Serial.begin(9600);
}
void loop()
{
    //Set the font size
  display.setTextSize(2);
  //Set the display location
  display.setCursor(0,30);
  //String displayed
  display.print("NEBUL");
  //Began to show
  display.display();
//  servo1.write(dataServo1+dirServo1Offset);//goes to dataServo1 degrees 
//  servo2.write(dataServo2+dirServo2Offset);//goes to dataServo2 degrees 
//  servo3.write(dataServo3+dirServo3Offset);//goes to dataServo3 degrees 
//  servo4.write(dataServo4+dirServo4Offset);//goes to dataServo4 degrees 
//  servo5.write(dataServo5+dirServo5Offset);//goes to dataServo5 degrees 

//  val1 = map(analogRead(0), 0, 1023, 0, 180);  
//  val2 = map(analogRead(1), 0, 1023, 0, 180);  
//  val3 = map(analogRead(2), 0, 1023, 0, 180);  
//  val4 = map(analogRead(3), 0, 1023, 0, 180);
//  val5 = map(analogRead(6), 0, 1023, 35, 180);  
 
//  dataServo1 = val1;
//  dataServo2 = val2;
//  dataServo3 = val3;
//  dataServo4 = val4;
//  dataServo5 = val5;
//  delay(50);//wait for 0.05second

  if(Serial.available()) {
    String data = Serial.readString();
    data.trim();
    char cmd = data[0];
    
    if(cmd == 'T')
    {
      pickUpCube();
    }

    if(cmd == 'R')
    {
      resetServo();
    }
    if(cmd == 'P')
    {
      pointCubeLocation();
    }
    if(cmd == 'D')
    {
      dontPickItUp();
    }
    if(cmd == 'S')
    {
      iWantThis();
    }
  }   
}
