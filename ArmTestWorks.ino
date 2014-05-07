#include <Servo.h>
#include <Stepper.h>

const int stepsPerRevolution = 200;

Servo myservo;  // create servo object to control a servo
Servo myservo10; 
Servo myservo11; 
Servo myservo9;

Stepper myStepper(stepsPerRevolution, 12, 8, 4, 2);

int servoPin = 3;
int enPin = 7;

void setup(){
    myservo.attach(servoPin);  // attaches the servo on pin 9 to the servo object
    myservo10.attach(11);  // attaches the servo on pin 9 to the servo object 
    myservo11.attach(10);
    myservo9.attach(9);

    myStepper.setSpeed(60);    // set speed to 30 rpm
    pinMode(enPin, OUTPUT);
    digitalWrite(enPin, LOW);
    Serial.begin(9600);  
}

void loop() { 
    char c = Serial.read();
    
    if(c == 'd'){
        myservo.write(180);
        delay(15);  
    }
    
    if(c == 'u'){
        myservo.write(90);  
        delay(15);  
    }
        
    if(c == 'l'){
        digitalWrite(enPin, HIGH);
        myStepper.step(55);
    }
    
    if(c == 'r'){
        digitalWrite(enPin, HIGH);
        myStepper.step(-55);
    }
    
    if(c == 'f'){
        armDown();
        feetForward();
        flick();
        feetBackward();
    }
    
  
    digitalWrite(enPin, LOW);
} 

void feetForward(void){
  myservo10.write(60);
  myservo11.write(180-70);
  delay(250);
}  

void feetBackward(void){
  myservo10.write(90);
  myservo11.write(180-90);
  delay(250);
}  


void armUp(void){
  myservo9.write(80);
  delay(250);
}  

void armDown(void){
  myservo9.write(120);
  delay(250);
}


void flick(void){
  for(int i = 120; i > 81; i--)
  {
    myservo9.write(i);
    delay(10);
  }
  
  delay(1000);
}




