void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);
  pinMode(13, OUTPUT);
}
void loop() {  
  while(!Serial.available());
  String data = Serial.readString();
  int num_data = data.toInt();
  if(num_data == 1){
    digitalWrite(13, HIGH);
  }
  if(num_data == 0){
    digitalWrite(13,LOW);
  } 
}

