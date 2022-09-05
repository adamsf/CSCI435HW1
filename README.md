# Assignment 1: XML parser to highlight interactable elements

Note: my design decisions are also included in this document and will not be in another one for the sake of being concise

## Description

This Python program is designed to highlight all leaf nodes in an XML file and then output a PNG image that shows such. Anything surrounded with a yellow box 
indicates that it is a leaf node. Using the XML file

## How to use the program

I designed my implementation using Python 3.8, using two external libraries: Pillow, for drawing the highlights around each leaf node; and BeautifulSoup, which provides the means to parse the XML file for leaf nodes.

install python 3.8, pillow, beautifulsoup

command line syntax: python GUIXML.py pngName.png xmlName.xml

the program will run and output a new PNG file with highlighted elements 

## Design Choices

For this assignment, I opted to use python because I have the most experience with using python for programs like this and especially in a command prompt setting, which is the medium I chose to run this program. I used the BeautifulSoup library to parse the XML file and obtain the data for parsing 
