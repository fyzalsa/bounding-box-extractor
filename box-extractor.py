import xml.etree.ElementTree as ET
import pandas as pd
import os

def main():
    path = '/home/hduser/Desktop/palmtree-data-pix-segamat/03images-after-segregate/xml/'
    for filename in os.listdir(path):
        if not filename.endswith('.xml'):
            continue
        fullname = os.path.join(path, filename)
        parsed_xml = ET.parse(fullname)
                
        dfcols = ['label', 'x', 'y']
        # dfcols = []
        df_xml = pd.DataFrame(columns=dfcols)

        for boxes in parsed_xml.iter('object'):
            name = boxes.find('name').text
            for box in boxes.findall("bndbox"):
                x = int(box.find("xmax").text)-int(box.find("xmin").text)
                y = int(box.find("ymax").text)-int(box.find("ymin").text)

            df_xml = df_xml.append(pd.Series([name, x, y], index=dfcols), ignore_index=True)
        print(df_xml, sep=',')
        # df_xml.to_csv('test.csv', sep=',', encoding='utf8')

main()
