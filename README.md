# Assignment 1: XML parser to highlight interactable elements

Note: my design decisions are also included in this document

## Description

This Python program is designed to highlight all leaf nodes in an XML file and then output a PNG image that shows such. Anything surrounded with a yellow box 
indicates that it is a leaf node. It parses the XML file for leaf nodes, obtains the bounds of the nodes using regular expressions, and uses those coordinates to draw a rectangle around each of them indicating that they are such.

## How to use the program

I designed my implementation using Python 3.8, using two external libraries: Pillow, for drawing the highlights around each leaf node; and BeautifulSoup, which provides the means to parse the XML file for leaf nodes.

### Required Libraries:

Running this program works best in Anaconda because the libraries are already installed. If they are not, here are the commands to run in order to install them:

Pillow (pip install pillow)

Beatiful Soup (pip install beautifulsoup4

Command line syntax: python GUIXML.py directory-name

For each pair of XML-PNG files in the directory, the program will output 1 file containing highlighter leaf nodes 

## Design Choices

For this assignment, I opted to use python because I have the most experience with using python for programs like this and especially in a command prompt setting, which is the medium I chose to run this program. The program accepts a directory containing the files needed for conversion as input and parses through each of them to locate I used the BeautifulSoup library to parse the XML file and obtain the data for parsing because it will grab each individual node without the need to go into the file and separate each line (i.e. in the case of the XML code all being on one line, I can still easily grab everything without new lines. Once each line has been read, the bounds for each leaf node need to be parsed so that the program can grab the border coordinates. Using regular expressions, the extra information in the node leaf can be removed from the string so that the coordinates can be extracted and inserted into a list of [x0, y0, x1, y1]. Regex was the easiest way to do this because I was unable to find way to parse tags in the XML nodes, and string manipulation is a generally reliable way of doing this.

Once the coordinates are obtained through using BS and Regex, The Pillow library comes into play to draw the highlighted border on each node leaf. Using a simple draw rectangle method included in this library, the program creates a temporary image that is an empty rectangle with a yellow border that is then drawn onto the Android image. After all of the rectangles have been created and drawn onto the image, the program uses Pillow's save method to create a new PNG and save it in the current directory, where the user can find it and open it to see all the leaf nodes highlighted with a yellow border. PIL's draw rectangle method was easiest in my design because it did not force me to draw four lines manually. The ability to savenew images and not waste time with duplication is another nice feature included in the Pillow library. 
