from io import StringIO
#import xmldict
from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from twisted.web.client import FileBodyProducer
#from xml_dict import bm_xml
xml_str = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<soap_env:Envelope
xmlns:soap_env="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:soap_enc="http://schemas.xmlsoap.org/soap/encoding/"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:cwmp="urn:dslforum-org:cwmp-1-2">
<soap_env:Header>
<cwmp:ID soap_env:mustUnderstand="1">1</cwmp:ID>
</soap_env:Header>
<soap_env:Body>
<cwmp:Inform>
<DeviceId>
<Manufacturer>Ventus Wireless</Manufacturer>
<OUI>001537</OUI>
<ProductClass>CX500</ProductClass>
<SerialNumber>HCCX546160029</SerialNumber>
</DeviceId>
<Event soap_enc:arrayType="cwmp:EventStruct[1]">
<EventStruct>
<EventCode>1 BOOT</EventCode>
<CommandKey />
</EventStruct>
</Event>
<MaxEnvelopes>1</MaxEnvelopes>
<CurrentTime>2020-08-07T09:14:52+00:00</CurrentTime>
<RetryCount>0</RetryCount>
<ParameterList soap_enc:arrayType="cwmp:ParameterValueStruct[0]" />
</cwmp:Inform>
</soap_env:Body>
</soap_env:Envelope>"""

agent = Agent(reactor)
body = FileBodyProducer(StringIO(xml_str))
d = agent.request(
   'POST',
   'http://localhost:8080/',
    Headers({'User-Agent': ['cwmp'],
            'Content-Type': ['text/xml']}),
    body)
def cbResponse(response):
    print (response.version)
d.addCallback(cbResponse)
def cbShutdown(ignored):
   reactor.stop()
d.addBoth(cbShutdown)
reactor.run()
