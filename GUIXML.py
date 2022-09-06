#Francis Adams
#CSCI435
#Basic tool to highlight leaf nodes of an XML file, converted to a PNG image
import sys
from bs4 import BeautifulSoup
import re
from PIL import Image, ImageDraw
import os 

filenames = []
#obtain every set of files and add their name to a set. once the set is built, reappend the 
#file endings to the corresponding strings and 
for filename in os.listdir(sys.argv[1]):
    nameset = str(filename)[:-4] # for .png and .xml, this cleanly removes them 
    if nameset not in filenames and (filename.endswith('.png') or filename.endswith('.xml')):
        filenames.append(nameset)

for i in range(0, len(filenames)):

    img =  sys.argv[1] + '/' + filenames[i] + '.png'#the image file
    xml =  sys.argv[1] + '/' + filenames[i] + '.xml'#the matching xml file 
    highlight = Image.open(img) #the location of the outgoing highlighted png file 


    with open(xml) as fxml:
        soup = BeautifulSoup(fxml.read(), 'xml')
        nodes = soup.find_all('node')
        for node in nodes:
            #find the bounds of each node. if there are no bounds attributes then it can be skipped
            #i string cast the nodes because i cannot get the bounds or regex match without that 
            nodeline = str(node)
            pattern = re.compile('bounds="\[\d+,\d+\]\[\d+,\d+\]"') 
            #leaf nodes end in /> 
            isLeaf = '/>' == nodeline[-2:]
            if not pattern.search(nodeline) or not isLeaf:
                continue  # debug statement so i can get the right nodes
            #else: #debug
            #print(nodeline[-50:], "passes the check and is a leaf node ")

            #to get the list of bounds, remove all but numbers and commas and then split on commas  
            #this is probably not ideal but it works. i remove everything except for the numbers listed in the bounds
            boundstr = re.sub('(.*bounds="\[)', '', nodeline)
            boundstr = re.sub('(\]".*)', '', boundstr)
            #small issue: to get the pair of brackets out of the middle so i can split, a simple replace would work
            #otherwise boundstr looks like 1,2][3,4 instead of 1,2,3,4
            boundstr = boundstr.replace('][', ',')
            boundstr = re.sub('\\n.*', '', boundstr) #only reason this is here is because dropbox will not work 
            #print('Node\'s numbers are ', boundstr ) #debug

            #coords is arranged to be [x1, y1, x2, y2]
            #need to convert to int values before 
            coords = boundstr.split(',')
            for i in range(0, len(coords)):
                coords[i] = int(coords[i]) 

            #use PIL draw rectangle to highlight the image 
            
            img1 = ImageDraw.Draw(highlight)  
            img1.rectangle([(coords[0], coords[1]), (coords[2], coords[3])], fill = None, outline = "yellow", width = 7)
        highlight = highlight.save(img.replace('.png', '-annotated.png'))
        



    
