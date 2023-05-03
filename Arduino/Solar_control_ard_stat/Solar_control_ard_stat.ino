#include <WiFiNINA.h>
#include <ArduinoJson.h>

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
  // создание объекта JSON и заполнение его данными
  StaticJsonDocument<200> doc;
  doc["id"] = 13;
  doc["performance"] = random(0.5, 1.0);
  doc["voltage"] = random(0.5, 1.0);
  doc["power"] = random(0.5, 1.0);

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

  delay(10000);
}
