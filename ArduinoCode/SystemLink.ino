/*
This example talks to SystemLink.  Use VERBOSE true to see all of the information 
that passes back and forth. Note that with VERBOSE false, we do not wait for the serial
connection to be setup.

Remember to run VERBOSE the first time to get your MAC address to register it on Tufts Wireless.

Note the timestamp does not work - the arduino does not have a clock

Written by Chris Rogers
last revision November 2019

*/
#define VERBOSE true

#include <WiFiNINA.h>
#include "arduino_secrets.h" 

///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;            // your network key Index number (needed only for WEP)
String apikey = API_KEY;

int status = WL_IDLE_STATUS;

char server[] = "api.systemlinkcloud.com";    
WiFiSSLClient client;

String SL_Time = "";

void setup() {
  Serial.begin(9600);
  if (VERBOSE) while (!Serial);
  
  if (not(StartWiFi())) {  // don't continue
        while (true);
   }
}

void loop() {

    GET_SystemLink("fred");
    GET_SystemLink("fred_Num");
    PUT_SystemLink("fred",BuildString("test"));
    PUT_SystemLink("fred_Num",BuildInt16(12));
    delay(60000);
}

void GET_SystemLink (String tag) {
  
  Serial.print("\nTrying to connect for GET...");
  bool success = client.connect(server, 443);
  Serial.println(success);
  if (success) {
    Serial.println("connected to server");
    client.println("GET /nitag/v2/tags/" + tag + "/values HTTP/1.1");
    client.println("Host: api.systemlinkcloud.com");
    client.println("Content-Type:application/json");
    client.println("Accept:application/json");
    client.println("x-ni-api-key:" + apikey);
    client.println("Connection: close");
    client.println();

    String response = GetReply();
    int location = response.indexOf("OK");
    SL_Time = response.substring(location+4,(location+35)); // get the time from SystemLink
    if (VERBOSE) Serial.print(SL_Time);
    if (VERBOSE) Serial.println(" Time is " + GetTime());
    
    Serial.println(GetStringValue(response));
  }
}

void PUT_SystemLink (String tag, String PostData) {
  Serial.print("\nTrying to connect for PUT...");
  bool success = client.connect(server, 443);
  if (success) {
    Serial.println("connected to server, sending " + PostData);
    client.println("PUT /nitag/v2/tags/" + tag + "/values/current HTTP/1.1");
    client.println("Host: api.systemlinkcloud.com");
    client.println("Content-Type:application/json");
    client.println("Accept:application/json");
    client.println("x-ni-api-key:" + apikey);
    client.println("Connection: close");
    client.print("Content-Length: ");
    client.println(PostData.length());
    client.println();
    client.println(PostData);
    client.println();
    
    String response = GetReply();  
    Serial.println(PutStringValue(response));
  }
}

String GetReply() {
  String response = "";
  int counter = 0;
  while (client.connected() & (counter <100)) {  // connects for 1 sec of no data or loss of connection
    if (client.available()) {
      char c= client.read();
      if (VERBOSE) Serial.print(c);
      response += c;
      counter = 0;   // rezero counter
    }
    else {
      counter += 1;
      delay(10);
    }
  }
  if (VERBOSE) Serial.println();
  else Serial.println(response.substring(0,response.indexOf("\n")));
  if (VERBOSE) Serial.println("disconnecting from server.");
  client.stop();
  return response;
}

String BuildString(String package) {
  return "{\"value\":{\"type\":\"STRING\", \"value\":\"" + package + "\"}}";
}

String BuildInt16(int package) {
  return "{\"value\":{\"type\":\"INT\", \"value\":\"" + String(package) + "\"}}";
}

String GetStringValue (String replyString)  {
  String json = replyString.substring(replyString.lastIndexOf("{"),replyString.lastIndexOf("}"));
  if (VERBOSE) Serial.println ("full reply: " + json);
  json = json.substring((json.lastIndexOf(":")+1),json.indexOf("}"));
  return json;
}

String PutStringValue (String replyString)  {
  return replyString.substring(replyString.lastIndexOf("\n"));
}

bool StartWiFi() {
    // check for the WiFi module:
  if (WiFi.status() == WL_NO_MODULE) {
    Serial.println("Communication with WiFi module failed!");
    return 0;
  }

  String fv = WiFi.firmwareVersion();
  if (VERBOSE) Serial.println("Firmware: "+fv);
  if (fv < "1.0.0") {
    Serial.println("Please upgrade the firmware");
  }

  // attempt to connect to WiFi network:
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:
    //delay(10000);
  }
  Serial.println("Connected to wifi");
  if (VERBOSE) printWiFiStatus();
  return true;
}

// MAC: A4:CF:12:23:3D:9C or A4:CF:12:23:57:A4
 
void printWiFiStatus() {
  byte mac[6];
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());
  for (int i = 5; i<0; i--) {mac[i]=0;}
  // print your board's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);
  WiFi.macAddress(mac);
  Serial.print("MAC: ");
  for (int i = 5; i>=0; i--) {
    Serial.print(mac[i],HEX);
    if (i!=0) Serial.print(":");
  }
  Serial.println();

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  if (VERBOSE) Serial.print("signal strength (RSSI):");
  if (VERBOSE) Serial.print(rssi);
  if (VERBOSE) Serial.println(" dBm");
}

String NextInfo(String searchText) {
  String temp = SL_Time.substring(0,SL_Time.indexOf(searchText) + searchText.length());
  SL_Time = SL_Time.substring(SL_Time.indexOf(searchText) + searchText.length());
  SL_Time.trim();
  return temp;
}

String GetTime()  {
  String temp;
  temp = NextInfo("Date:");  //Date title
  temp = NextInfo(" ");      // Day
  temp = NextInfo(" ");
  int date = temp.toInt();
  temp = NextInfo(" ");     // month
  int month = 3;  // need the switch statement here...
  temp = NextInfo(" ");     //year
  int year = temp.toInt();
  temp = NextInfo(":");     //hour
  int hour = temp.toInt();
  temp = NextInfo(":");     //min
  int minute = temp.toInt();
  temp = NextInfo(" ");     //sec
  int sec = temp.toInt();

  return String(year) + "-" + String(month) + "-" + String(date) + "T" + String(hour) + ":" + String(minute) + ":" + String(sec) + "Z";
}