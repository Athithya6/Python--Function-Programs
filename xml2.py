from twisted.web import server, resource
from twisted.internet import reactor
from xml_parser import parser
from twisted.web.resource import Resource

def parse_xml(xml_str):
	print(xml_str)
        xml_response = parser(xml_str)
        return xml_response

class re_simple(Resource):
	isLeaf = True
        def render_POST(self, request):
		xml_request_str = request.content.read()
                xml_response = parse_xml(xml_request_str)
                return xml_response

site = server.Site(re_simple())
reactor.listenTCP(8080, site)
print ("server started")
reactor.run()
