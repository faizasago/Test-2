#include <Wire.h>  //Library for intializing I2C coomunication between Arduino & the peripherals

#include <Adafruit_PWMServoDriver.h>  ?? Library for 16 channel pwm servo driver shield

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();  // PWM Object Defined

#define ServoMin 150  //tick(out of 4096) corresponding to Duty Cycle for 0 degrees of Servo Arm position
#define ServoMax 510  // tick (out of 4096) cocorresponding to Duty Cycle for 180 degrees of Servo Arm position

void servowrite(int servonum, int angle){
  // Function to drive servo t an angle directly using the setPWM function
  int tick =map(angle,0,180,ServoMin,ServoMax);   //Map angle to tick in the duty cycle
  pwm.setPWM(servonum,0,tick);
}

void zeroset(){  //Fuction for setting all servos to 90 degrees (Zero Setting)
  for(int i=0;i<6;i++){
    servowrite(2*i,90);
    delay(100);
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pwm.begin();
  pwm.setPWMFreq(60);  //Analog Servos run at ~60 Hz
  delay(100);

  zeroset();
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:

}
