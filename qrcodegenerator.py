import pyqrcode
from PIL import Image



q=pyqrcode.create("http://www.google.com")

q.png("qrcode.png",scale=8)
