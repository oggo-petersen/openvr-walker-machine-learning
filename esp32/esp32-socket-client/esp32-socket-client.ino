#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
#include <WiFi.h>
#include <HTTPClient.h>

WiFiClient client;
Adafruit_MPU6050 mpu;

// Informações da rede WiFi.
const char* ssid = "yourssid";
const char* pass = "yourpass";
const char* host = "yourhostip";
const int16_t port = 8080;

int read_delay = 100;

void setup(void) {
  Serial.begin(9600);

  // Try to initialize!
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }

  mpu.setAccelerometerRange(MPU6050_RANGE_16_G);
  mpu.setGyroRange(MPU6050_RANGE_250_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

  // Connecting to wifi...
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected!");
  Serial.println("nConnecting to socket!");
  connectSocket();
  Serial.println("Connected!");
  Serial.println("Starting main loop!");
  Serial.println("");
  delay(100);
}

void loop() {
  if (client.connected()) {
    sensors_event_t a, g, temp;
    mpu.getEvent(&a, &g, &temp);

    HTTPClient http;
    String currAccelX = String(a.acceleration.x);
    String currAccelY = String(a.acceleration.y);
    String currAccelZ = String(a.acceleration.z);
    String currGyroX= String(g.gyro.x);
    String currGyroY= String(g.gyro.y);
    String currGyroZ= String(g.gyro.z);
    String result = String(currAccelX + "," + currAccelY + "," + currAccelZ + "," + currGyroX + "," + currGyroY + "," + currGyroZ);
    Serial.println(result);
    client.print(result);
  } else {
    client.stop();
    connectSocket();
  }
  Serial.println("----");
  delay(read_delay);
}

void connectSocket() {
  while (!client.connect(host, port)) {
    Serial.println("\nConnection to host failed");
    delay(500);
  }
}