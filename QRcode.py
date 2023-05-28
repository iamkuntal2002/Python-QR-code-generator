import qrcode as qr
from PIL import Image

#first approach, it will generate a very simple qr code
# img = qr.make("Try yourself")
# img.save("file1.png")


qr = qr.QRCode(version=1,
            error_correction=qr.ERROR_CORRECT_H,
            box_size=10,border=4)
qr.add_data("try yourself and do some change on the QR code")
qr.make(fit=True)
img = qr.make_image(fill_color = "black",back_color = "white")
img.save("file2.png")