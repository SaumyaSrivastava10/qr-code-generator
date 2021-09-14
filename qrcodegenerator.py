import pyqrcode
from PIL import Image



q=pyqrcode.create(input("Enter a link or text:  "))

q.png("qrcode.png",scale=8)
