import qrcode

#python -m pip install qrcode[pil]   

URL = input("enter the link or URL of what you want to make a QR from").strip()
filename = input("What you want to save yo image as ?!")

if not filename.endswith(".png"):
  filename += ".png"

qr = qrcode.QRCode(box_size=20, border=10)
qr.add_data(URL)

image = qr.make_image(fill_color="red", back_colour="white")
image.save(filename)
print(f"saved as : {filename}")

