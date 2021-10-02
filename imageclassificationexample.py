

#code part 1
from bs4 import BeautifulSoup
import numpy as np
import requests
import cv2
import PIL.Image
import urllib
from keras.models import model_from_json
from keras.preprocessing import image

page = requests.get("http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n04194289")
print(page.content)

# BeautifulSoup is an HTML parsing library

soup = BeautifulSoup(page.content, 'html.parser')#puts the content of the website into the soup variable, each url on a different line
#print(soup)
#print(soup.prettify())
