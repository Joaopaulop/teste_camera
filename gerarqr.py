'''import pyqrcode

#print("Digite a url")

#url="https://www.youtube.com/watch?v=-4fIUSvXtUM"

code = pyqrcode.create("https://www.youtube.com/watch?v=-4fIUSvXtUM")

code.png('codigo.png',scale=6)

if code!=0:
    print("QRCode gerado")

'''

import qrcode
img = qrcode.make('https://www.youtube.com/watch?v=3yiT_WMlosg')
type(img)  # qrcode.image.pil.PilImage
img.save("qrcode.png")

