import xml.etree.ElementTree as ET
from extract_rtf import striprtf

#base variables
basePath = '/Users/ufasoli/dev/trivadis/workspaces/idea/gerasmigration/metadata/exchange/XML/OW'
file = 'Talk.xml'
sanitizedFile = 'Talk_sanitized.xml'
textTag = 'JOURNAL'
rtfFilter = 'rtf1'

tree = ET.parse(basePath + '/' + file)
root = tree.getroot()

for talk in root:
    #look for the correct tag
    for t in talk.iter(textTag):
        #check if rtf formatted
        if (rtfFilter in str(t.text)):
            t.text = striprtf(t.text) #strip rtf

#write the file to disk
tree.write(basePath + '/' + sanitizedFile)
