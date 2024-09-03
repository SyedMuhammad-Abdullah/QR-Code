from qrcode import *

img = make(input("Enter link or text to convert to QR-CODE: "))
inp = input("Enter the name of File: ")
img.save(inp + ".png")

