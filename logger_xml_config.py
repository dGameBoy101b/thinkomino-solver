from logging.config import dictConfig
from xml.etree.ElementTree import fromstring, XMLParser
from dictionary_xml_builder import DictionaryXMLBuilder
from re import compile

def configXML(path: str):
	with open(path,'rt') as file:
		xml_str = compile('>\s+<').sub('><', file.read())
	xml_dict = fromstring(xml_str, XMLParser(target=DictionaryXMLBuilder()))
	logger_config = xml_dict[next(iter(xml_dict))]
	logger_config['version'] = int(logger_config['version'])
	dictConfig(logger_config)