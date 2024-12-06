
#include <Wire.h>   //Library for initializing I2C Communication between Arduino & the peripherals

#include <Adafruit_PWMServoDriver.h>  // Library for 16-chanel PWM Servo Driver Shield

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();  //PWM Object Defined

#define ServoMin 150   // 'Tick' (out of 4096) corresponding to duty Cycle of minimum angle
#define ServoMax 510   // 'Tick' (out of 4096) corresponding to duty Cycle of maximum angle

uint8_t num = 1;       // The pin # of the Servo Shield to which the servo is connected to --> 0-15

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pwm.begin();
  pwm.setPWMFreq(60); //Analog Servos run ~60 

delay(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i=ServoMin; i<=ServoMax; i++) {
    pwm.setPWM(num,0,i);
    delay(10);
  }

  delay(2000);

  for (int i=ServoMax; i>ServoMin; i--) {
    pwm.setPWM(num,0,i);
    delay(10);
  }

  delay(5000);

  

}
