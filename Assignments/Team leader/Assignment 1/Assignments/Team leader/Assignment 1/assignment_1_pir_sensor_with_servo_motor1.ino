#include <Servo.h>
Servo s;

int ledPin = 13;                
int pirPin = 2;                
int pirStat = 0;                   
int pos = 0;

void setup() {
 pinMode(13, OUTPUT);     
 pinMode(2, INPUT);
 s.attach(9); 
 Serial.begin(9600);
}
void loop(){
 pirStat = digitalRead(pirPin); 
 if (pirStat == 1) {            
   digitalWrite(13, 1); 
   
   Serial.println("Hey I got you!!");

   for(pos = 0; pos <= 180; pos++){
    s.write(pos);              
    delay(15);                       
   } 
   digitalWrite(13, 0);
   for(pos = 180; pos >= 0; pos--) { 
    s.write(pos);              
    delay(15);                       
   }
  } 
} 