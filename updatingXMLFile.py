import xml.etree.ElementTree as ET

xmlname="/Users/munperum/PycharmProjects/training/data/emp.xml"


tree = ET.parse(xmlname)
root = tree.getroot()

for child in root.iter('sal'):
    print(child.tag, child.attrib, child.text)
    child.text = str("100K")
    child.set('updated', 'yes')
    print(child.tag, child.attrib, child.text)

tree.write(xmlname)