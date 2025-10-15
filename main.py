# main.py  (fixed)
import os
import qrcode

print("Enter the website you need to make QR Code")
s = input().strip()

# QR code box structure
q = qrcode.QRCode(version=1, box_size=10, border=5)
q.add_data(s)
q.make(fit=True)

# create image
img = q.make_image(fill_color="black", back_color="white")

# ensure static folder exists and save using os.path.join
os.makedirs("static", exist_ok=True)
img_path = os.path.join("static", "qrcode.jpg")
img.save(img_path)

print(f"QR Code generated successfully and saved as {img_path}")
