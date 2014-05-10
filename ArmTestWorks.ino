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
    //digitalWrite(enPin, HIGH);
    Serial.begin(9600);  
}

void loop() { 
    char c = Serial.read();
    
    if(c == 'd'){
        myservo.write(172);
        delay(15);  
    }
    
    if(c == 'u'){
        myservo.write(90);  
        delay(15);  
    }
        
    if(c == 'l'){
        digitalWrite(enPin, HIGH);
        myStepper.step(55);
        myStepper.step(-5);        
        delay(500);
    }
    
    if(c == 'a'){
        digitalWrite(enPin, HIGH);
        myStepper.step(45);
        delay(500);
    }
    
     if(c == 'b'){
        digitalWrite(enPin, HIGH);
        myStepper.step(-45);
        delay(500);
    }
    
    if(c == 'r'){
        digitalWrite(enPin, HIGH);
        myStepper.step(-55);
        myStepper.step(5);
        delay(500);
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
  myservo10.write(68);
  myservo11.write(180-68);
  delay(150);
}  

void feetBackward(void){
  myservo10.write(90);
  myservo11.write(180-90);
  delay(150);
}  


void armUp(void){
  myservo9.write(80);
  delay(150);
}  

void armDown(void){
  myservo9.write(110);
  delay(150);
}


void flick(void){
  for(int i = 110; i > 81; i--)
  {
    myservo9.write(i);
    delay(20);
  }
  
  delay(400);
}




