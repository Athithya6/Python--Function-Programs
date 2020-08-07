#https://www.datacamp.com/community/tutorials/python-xml-elementtree
#library converts dict to xml
#library conver xmltodict
#xml validation against a XSD
from xml.etree import ElementTree
from lxml import etree
class XmlListConfig(list):
    def __init__(self, aList):
        for element in aList:
            if element:
                # treat like dict
                if len(element) == 1 or element[0].tag != element[1].tag:
                    self.append(XmlDictConfig(element))
                # treat like list
                elif element[0].tag == element[1].tag:
                    self.append(XmlListConfig(element))
            elif element.text:
                text = element.text.strip()
                if text:
                    self.append(text)

class XmlDictConfig(dict):
    '''
    Example usage:
    >>> tree = ElementTree.parse('your_file.xml')
    >>> root = tree.getroot()
    >>> xmldict = XmlDictConfig(root)
    Or, if you want to use an XML string:
    >>> root = ElementTree.XML(xml_string)
    >>> xmldict = XmlDictConfig(root)
    And then use xmldict for what it is... a dict.
    '''
    def __init__(self, parent_element):
        if parent_element.items():
            self.update(dict(parent_element.items()))
        for element in parent_element:
            if element:
                # treat like dict - we assume that if the first two tags
                # in a series are different, then they are all different.
                if len(element) == 1 or element[0].tag != element[1].tag:
                    aDict = XmlDictConfig(element)
                # treat like list - we assume that if the first two tags
                # in a series are the same, then the rest are the same.
                else:
                    # here, we put the list in dictionary; the key is the
                    # tag name the list elements all share in common, and
                    # the value is the list itself 
                    aDict = {element[0].tag: XmlListConfig(element)}
                # if the tag has attributes, add those to the dict
                if element.items():
                    aDict.update(dict(element.items()))
                self.update({element.tag: aDict})
            # this assumes that if you've got an attribute in a tag,
            # you won't be having any text. This may or may not be a 
            # good idea -- time will tell. It works for the way we are
            # currently doing XML configuration files...
            elif element.items():
                self.update({element.tag: dict(element.items())})
            # finally, if there are no child tags and no attributes, extract
            # the text
            else:
                self.update({element.tag: element.text})

def dicttoxml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = ElementTree.Element(tag)
    for key, val in d.items():
        child = ElementTree.Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


#if we parse xml file
tree = ElementTree.parse('sample.xml')
root = tree.getroot()
xmldict = XmlDictConfig(root)
print(xmldict)
etree.XMLParser(dtd_validation=True)
#if you want to use an XML string:
#root = ElementTree.XML(xml_string)
#xmldict = XmlDictConfig(root)

e = dicttoxml('tagname',xmldict)
mystr = ElementTree.tostring(root, encoding='utf8').decode('utf8')
#myxml = ElementTree.tostring(e)
fileptr  = open('dest.xml','w+')
fileptr.write(mystr)
fileptr.close()


