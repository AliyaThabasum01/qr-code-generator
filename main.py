import os
import qrcode

print("=" * 40)
print("📱 QR Code Generator")
print("=" * 40)

text = input("Enter text or URL: ")

os.makedirs("output", exist_ok=True)

img = qrcode.make(text)

file_path = "output/qr_code.png"
img.save(file_path)

print("\n✅ QR Code generated successfully!")
print(f"Saved at: {file_path}")
