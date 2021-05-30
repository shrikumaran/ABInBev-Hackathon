import xml.etree.ElementTree as ET
import cv2
import os 
import numpy as np

path = "/home/shrikumaran/Desktop/tech stuff/Competitions/Abinbev/Invoice Copies/label/"
files = os.listdir(path)

for label in files:
    if label.endswith('.xml'):
        tree = ET.parse(label)
        root = tree.getroot()
        table_coord = []
        column_coord = []
        
        for child in root:
            if child.tag == 'size':
                width = int(child[0].text)
                height = int(child[1].text)
            if child.tag == 'object' and child[0].text=='table':
                bnd=child[4]
                table_coord.append([int(bnd[0].text),int(bnd[1].text),int(bnd[2].text),int(bnd[3].text)])
            if child.tag == 'object' and child[0].text=='column':
                bnd=child[4]
                column_coord.append([int(bnd[0].text),int(bnd[1].text),int(bnd[2].text),int(bnd[3].text)])
        
        table_mask = np.zeros([height,width],dtype=np.float32)
        column_mask = np.zeros([height,width],dtype=np.float32)
        coord = table_coord[0]

        table_mask = cv2.rectangle(table_mask, (coord[0],coord[1]),(coord[2],coord[3]),(255),-1)

        name = label.split('.')[0]+".bmp"
        

        for coord in column_coord:
            column_mask = cv2.rectangle(column_mask, (coord[0],coord[1]),(coord[2],coord[3]),(255),-1)

        cv2.imwrite(name,table_mask)

