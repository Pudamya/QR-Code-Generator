import qrcode

qr=qrcode.QRCode(box_size=30,border=1)
qr.add_data("https://github.com/")
qr.make()
qr.make_image(fill_color="black",back_color="white")
