#include <WiFiNINA.h>
#include <ArduinoJson.h>

int Sensor = A0; 
float VpA = 100; 
float sensorwert = 0;
float Nullpunkt = 2.5; 
float Voltage = 0;
float Ampere = 0;
float Performance = 0;

char ssid[] = "ssid";
char pass[] = "ssid password";
char server[] = "server ip";
int port = 8000;

WiFiClient client;

unsigned long lastSensorReadingTime = 0; 
const unsigned long sensorReadingInterval = 2000; 

unsigned long lastDataSendTime = 0; 
const unsigned long dataSendInterval = 3600000; 

int numReadings = 10;  
int iter = 0;
float voltageSum = 0;
float ampereSum = 0;
float performanceSum = 0;

bool isConnected = false; 

void setup() {
  Serial.begin(9600);
  while (!Serial) {}

  
  connectToWiFi();
}

void loop() {
  unsigned long currentMillis = millis();

  
  if (!isConnected || !client.connected()) {
  
    connectToWiFi();
    connectToServer();
  }

  
  if (currentMillis - lastSensorReadingTime >= sensorReadingInterval) {
    lastSensorReadingTime = currentMillis;


    sensorwert = analogRead(Sensor);
    Voltage = abs(((sensorwert / 1024.0) * 5000) / 1000);
    Ampere = abs((Voltage - Nullpunkt)) / VpA;
    Performance = Ampere * Voltage;

    
    iter += 1;
    voltageSum += Voltage;
    ampereSum += Ampere;
    performanceSum += Performance;


    
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


  if (isConnected && currentMillis - lastDataSendTime >= dataSendInterval) {
    lastDataSendTime = currentMillis;


    StaticJsonDocument<200> doc;
    doc["id"] = 13;
    doc["performance"] = performanceSum;
    doc["voltage"] = voltageSum/ iter;
    doc["power"] = ampereSum / iter;
    performanceSum = 0;
    voltageSum = 0;
    ampereSum = 0;

    String jsonStr;
    serializeJson(doc, jsonStr);


    String url = "/group_data";
    String contentType = "application/json";
    String contentLength = String(jsonStr.length());
    String payload = jsonStr;

    String request = "POST " + url + " HTTP/1.1\r\n" + "Host: " + String(server) + ":" + String(port) + "\r\n" + "Content-Type: " + contentType + "\r\n" + "Content-Length: " + contentLength + "\r\n\r\n" + payload;



    if (client.connected()) {
      Serial.println("Connected to server");
      client.println(request);
    } else {
      Serial.println("Connection to server failed");
      isConnected = false; 
    }

   
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
  
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void connectToServer() {
  
  if (client.connect(server, port)) {
    Serial.println("Connected to server");
    isConnected = true;
  } else {
    Serial.println("Connection to server failed");
    isConnected = false;
  }
}

