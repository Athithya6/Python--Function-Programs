package testhttp;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

public class Boot extends Connect {

public Boot(String targetURL) throws IOException {
super(targetURL);
// TODO Auto-generated constructor stub
}

static String cookie = null;


public String inform() {
return "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\r\n"
+ " <soap_env:Envelope\r\n"
+ "xmlns:soap_env=\"http://schemas.xmlsoap.org/soap/envelope/\"\r\n"
+ "xmlns:soap_enc=\"http://schemas.xmlsoap.org/soap/encoding/\"\r\n"
+ "xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\"\r\n"
+ "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\r\n"
+ "xmlns:cwmp=\"urn:dslforum-org:cwmp-1-2\">\r\n"
+ " <soap_env:Header>\r\n"
+ " <cwmp:ID soap_env:mustUnderstand=\"1\">1</cwmp:ID>\r\n"
+ " </soap_env:Header>\r\n"
+ " <soap_env:Body>\r\n"
+ " <cwmp:Inform>\r\n"
+ " <DeviceId>\r\n"
+ " <Manufacturer>Ventus Wireless</Manufacturer>\r\n"
+ " <OUI>001537</OUI>\r\n"
+ " <ProductClass>CX500</ProductClass>\r\n"
+ " <SerialNumber>HCCX546160042</SerialNumber>\r\n"
+ " </DeviceId>\r\n"
+ " <Event soap_enc:arrayType=\"cwmp:EventStruct[0]\">\r\n"
+ " <EventStruct>\r\n"
+ " <EventCode>2 PERIODIC</EventCode>\r\n"
+ " <CommandKey />\r\n"
+ " </EventStruct>\r\n"
// " <EventStruct>\r\n" +
// " <EventCode>2 PERIODIC</EventCode>\r\n" +
// " <CommandKey />\r\n" +
// " </EventStruct>\r\n" +
+" </Event>\r\n"
+ " <MaxEnvelopes>1</MaxEnvelopes>\r\n"
+ " <CurrentTime>2018-02-28T04:57:08-05:00</CurrentTime>\r\n"
+ " <RetryCount>0</RetryCount>\r\n"
+ " <ParameterList soap_enc:arrayType=\"cwmp:ParameterValueStruct[0]\" />\r\n"
+ " </cwmp:Inform>\r\n"
+ " </soap_env:Body>\r\n"
+ " </soap_env:Envelope>";
}

public void periodic() {
cookie = executePost("http://localhost:8081/cwmp/endpoint", inform(), cookie);
cookie = executePost("http://localhost:8081/cwmp/endpoint", "", cookie);
//cookie = executePost("http://localhost:8081/cwmp/endpoint", "204", cookie);
disconnect();
}

public void periodicEvent() {
cookie = executePost("http://localhost:8081/cwmp/endpoint", inform(), cookie);
cookie = executePost("http://localhost:8081/cwmp/endpoint", "", cookie);
}

}

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

package testhttp;

import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;

public class Bootstrap extends Connect {

static HttpURLConnection connection = null;
static String cookie = null;

public Bootstrap(String targetURL) throws IOException {
super(targetURL);
}

public String inform() {
return "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\r\n"
+ " <soap_env:Envelope\r\n"
+ "xmlns:soap_env=\"http://schemas.xmlsoap.org/soap/envelope/\"\r\n"
+ "xmlns:soap_enc=\"http://schemas.xmlsoap.org/soap/encoding/\"\r\n"
+ "xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\"\r\n"
+ "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\r\n"
+ "xmlns:cwmp=\"urn:dslforum-org:cwmp-1-2\">\r\n"
+ " <soap_env:Header>\r\n"
+ " <cwmp:ID soap_env:mustUnderstand=\"1\">1</cwmp:ID>\r\n"
+ " </soap_env:Header>\r\n"
+ " <soap_env:Body>\r\n"
+ " <cwmp:Inform>\r\n"
+ " <DeviceId>\r\n"
+ " <Manufacturer>Ventus Wireless</Manufacturer>\r\n"
+ " <OUI>001537</OUI>\r\n"
+ " <ProductClass>CX500</ProductClass>\r\n"
+ " <SerialNumber>HCCX546160042</SerialNumber>\r\n"
+ " </DeviceId>\r\n"
+ " <Event soap_enc:arrayType=\"cwmp:EventStruct[0]\">\r\n"
+ " <EventStruct>\r\n"
+ " <EventCode>0 BOOTSTRAP</EventCode>\r\n"
+ " <CommandKey />\r\n"
+ " </EventStruct>\r\n"
+" </Event>\r\n"
+ " <MaxEnvelopes>1</MaxEnvelopes>\r\n"
+ " <CurrentTime>2018-02-28T04:57:08-05:00</CurrentTime>\r\n"
+ " <RetryCount>0</RetryCount>\r\n"
+ " <ParameterList soap_enc:arrayType=\"cwmp:ParameterValueStruct[0]\" />\r\n"
+ " </cwmp:Inform>\r\n"
+ " </soap_env:Body>\r\n"
+ " </soap_env:Envelope>";
}

public String getRpcMethods() {
return "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\r\n"
+ " <soap_env:Envelope\r\n"
+ "xmlns:soap_env=\"http://schemas.xmlsoap.org/soap/envelope/\"\r\n"
+ "xmlns:soap_enc=\"http://schemas.xmlsoap.org/soap/encoding/\"\r\n"
+ "xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\"\r\n"
+ "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\r\n"
+ "xmlns:cwmp=\"urn:dslforum-org:cwmp-1-2\">\r\n"
+ " <soap_env:Header>\r\n"
+ " <cwmp:ID soap_env:mustUnderstand=\"1\">1</cwmp:ID>\r\n"
+ " </soap_env:Header>\r\n"
+ " <soap_env:Body>\r\n"
+ "<cwmp:GetRPCMethodsResponse>\r\n"
+ "<MethodList soap_enc:arrayType=\"xsd:string[12]\">\r\n"
+ "<string>GetRPCMethods</string> \r\n"
+ "<string>SetParameterValues</string> \r\n"
+ "<string>GetParameterValues</string> \r\n"
+ "<string>GetParameterNames</string> \r\n"
+ "<string>GetParameterAttributes</string> \r\n"
+ "<string>SetParameterAttributes</string> \r\n"
+ "<string>AddObject</string> \r\n"
+ "<string>DeleteObject</string> \r\n"
+ "<string>Download</string> \r\n"
+ "<string>Reboot</string> \r\n"
+ "<string>FactoryReset</string> \r\n"
+ "<string>ScheduleInform</string> \r\n"
+ "</MethodList>\r\n"
+ "</cwmp:GetRPCMethodsResponse>\r\n"
+ " </soap_env:Body>\r\n"
+ " </soap_env:Envelope>";
}

public String discoverBootstrapName() {
String s1 = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\r\n"
+ " <soap_env:Envelope\r\n"
+ "xmlns:soap_env=\"http://schemas.xmlsoap.org/soap/envelope/\"\r\n"
+ "xmlns:soap_enc=\"http://schemas.xmlsoap.org/soap/encoding/\"\r\n"
+ "xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\"\r\n"
+ "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-in stance\"\r\n"
+ "xmlns:cwmp=\"urn:dslforum-org:cwmp-1-2\">\r\n"
+ " <soap_env:Header>\r\n"
+ " <cwmp:ID soap_env:mustUnderstand=\"1\">1</cwmp:ID>\r\n"
+ " </soap_env:Header>\r\n"
+ " <soap_env:Body>\r\n"
+ " <cwmp:GetParameterNamesResponse>\r\n"
+ " <ParameterList soap_enc:arrayType=\"cwmp:ParameterInfoStruct[797]\">\r\n"
+ " <ParameterInfoStruct>\r\n"
+ " <Name>Device.WiFi.SSID.1.Stats.PacketsReceived</Name>\r\n"
+ " <Writable>0</Writable>\r\n"
+ " </ParameterInfoStruct>\r\n"
+ " <ParameterInfoStruct>\r\n"
+ " <Name>Device.WiFi.SSID.1.Stats.PacketsSent</Name>\r\n"
+ " <Writable>0</Writable>\r\n"
+ " </ParameterInfoStruct>\r\n"
+ " <ParameterInfoStruct>\r\n"
+ " <Name>Device.WiFi.SSID.1.Status</Name>\r\n"
+ " <Writable>0</Writable>\r\n"
+ " </ParameterInfoStruct>\r\n"
+ " </ParameterList>\r\n"
+ " </cwmp:GetParameterNamesResponse>\r\n"
+ " </soap_env:Body>\r\n"
+ "</soap_env:Envelope>";
return s1;
}

public String discoverBootstrapValue() {
String s2 = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\r\n"
+ " <soap_env:Envelope\r\n"
+ "xmlns:soap_env=\"http://schemas.xmlsoap.org/soap/envelope/\"\r\n"
+ "xmlns:soap_enc=\"http://schemas.xmlsoap.org/soap/encoding/\"\r\n"
+ "xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\"\r\n"
+ "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\r\n"
+ "xmlns:cwmp=\"urn:dslforum-org:cwmp-1-2\">\r\n"
+ " <soap_env:Header>\r\n"
+ " <cwmp:ID soap_env:mustUnderstand=\"1\">1</cwmp:ID>\r\n"
+ " </soap_env:Header>\r\n"
+ " <soap_env:Body>\r\n"
+ "<cwmp:GetParameterValuesResponse>\r\n"
+ " <ParameterList soap_enc:arrayType=\"cwmp:ParameterInfoStruct[797]\">\r\n"
+ "<ParameterValueStruct>\r\n"
+ "<Name>Device.WiFi.SSID.1.Stats.PacketsReceived</Name>\r\n"
+ " <Value xsi:type=\"xsd:long\">0</Value>\r\n"
+ "</ParameterValueStruct>\r\n"
+ " <ParameterValueStruct>\r\n"
+ "<Name>Device.WiFi.SSID.1.Stats.PacketsSent</Name>\r\n"
+ "<Value xsi:type=\"xsd:string\">0</Value>\r\n"
+ "</ParameterValueStruct>\r\n"
+ "<ParameterValueStruct>\r\n"
+ "<Name>Device.WiFi.SSID.1.Status</Name>\r\n"
+ "<Value xsi:type=\"xsd:string\">Down</Value>\r\n"
+ "</ParameterValueStruct>\r\n"
+ "</ParameterList>\r\n"
+ " </cwmp:GetParameterValuesResponse>\r\n"
+ "</soap_env:Body>\r\n"
+ "</soap_env:Envelope>";
return s2;
}

public String discoverBootstrapAttribute() {
String s3 = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\r\n"
+ " <soap_env:Envelope\r\n"
+ "xmlns:soap_env=\"http://schemas.xmlsoap.org/soap/envelope/\"\r\n"
+ "xmlns:soap_enc=\"http://schemas.xmlsoap.org/soap/encoding/\"\r\n"
+ "xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\"\r\n"
+ "xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\r\n"
+ "xmlns:cwmp=\"urn:dslforum-org:cwmp-1-2\">\r\n"
+ " <soap_env:Header>\r\n"
+ " <cwmp:ID soap_env:mustUnderstand=\"1\">1</cwmp:ID>\r\n"
+ " </soap_env:Header>\r\n"
+ " <soap_env:Body>\r\n"
+ "<cwmp:GetParameterAttributesResponse>\r\n"
+ " <ParameterList soap_enc:arrayType=\"cwmp:ParameterAttributeStruct[426]\">\r\n"
+ "<ParameterAttributeStruct>\r\n"
+ " <Name>Device.WiFi.SSID.1.Stats.PacketsReceived</Name>\r\n"
+ "<Notification>0</Notification>\r\n" + "<AccessList />\r\n"
+ "</ParameterAttributeStruct>\r\n"
+ "<ParameterAttributeStruct>\r\n"
+ "<Name>Device.WiFi.SSID.1.Stats.PacketsSent</Name>\r\n"
+ "<Notification>0</Notification>\r\n"
+ "<AccessList />\r\n"
+ "</ParameterAttributeStruct>\r\n"
+ "<ParameterAttributeStruct>\r\n"
+ "<Name>Device.WiFi.SSID.1.Status</Name>\r\n"
+ "<Notification>0</Notification>\r\n"
+ "<AccessList />\r\n"
+ "</ParameterAttributeStruct>"
+ "</ParameterList>\r\n"
+ " </cwmp:GetParameterAttributesResponse>\r\n"
+ "</soap_env:Body>\r\n"
+ "</soap_env:Envelope>";
return s3;

}

public void bootstrapDiscover() {
cookie = executePost("http://localhost:8081/cwmp/endpoint", inform(), cookie);
cookie = executePost("http://localhost:8081/cwmp/endpoint", "", cookie);
cookie = executePost("http://localhost:8081/cwmp/endpoint", getRpcMethods(), cookie);
cookie = executePost("http://localhost:8081/cwmp/endpoint", discoverBootstrapName(), cookie);
cookie = executePost("http://localhost:8081/cwmp/endpoint", discoverBootstrapValue(), cookie);
cookie = executePost("http://localhost:8081/cwmp/endpoint", discoverBootstrapAttribute(), cookie);
//cookie = executePost("http://localhost:8081/cwmp/endpoint", "204", cookie);
disconnect();

}

}

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

package testhttp;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Connect {


static HttpURLConnection connection = null;
static String cookie = null;

public Connect(String targetURL) throws IOException {
URL url = new URL(targetURL);
this.connection = (HttpURLConnection) url.openConnection();
}

public static String executePost(String targetURL, String urlParameters, String cookie) {

try {
// Create connection
URL url = new URL(targetURL);
connection = (HttpURLConnection) url.openConnection();
connection.setRequestMethod("POST");
connection.setRequestProperty("Content-Type", "application/xml");

connection.setRequestProperty("Content-Length", Integer.toString(urlParameters.getBytes().length));
connection.setRequestProperty("Content-Language", "en-US");
if (cookie != null) {
System.out.println("setting cookie");
connection.setRequestProperty("Cookie", cookie);
}

connection.setUseCaches(false);
connection.setDoOutput(true);

// Send request
DataOutputStream wr = new DataOutputStream(connection.getOutputStream());
wr.writeBytes(urlParameters);
wr.close();

// Get Response
InputStream is = connection.getInputStream();
for (int i = 0;; i++) {
String headerValue = connection.getHeaderField(i);
String headerName = connection.getHeaderFieldKey(i);
System.out.println("headerName=" + headerName + "headerValue=" + headerValue);
if (headerName == null && headerValue == null) {
System.out.println("Null header");
break;
}
if ("Set-Cookie".equalsIgnoreCase(headerName)) {
// String[] fields = headerValue.split(";\\s*");
cookie = headerValue;
System.out.println("cookie=" + cookie);
break;
}

}
BufferedReader rd = new BufferedReader(new InputStreamReader(is));
StringBuilder response = new StringBuilder(); // or StringBuffer if Java version 5+
String line;
while ((line = rd.readLine()) != null) {
response.append(line);
response.append('\r');
}
rd.close();
System.out.println("responsedata:"+response.toString());
System.out.println("cookie=" + cookie);
return cookie;
// return response.toString();
} catch (Exception e) {
e.printStackTrace();
return null;
}
}

public static void disconnect() {
if (connection != null) {
connection.disconnect();
}
}


}

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

package testhttp;

import java.io.IOException;

public class MainTest {

public static void main(String[] args) throws IOException, InterruptedException {
// TODO Auto-generated method stub
Bootstrap bootstrap = new Bootstrap("http://localhost:8081/cwmp/endpoint");
//bootstrap.bootstrapDiscover();
// Thread.sleep(10000);
Boot periodic = new Boot("http://localhost:8081/cwmp/endpoint");
//periodic.periodic();
ScheduleInform scheduleInform = new ScheduleInform("http://localhost:8081/cwmp/endpoint");
scheduleInform.ScheduleiInformresponse();
}

}

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


