from StringIO import StringIO

from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from twisted.internet.defer import Deferred

from twisted.web.client import FileBodyProducer
from xml_dict import bm_xml

xml_str = bm_xml()
agent = Agent(reactor)
body = FileBodyProducer(StringIO(xml_str))

class BeginningPrinter(Protocol):
	def __init__(self, finished):
		self.finished = finished
		self.remaining = 1024 * 10

	def dataReceived(self, bytes):
        	if self.remaining:
            		reply = bytes[:self.remaining]
            		print(reply)

	def connectionLost(self, reason):
		print('Finished receiving body:', reason.getErrorMessage())
		self.finished.callback(None)


d = agent.request('POST','http://localhost:8080/',Headers({'User-Agent': ['Replication'],'Content-Type': ['text/x-greeting']}),body)

def cbRequest(response):
	finished = Deferred()
        response.deliverBody(BeginningPrinter(finished))
        return finished

d.addCallback(cbRequest)

def cbShutdown(ignored):
	reactor.stop()

d.addBoth(cbShutdown)
reactor.run()
