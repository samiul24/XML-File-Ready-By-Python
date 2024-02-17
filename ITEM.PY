import xml.etree.ElementTree as ET

# Parse the ITEM XML file
tree = ET.parse('ITEM.XML')
root = tree.getroot()
#print(root)

# Iterate through records
for record in root.findall('RECORD'):
    row = record.find('ROW')
    
    # Extract information from ROW attributes
    ItemCounter = row.get('ItemCounter')
    ItemDate = row.get('ItemDate')
    PatAmount = row.get('PatAmount')
    InsAmount = row.get('InsAmount')
    InsBalance = row.get('InsBalance')
    PatBalance = row.get('PatBalance')
    carrier = row.get('carrier')
    SecondaryCarrier = row.get('SecondaryCarrier')
    provider = row.get('provider')
    BillToDr = row.get('BillToDr')
    status = row.get('status')
    reversed = row.get('reversed')
    PaymentCode = row.get('PaymentCode')
    NoteAvailable = row.get('NoteAvailable')
    AccountAdjustment = row.get('AccountAdjustment')
    
    # Print or process the extracted information
    print(f"Item Counter: {ItemCounter}, Item Date: {ItemDate}, PatAmount: {PatAmount.strip()}, InsAmount: {InsAmount.strip()}, InsBalance: {InsBalance.strip()}")
    