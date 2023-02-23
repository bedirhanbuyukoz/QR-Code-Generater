import qrcode

qr = qrcode.QRCode(
	version=1,
	box_size=15,
	border=5
)

data ='url'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('file1name.png')