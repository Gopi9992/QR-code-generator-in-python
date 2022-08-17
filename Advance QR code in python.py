import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)

qr.add_data("Soon it will be one year that you are so far away from me.I miss you so much,my love!I wish I could be there with you right now.A million and one thoughts go through my head each and everyday about you.I can't wait for you to come to India and meet me.I love you a million times over with all of my heart, Parth!! ")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("for specialone.png")
