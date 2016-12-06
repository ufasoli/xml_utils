import sys
import os
from xml.dom.minidom import parseString

basePath = sys.argv[1]
file = sys.argv[2]
tag = sys.argv[3]

tagValues = set()
xml_file = open(os.path.join(basePath, file), 'r', encoding='utf-8')
print("opening file " + basePath + file)
xml_data = xml_file.read()
xml_file.close()
xml_dom = parseString(xml_data)

for tagValue in xml_dom.getElementsByTagName(tag):
    tagValues.add(tagValue.firstChild.nodeValue)

print("unique tag values for tag [{}] in file :".format(tag))
for v in tagValues:
    print(v)