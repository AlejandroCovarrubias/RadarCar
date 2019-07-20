//---------------------------------------------------------------//
//                 Movimiento_con_Joystick.ino
// Programa de control Arduino que maneja los motores, un servo
// y un sensor ultrasonico, que generan una salida de información
// de los objetos que se encuentran en una visión frontal de 90
// grados de un vehiculo montado con Arduino UNO.
//
//---------------------------------------------------------------//

//Libreria para controlar los motores
#include <AFMotor.h>
//Libreria para controlar el motor servo
#include <Servo.h>
//Libreria para controlar el sensor ultrasonico
#include <NewPing.h>
//ibreria para controlar el buzzer
#include <TimerFreeTone.h>

//Pines para el Joystick
int xPin = A1;
int yPin = A0;
int buttonPin = 2;

//Pines para el Sensor Ultrasonico
#define PIN_ECHO A4
#define PIN_TRIGGER A5
const int DISTANCIA_MAX = 60;
int distancia = 120;

//Posiciones del Joystick
int xPosition = 0;
int yPosition = 0;
int buttonState = 0;

//Definir ambos motores
AF_DCMotor motor1(1); //Motor Izquiero
AF_DCMotor motor2(2); //Motor Derecho

const unsigned int BAUD_RATE = 9600;

//Pin del zumbador
const unsigned int PIN_ZUM = 13;

//El servo
Servo elServo;

//El sonar
NewPing sonar(PIN_ECHO, PIN_TRIGGER, DISTANCIA_MAX);

//Valores de angulo y distacia que lee el sensor ultrasonico y el servo
signed int angulo;
signed int distanciaT;

//El setup
void setup() {

  //Inicializa las comunicaciones en serie a 9600 bps:
  Serial.begin(BAUD_RATE);

  //Inicializa los pines del Joystick
  pinMode(xPin, INPUT);
  pinMode(yPin, INPUT);
  pinMode(buttonPin, INPUT_PULLUP);

  //Inicializa el pin del zumbador
  pinMode(PIN_ZUM, OUTPUT);

  //Velocidad de los motores
  motor1.setSpeed(255);
  motor2.setSpeed (255);

  //El servo
  elServo.attach(10);
  elServo.write(45);
}

void loop() {

  //Lee las posiciones X y Y del joystick, ademas de si esta precionado o no
  xPosition = analogRead(xPin) / 10; //Se divide entre 10 para tener valores 
  yPosition = analogRead(yPin) / 10; //entre 0 y 103 en lugar de valores
  buttonState = digitalRead(buttonPin); //entre 0 y 1030

  //Totalmente quieto rangos (58<= y <=44) y (60<= x <=45)
  if (58 <= yPosition <= 44 && 60 <= xPosition <= 45) {
    //Deja en reposo a ambos motores, el servo y el sensor ultrasonico
    quieto();
  }

  //Derecha rango (58< x <= 102)
  if (58 < xPosition && xPosition <= 102) {
    //Función encargada de dar vuelta a la derecha
    derecha();
  }

  //Izquierda rango (0 <= x <44)
  if (0 <= xPosition && xPosition < 44) {
    //Función encargada de dar vuelta a la izquierda
    izquierda();
  }

  //Avanza rango (0<= y <30)
  if (0 <= yPosition && yPosition < 30) {
    //Función encargada de hacer avanzar el carro
    adelante();
  }

  //Reversa rango (85< y <=102)
  if (85 < yPosition && yPosition <= 102) {
    //Función encargada de hacer retroceder el carro
    reversa();
  }

  //Claxon si se preciona el joystick
  if (buttonState != 1) {
    //Función encargada de hacer sonar el claxon
    pito();
  }
}

//Hace que la llanta izquierda avance para ir a la derecha
void derecha() {
  motor1.run(BACKWARD);
  motor2.run(RELEASE);
}

//Hace que la llanta derecha avance para ir a la izquierda
void izquierda() {
  motor2.run(BACKWARD);
  motor1.run(RELEASE);
}

//Hace que el carro avance, escanee y envie al serial lo escaneado
void adelante() {
  //Se activa motor izquierdo
  motor1.run(BACKWARD);
  //Se activa motor derecho
  motor2.run(BACKWARD);
  for (int i = 45; i <= 135; i += 5) {
    //El servo se mueve en el anugulo indicado por el ciclo
    elServo.write(i);
    // Mide la distancia en cm usando un solo ping
    distanciaT = sonar.ping_cm();
    angulo = i;
    //Imprime el angulo y la distancia del objeto escaneado
    Serial.println("scan");
    Serial.println(angulo);
    Serial.println(distanciaT);
    //Tiempo de espera para las mediciones
    delay(60);
    //Se activa motor izquierdo
    motor1.run(BACKWARD);
    //Se activa motor derecho
    motor2.run(BACKWARD);
  }
  //Regresa al servo al lugar original osea 45 grados
  elServo.write(45);
}

//Hace que el carro retroseda
void reversa() {
  motor1.run(FORWARD);
  motor2.run(FORWARD);
}

//Hace que los motores esten quietos
void quieto() {
  motor1.run(RELEASE);
  motor2.run(RELEASE);
}

//Claxon del carro
void pito() {
  //Establece el sonido del claxon
  TimerFreeTone(PIN_ZUM, 159600, 200);
  // Apaga el zumbador
  TimerFreeTone(PIN_ZUM, 0, 0);
}
