import xml.etree.ElementTree as ET

# Parse the XML string
root = ET.parse('productList.xml')
print(root)
#exit()

# Iterate through products and catalog items
for product in root.findall('product'):
    description = product.get('description')
    product_image = product.get('product_image')
    #print(description +', '+ product_image)

    

    for catalog_item in product.findall('catalog_item'):
        #print(catalog_item)
        gender = catalog_item.get('gender')
        print(gender)
        gender = catalog_item.attrib['gender']
        print(gender)        
        item_number = catalog_item.find('item_number').text
        price = catalog_item.find('price').text
        #exit()

        # Extract information about sizes and color swatches
        sizes = []
        for size in catalog_item.findall('size'):
            size_description = size.get('description')
            print(size_description)
            color_swatches = [(swatch.text, swatch.get('image')) for swatch in size.findall('color_swatch')]
            sizes.append({'description': size_description, 'color_swatches': color_swatches})
            print(sizes)
            exit()

        # Print or process the extracted information
        print(f"Product: {description}, Product Image: {product_image}")
        print(f"Catalog Item: Gender: {gender}, Item Number: {item_number}, Price: {price}")

        for size_info in sizes:
            print(f"  Size: {size_info['description']}")
            for color_swatch in size_info['color_swatches']:
                print(f"    Color: {color_swatch[0]}, Image: {color_swatch[1]}")
