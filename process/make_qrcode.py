import qrcode

ad = input()
img = qrcode.make(ad)

img.show()
