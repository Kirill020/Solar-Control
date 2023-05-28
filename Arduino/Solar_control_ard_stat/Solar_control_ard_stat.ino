#include <WiFiNINA.h>
#include <ArduinoJson.h>

int Sensor = A0; // Датчик тока подключен к пину A0
float VpA = 100; // Милливольт на ампер (100 для 20-амперного модуля и 66 для 30-амперного модуля)
float sensorwert = 0;
float Nullpunkt = 2.5; // Напряжение в милливольтах, когда нет тока
float Voltage = 0;
float Ampere = 0;
float Performance = 0;

char ssid[] = "FRITZ!Box 7530 HW";
char pass[] = "04087603372686221636";
char server[] = "192.168.178.21";
int port = 8000;

WiFiClient client;

unsigned long lastSensorReadingTime = 0; // Последнее время считывания данных с датчика
const unsigned long sensorReadingInterval = 2000; // Интервал считывания данных с датчика (2 секунды)

unsigned long lastDataSendTime = 0; // Последнее время отправки данных на сервер API
const unsigned long dataSendInterval = 3600000; // Интервал отправки данных на сервер API (1 час)

int numReadings = 10;  // Количество измерений для усреднения
int iter = 0;
float voltageSum = 0;
float ampereSum = 0;
float performanceSum = 0;

bool isConnected = false; // Флаг подключения к серверу

void setup() {
  Serial.begin(9600);
  while (!Serial) {}

  // Подключение к Wi-Fi сети
  connectToWiFi();
}

void loop() {
  unsigned long currentMillis = millis();

  // Проверка статуса подключения к Wi-Fi и серверу
  if (!isConnected || !client.connected()) {
    // Если нет подключения, повторная попытка подключения
    connectToWiFi();
    connectToServer();
  }

  // Считывание данных с датчика каждые 2 секунды
  if (currentMillis - lastSensorReadingTime >= sensorReadingInterval) {
    lastSensorReadingTime = currentMillis;


    sensorwert = analogRead(Sensor);
    Voltage = abs(((sensorwert / 1024.0) * 5000) / 1000);
    Ampere = abs((Voltage - Nullpunkt)) / VpA;
    Performance = Ampere * Voltage;

    // Обновление суммарных значений
    iter += 1;
    voltageSum += Voltage;
    ampereSum += Ampere;
    performanceSum += Performance;


    // Вывод данных в серийный порт
    Serial.print("\n\t Voltage in V = ");
    Serial.print(Voltage, 3);
    Serial.print("\n");
    Serial.print("\t Ampere = ");
    Serial.println(Ampere, 3);
    Serial.print("\n");
    Serial.print("\t Performance in W = ");
    Serial.print(performanceSum, 3);
    Serial.print("\n");
  }

  // Отправка данных на сервер API каждый час
  if (isConnected && currentMillis - lastDataSendTime >= dataSendInterval) {
    lastDataSendTime = currentMillis;

    // Создание объекта JSON и заполнение его данными
    StaticJsonDocument<200> doc;
    doc["id"] = 13;
    doc["performance"] = performanceSum;
    doc["voltage"] = voltageSum/ iter;
    doc["power"] = ampereSum / iter;
    performanceSum = 0;
    voltageSum = 0;
    ampereSum = 0;
    // Сериализация объекта JSON в строку
    String jsonStr;
    serializeJson(doc, jsonStr);

    // Создание HTTP POST запроса
    String url = "/group_data";
    String contentType = "application/json";
    String contentLength = String(jsonStr.length());
    String payload = jsonStr;

    String request = "POST " + url + " HTTP/1.1\r\n" + "Host: " + String(server) + ":" + String(port) + "\r\n" + "Content-Type: " + contentType + "\r\n" + "Content-Length: " + contentLength + "\r\n\r\n" + payload;


    // Отправка запроса на сервер
    if (client.connected()) {
      Serial.println("Connected to server");
      client.println(request);
    } else {
      Serial.println("Connection to server failed");
      isConnected = false; // Сброс флага подключения
    }

   // Ожидание ответа от сервера
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
      }
    }

    client.stop();
  }
}

void connectToWiFi() {
  // Подключение к Wi-Fi сети
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void connectToServer() {
  // Подключение к серверу
  if (client.connect(server, port)) {
    Serial.println("Connected to server");
    isConnected = true;
  } else {
    Serial.println("Connection to server failed");
    isConnected = false;
  }
}

