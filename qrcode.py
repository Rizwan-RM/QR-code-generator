import qrcode

url = input("Enter a URL: ").strip() #any url of your choice
img_file = "./qrcode.png"

img = qrcode.make(url)
img.save(img_file)

qr = qrcode.QRCode()
qr.add_data(url)
img = qr.make_image()

img.save(img_file)