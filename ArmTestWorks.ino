/* Sweep
 by BARRAGAN <http://barraganstudio.com> 
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://arduino.cc/en/Tutorial/Sweep
*/ 

#include <Servo.h> 
 
Servo myservo10; // 180
Servo myservo11; // 0
Servo myservo9;
                // twelve servo objects can be created on most boards
 
int pos = 0;    // variable to store the servo position 
 
void setup() 
{ 
  myservo10.attach(10);  // attaches the servo on pin 9 to the servo object 
  myservo11.attach(11);
  myservo9.attach(9);
} 
 
void loop() 
{ 
  /*
  myservo9.write(170);
  
  for(int i = 30; i < 91; i = i + 10){
  myservo11.write(180-i);
  myservo10.write(i);
  delay(500);
  
  }
  */
  
 /* 
  myservo10.write(50);
  myservo11.write(180-50);
  
  for(int i = 70; i < 30; i++)
  {
    myservo9.write(i);
    delay(50);
  }
*/

//armUp();
armDown();
feetForward();
flick();
feetBackward();
delay(3000);
}

void feetForward(void){
  myservo10.write(60);
  myservo11.write(180-70);
  delay(500);
}  

void feetBackward(void){
  myservo10.write(90);
  myservo11.write(180-90);
  delay(500);
}  


void armUp(void){
  myservo9.write(80);
  delay(500);
}  

void armDown(void){
  myservo9.write(120);
  delay(500);
}


void flick(void){
   for(int i = 120; i > 81; i--)
  {
    myservo9.write(i);
    delay(15);
  }
  delay(1000);
}



