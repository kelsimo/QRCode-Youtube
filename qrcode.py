import qrcode
from PIL import Image
data = 'https://www.youtube.com/watch?v=RfeVPxdSwaM&ab_channel=CameronGreen'
qr=qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="teal", back_color="tan")
img.save('MyQRCode44.jpg') #change that qrcode to an image
img = Image.open('MyQRCode44.jpg')
img.show()