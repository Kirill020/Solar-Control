#include <WiFiNINA.h>
#include <ArduinoJson.h>

int Sensor = A0; // Der Stromstärkesensor wird am Pin A0 (Analog "0") angeschlossen.
int VpA = 185; // Millivolt pro Ampere (100 für 20A Modul und 66 für 30A Modul)
int sensorwert= 0;
float Nullpunkt = 2.5; // Spannung in mV bei dem keine Stromstärke vorhanden ist
double Voltage = 0;
double Ampere = 0;
double Performance = 0;


char ssid[] = "FRITZ!Box 7530 HW";
char pass[] = "04087603372686221636";
char server[] = "192.168.178.21"; 
int port = 8000;

WiFiClient client;

void setup() {
  Serial.begin(9600);
  while (!Serial) {}

  // подключение к Wi-Fi сети
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  sensorwert = analogRead(Sensor);
  Voltage = ((sensorwert / 1024.0) * 5000)/1000; 
  Ampere = ((Voltage - Nullpunkt) / VpA); 
  Performance = Performance +(Ampere*Voltage);

  //Serial.print("\t Voltage in V = ");
  //Serial.print(Voltage,3);
  //Serial.print("\t Ampere = ");
  //Serial.println(Ampere,3);
  //Serial.print("\t Performance in W = ");
  //Serial.print(Performance,3);
  

  // создание объекта JSON и заполнение его данными
  StaticJsonDocument<200> doc;
  doc["id"] = 13;
  doc["performance"] = Performance;
  doc["voltage"] = Voltage;
  doc["power"] = Ampere;

  // сериализация объекта JSON в строку
  String jsonStr;
  serializeJson(doc, jsonStr);

  // создание HTTP POST запроса
  String url = "/group_data";
  String contentType = "application/json";
  String contentLength = String(jsonStr.length());
  String payload = jsonStr;

  String request = "POST " + url + " HTTP/1.1\r\n" + "Host: " + String(server) + ":" + String(port) + "\r\n" + "Content-Type: " + contentType + "\r\n" + "Content-Length: " + contentLength + "\r\n\r\n" + payload;


  // отправка запроса на сервер
  if (client.connect(server, port)) {
    Serial.println("Connected to server");
    client.println(request);
  } else {
    Serial.println("Connection to server failed");
  }

  // ожидание ответа от сервера
  while (client.connected()) {
    if (client.available()) {
      char c = client.read();
      Serial.write(c);
    }
  }

  
  client.stop();

  delay(1800000);
}
