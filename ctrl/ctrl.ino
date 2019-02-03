// Define pins
int ctr_a =9;
int ctr_b =8;
int ctr_c =11;
int ctr_d =10;
int l = 12;
// Counter and delay vars
int i=0;
int d=1000;
int launchDur = 2000;
// Serial stream
char data[64];
char term = '.';
int len = 0;
int val = 0;

void setup()
{
    pinMode(ctr_a,OUTPUT);
    pinMode(ctr_b,OUTPUT);
    pinMode(ctr_c,OUTPUT);
    pinMode(ctr_d,OUTPUT);
    pinMode(l, OUTPUT);
    Serial.begin(9600);
}


void loop ()
{
  if (Serial.available() > 0) {
    len = Serial.readBytesUntil(term, data, 64);
    val = (int(data[1])-48)*100 + (int(data[2])-48)*10 + (int(data[3])-48);
    Serial.println(val, DEC);
    if (data[0] == 'a') {
      clockwise(val);
    }
    else if (data[0] == 'b') {
      cclockwise(val);
    }
    else if (data[0] == 'c'){
      launch();
    }
  }
}

void clockwise(int t) {
  t = t*29/20;
  for (i = 0; i < t; i++) {
     digitalWrite(ctr_a,LOW);//A
     digitalWrite(ctr_b,HIGH);
     digitalWrite(ctr_c,HIGH);
     digitalWrite(ctr_d,HIGH);
     delayMicroseconds(d);
     digitalWrite(ctr_a,LOW);
     digitalWrite(ctr_b,LOW);//AB
     digitalWrite(ctr_c,HIGH);
     digitalWrite(ctr_d,HIGH);
     delayMicroseconds(d);
     digitalWrite(ctr_a,HIGH);
     digitalWrite(ctr_b,LOW);//B
     digitalWrite(ctr_c,HIGH);
     digitalWrite(ctr_d,HIGH);
     delayMicroseconds(d);
     digitalWrite(ctr_a,HIGH);
     digitalWrite(ctr_b,LOW);
     digitalWrite(ctr_c,LOW);//BC
     digitalWrite(ctr_d,HIGH);
     delayMicroseconds(d);
     digitalWrite(ctr_a,HIGH);
     digitalWrite(ctr_b,HIGH);
     digitalWrite(ctr_c,LOW);//C
     digitalWrite(ctr_d,HIGH);
     delayMicroseconds(d);
     digitalWrite(ctr_a,HIGH);
     digitalWrite(ctr_b,HIGH);
     digitalWrite(ctr_c,LOW);//CD
     digitalWrite(ctr_d,LOW);
     delayMicroseconds(d);
     digitalWrite(ctr_a,HIGH);
     digitalWrite(ctr_b,HIGH);
     digitalWrite(ctr_c,HIGH);//D
     digitalWrite(ctr_d,LOW);
     delayMicroseconds(d);
     digitalWrite(ctr_a,LOW);
     digitalWrite(ctr_b,HIGH);
     digitalWrite(ctr_c,HIGH);//DA
     digitalWrite(ctr_d,LOW);
     delayMicroseconds(d);
  }
  digitalWrite(ctr_b, LOW);
  digitalWrite(ctr_c, LOW);
}

void cclockwise(int t) {
  t = t*29/20;
  for (i = 0; i < t; i++) {
     digitalWrite(ctr_a,LOW);//A
     digitalWrite(ctr_b,HIGH);
     digitalWrite(ctr_c,HIGH);
     digitalWrite(ctr_d,HIGH);
     delayMicroseconds(d);
     digitalWrite(ctr_a,LOW);
     digitalWrite(ctr_b,HIGH);//AD
     digitalWrite(ctr_c,HIGH);
     digitalWrite(ctr_d,LOW);
     delayMicroseconds(d);
     digitalWrite(ctr_a,HIGH);
     digitalWrite(ctr_b,HIGH);//D
     digitalWrite(ctr_c,HIGH);
     digitalWrite(ctr_d,LOW);
     delayMicroseconds(d);
     digitalWrite(ctr_a,HIGH);
     digitalWrite(ctr_b,HIGH);
     digitalWrite(ctr_c,LOW);//DC
     digitalWrite(ctr_d,LOW);
     delayMicroseconds(d);
     digitalWrite(ctr_a,HIGH);
     digitalWrite(ctr_b,HIGH);
     digitalWrite(ctr_c,LOW);//C
     digitalWrite(ctr_d,HIGH);
     delayMicroseconds(d);
     digitalWrite(ctr_a,HIGH);
     digitalWrite(ctr_b,LOW);
     digitalWrite(ctr_c,LOW);//CB
     digitalWrite(ctr_d,HIGH);
     delayMicroseconds(d);
     digitalWrite(ctr_a,HIGH);
     digitalWrite(ctr_b,LOW);
     digitalWrite(ctr_c,HIGH);//B
     digitalWrite(ctr_d,HIGH);
     delayMicroseconds(d);
     digitalWrite(ctr_a,LOW);
     digitalWrite(ctr_b,LOW);
     digitalWrite(ctr_c,HIGH);//BA
     digitalWrite(ctr_d,HIGH);
     delayMicroseconds(d);
  }
  digitalWrite(ctr_c, LOW);
  digitalWrite(ctr_d, LOW);
}

void launch() {
  digitalWrite(l, HIGH);
  delay(launchDur);
  digitalWrite(l, LOW);
}
