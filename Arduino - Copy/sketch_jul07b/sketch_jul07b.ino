void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
int Sensor_value = analogRead(A0);
Serial.println("The value of sensor_value is " +String(Sensor_value));
delay(1000);
//if(Sensor_value < 600) {
  //digitalWrite(13, HIGH);
//}
//else {
 // digitalWrite(13, LOW);

//if(Sensor_value > 600) {
  //digitalWrite(13, LOW);
//}
}
