import xml.etree.ElementTree as ET

xmlname="/Users/munperum/PycharmProjects/training/data/emp.xml"


tree = ET.parse(xmlname)
root = tree.getroot()

print(root)
for child in root:
    print(child.tag, child.attrib, child.text)

for child in root:
    print(child[0].text, child[1].text)

for child in root.iter('name'):
    print(child.tag, child.attrib, child.text)

