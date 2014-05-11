#include <Servo.h>
#include <Stepper.h>
String Move = "";


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

void loop(){
    while (Serial.available() > 0) {
        char inChar = Serial.read();   
    
        if (inChar == '\n'){          
            if(Move == "L"){
              Serial.println("Move L");
              move_L();              
            }
            
            if(Move == "R"){
              Serial.println("Move R");
              move_R();              
            }            

            if(Move == "U"){
              Serial.println("Move U");
              move_U();              
            }

            if(Move == "D"){
              Serial.println("Move D");
              move_D();              
            }

            if(Move == "F"){
              Serial.println("Move F");
              move_F();              
            }

            if(Move == "B"){
              Serial.println("Move B");
              move_B();              
            }
            
            if(Move == "M"){
              Serial.println("Move M");
              move_M();              
            }
            
             
            if(Move == "M2"){
              Serial.println("Move M2");
              move_M2();              
            }
            
             
            if(Move == "M'"){
              Serial.println("Move M'");
              move_Minv();              
            }
            
            if(Move == "L2"){
              Serial.println("Move L2");
              move_L2();              
            }
            
            
            if(Move == "R2"){
              Serial.println("Move L2");
              move_L2();              
            }            

            if(Move == "L'"){
              Serial.println("Move L'");
              move_Linv();              
            }

            if(Move == "R'"){
              Serial.println("Move R'");
              move_Rinv();              
            }

            if(Move == "U'"){
              Serial.println("Move U'");
              move_Uinv();              
            }

            if(Move == "D'"){
              Serial.println("Move D'");
              move_Dinv();              
            }

            if(Move == "F'"){
              Serial.println("Move F'");
              move_Finv();              
            }

            if(Move == "B'"){
              Serial.println("Move B'");
              move_Binv();              
            }

            Move = "";  
        }
        else
            Move.concat(inChar);
    }
}

/*----------move L-----------------*/
void move_L(){
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
    
      
    while(!(Serial.available()));
    Serial.read();
    flip(); 
    
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseRight();
    
    while(!(Serial.available()));
    Serial.read();
    holderUp();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    baseRight();
    
    Serial.println("Move L done");
}

/*----------move L2-----------------*/
void move_L2(){
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
    
      
    while(!(Serial.available()));
    Serial.read();
    flip(); 
    
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseRight();    
    
    while(!(Serial.available()));
    Serial.read();
    baseRight();
    
    while(!(Serial.available()));
    Serial.read();
    holderUp();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    baseRight();
    
    Serial.println("Move L done");
}

/*----------move R-----------------*/
void move_R(){
    while(!(Serial.available()));
    Serial.read();
    baseRight();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
    
    while(!(Serial.available()));
    Serial.read();
    holderUp();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
    
    Serial.println("Move R done");
}


/*----------move R2-----------------*/
void move_R2(){
    while(!(Serial.available()));
    Serial.read();
    baseRight();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
        
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
    
    while(!(Serial.available()));
    Serial.read();
    holderUp();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
    
    Serial.println("Move R done");
}


/*----------move U-----------------*/
void move_U(){
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseRight();
    
    while(!(Serial.available()));
    Serial.read();
    holderUp();
    
    while(!(Serial.available()));
    Serial.read();
    flip();  
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    Serial.println("Move U done");
}

/*----------move D-----------------*/
void move_D(){
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseRight();
    
    while(!(Serial.available()));
    Serial.read();
    holderUp();
      
    Serial.println("Move D done");
}


/*----------move F-----------------*/
void move_F(){
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseRight();
    
    while(!(Serial.available()));
    Serial.read();
    holderUp();
    
    /*
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
      */  
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    Serial.println("Move F done");
}

/*----------move B-----------------*/
void move_B(){
    while(!(Serial.available()));
    Serial.read();  
    flip();
    
    while(!(Serial.available()));
    Serial.read();  
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();  
    baseRight();
    
    while(!(Serial.available()));
    Serial.read();  
    holderUp();
    
    while(!(Serial.available()));
    Serial.read();  
    baseRight();
    
    while(!(Serial.available()));
    Serial.read();  
    baseRight();
    
    while(!(Serial.available()));
    Serial.read();  
    flip();
    
    while(!(Serial.available()));
    Serial.read();  
    baseRight();
    
    while(!(Serial.available()));
    Serial.read();  
    baseRight();
    
    
    Serial.println("Move B done");
}

/*----------move M-----------------*/
void move_M(){
    while(!(Serial.available()));
    Serial.read();
    baseLeft();    
      
    while(!(Serial.available()));
    Serial.read();
    flip(); 
    
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseRight();    
        
    while(!(Serial.available()));
    Serial.read();
    holderUp();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft();    
        
    while(!(Serial.available()));
    Serial.read();
    holderUp();
        
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    /*while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    */
    while(!(Serial.available()));
    Serial.read();
    baseRight();
    
    Serial.println("Move M done");
}

void move_M2(){
    while(!(Serial.available()));
    Serial.read();
    baseLeft();    
      
    while(!(Serial.available()));
    Serial.read();
    flip(); 
    
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseRight(); 
    
    while(!(Serial.available()));
    Serial.read();
    baseRight();    
        
    while(!(Serial.available()));
    Serial.read();
    holderUp();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft(); 
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft(); 
  
    while(!(Serial.available()));
    Serial.read();
    baseLeft();    
        
    while(!(Serial.available()));
    Serial.read();
    holderUp();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
    
    while(!(Serial.available()));
    Serial.read();
    flip();  

    while(!(Serial.available()));
    Serial.read();
    baseRight();
       
   
    
    /*while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    baseRight();
    */
    Serial.println("Move M2 done");
}
/*----------move M'-----------------*/
void move_Minv(){
    while(!(Serial.available()));
    Serial.read();
    baseLeft();    
      
    while(!(Serial.available()));
    Serial.read();
    flip(); 
    
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseRight();    
        
    while(!(Serial.available()));
    Serial.read();
    holderUp();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft();    
        
    while(!(Serial.available()));
    Serial.read();
    holderUp();
        
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    /*while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    */
    while(!(Serial.available()));
    Serial.read();
    baseRight();
    
    Serial.println("Move M' done");
}


/*----------move L inv-----------------*/
void move_Linv(){
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
    
      
    while(!(Serial.available()));
    Serial.read();
    flip(); 
    
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
    
    while(!(Serial.available()));
    Serial.read();
    holderUp();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    baseRight();
    
    Serial.println("Move L inverted done");
}

/*----------move R inv-----------------*/
void move_Rinv(){
    while(!(Serial.available()));
    Serial.read();
    baseRight();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseRight();
    
    while(!(Serial.available()));
    Serial.read();
    holderUp();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
    
    Serial.println("Move R inverted done");
}

/*----------move U inv-----------------*/
void move_Uinv(){
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
    
    while(!(Serial.available()));
    Serial.read();
    holderUp();
    
    while(!(Serial.available()));
    Serial.read();
    flip();  
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    Serial.println("Move U inverted done");

}

/*----------move D inv-----------------*/
void move_Dinv(){
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
    
    while(!(Serial.available()));
    Serial.read();
    holderUp();
      
    Serial.println("Move D inverted done");

}
 
/*----------move F inv-----------------*/ 
void move_Finv(){
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    while(!(Serial.available()));
    Serial.read();
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
    
    while(!(Serial.available()));
    Serial.read();
    holderUp();
    /*
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
    
    while(!(Serial.available()));
    Serial.read();
    baseLeft();
        */
    while(!(Serial.available()));
    Serial.read();
    flip();
    
    Serial.println("Move F inverted done");
}

/*----------move B inv-----------------*/ 
void move_Binv(){
    while(!(Serial.available()));
    Serial.read();  
    flip();
    
    while(!(Serial.available()));
    Serial.read();  
    holderDown();
    
    while(!(Serial.available()));
    Serial.read();  
    baseLeft();
    
    while(!(Serial.available()));
    Serial.read();  
    holderUp();
    
    while(!(Serial.available()));
    Serial.read();  
    baseRight();
    
    while(!(Serial.available()));
    Serial.read();  
    baseRight();
    
    while(!(Serial.available()));
    Serial.read();  
    flip();
    
    while(!(Serial.available()));
    Serial.read();  
    baseRight();
    
    while(!(Serial.available()));
    Serial.read();  
    baseRight();
    
    
    Serial.println("Move B inverted done");
}


void holderDown(){
   myservo.write(172);
   delay(15);  
}

void holderUp(){
   myservo.write(90);
   delay(15);  
}

void baseLeft(){
  digitalWrite(enPin, HIGH);
  myStepper.step(55);
  myStepper.step(-5);        
  delay(500);
  digitalWrite(enPin, LOW);  
}

void baseRight(){
  digitalWrite(enPin, HIGH);
  myStepper.step(-55);
  myStepper.step(5);        
  delay(500);
  digitalWrite(enPin, LOW);  
}

void flip(){
  armDown();
  feetForward();
  flick();
  feetBackward();    
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

  
