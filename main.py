import qrcode

qr = qrcode.QRCode(
	version=1,
	box_size=15,
	border=5
)

data = 'LPA:1$turktelekom.smdpp.protahub.com$E1479428-C5E4-4FDA-B57F-E5E5EDC05E20'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('file name.png')