
/* contants */
#define baudrate              9600 // resfresh rate of arduino
#define pin                   LED_BUILTIN    // TODO: pin for relay
#define action_on             "1"    // on action
#define action_off            "0"    // off action



/* configurations */
void setup() {
    Serial.begin(baudrate);
   while (!Serial) {
     ; // wait for serial port to connect. Needed for native USB port only
   }
    pinMode(pin, OUTPUT); 
}

void loop() {
  if (Serial.available() > 0) {
      String action = Serial.readStringUntil('\n');   
      if (action.equals(action_on)) {
        digitalWrite(pin, HIGH);     
        parseResponse("Encendido");
      } else if (action.equals(action_off)) {
        digitalWrite(pin, LOW);
        parseResponse ("Apagado");
      } else {
        parseResponse("Desconocido");
        digitalWrite(pin, LOW);
      }
  }
}

/* functions */
void parseResponse (String action){
    Serial.println("{'action':'" + action + "'}\n");
}
