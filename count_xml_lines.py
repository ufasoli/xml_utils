import sys
import os
from xml.dom.minidom import parseString

files_tag = {
    'AdresseTemporal.xml': 'AdresseTemporal', 'Communication.xml': 'Communication',
    'Contacts.xml': 'Contacts', 'ContactTypeTemporal.xml': 'ContactTypeTemporal',
    'Talk.xml': 'Talk', 'Demand.xml': 'Demand', 'DemandCatalogBenefit.xml': 'DemandCatalogBenefit',
    'DemandConsultationPurview.xml': 'DemandConsultationPurview', 'LinkedDocument.xml': 'LinkedDocument',
    'ContactStatus.xml': 'ContactStatus', 'Network.xml': 'Network', 'PaymentMethode.xml': 'PaymentMethode'

}
basePath = sys.argv[1]
count = {}

for file, tag in files_tag.items():
    xml_file = open(os.path.join(basePath, file), 'r', encoding='utf-8')
    print("opening file " + basePath + file)
    xml_data = xml_file.read()
    xml_file.close()
    xml_dom = parseString(xml_data)

    count[tag] = len(xml_dom.getElementsByTagName(files_tag[file]))


print("----------")
for tag, nb in count.items():
    print("{} : {}".format(tag, nb))

print("----------")
print("end")
