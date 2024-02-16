import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('employeeList.xml')
root = tree.getroot()
print(root)
#exit()


for employee in root.findall('employee'):
    #print(employee)
    id = employee.find('name').attrib['id']
    department = employee.get('department')
    #print(employee.attrib['department']) This is produce the same result as like above line.
    name = employee.find('name').text
    position = employee.find('position').text
    joinyear = employee.find('joinyear').text
    salary = employee.find('salary').text
    print('Id: '+str(id)+ ', Name: ' +name+ 'Dept: ' +str(department) +', Position: '+position+', Join Year: '+joinyear+', Salary: '+salary)

exit()
# Iterate through employees
for employee in root.findall('employee'):
    # Extract information
    department = employee.get('department')
    name = employee.find('name').text
    position = employee.find('position').text
    join_year = employee.find('joinyear').text

    # Extract salary information
    salaries = [salary.text for salary in employee.findall('.//salary/*')]

    # Print or process the extracted information
    print(f"Department: {department}, Name: {name}, Position: {position}, Join Year: {join_year}, Salaries: {salaries}")
