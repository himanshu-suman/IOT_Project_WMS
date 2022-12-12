#define BLYNK_PRINT Serial
#include "SPIFFS.h"
#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>
#include <DHT.h>
int a[4] = {81,17,5,13};
#define BLYNK_AUTH_TOKEN "VzNBt3lDPoxL4UAgcums3aEl_YwLZOyX"
char auth[] = "VzNBt3lDPoxL4UAgcums3aEl_YwLZOyX";//Enter your Auth token
char ssid[] = "realme C25Y";//Enter your WIFI name
char pass[] = "123456789";//Enter your WIFI password

DHT dht(4, DHT11);//(DHT sensor pin,sensor type)
BlynkTimer timer;




char status;
File file1;
void setup() {
  Serial.begin(9600);

  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass, "blynk.cloud", 80);
  dht.begin();

  //Call the functions
  timer.setInterval(100L, DHT11sensor);
  
}

//Get the DHT11 sensor values
void DHT11sensor() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  file1 = SPIFFS.open("C:\\Users\\parit\\Desktop\\try\\file.txt");

  if (isnan(h) || isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  
  Blynk.virtualWrite(V0, t);
  Blynk.virtualWrite(V1, h);
  Blynk.virtualWrite(V2, (float)a[0]);
  Blynk.virtualWrite(V3, (float)a[1]);
  Blynk.virtualWrite(V4, (float)a[2]);
  Blynk.virtualWrite(V5, (float)a[3]);

}

void loop() {
  Blynk.run();//Run the Blynk library
  timer.run();//Run the Blynk timer
  
}