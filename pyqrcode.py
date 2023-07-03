import qrcode
from PIL import Image

# 간단한 QR 코드 생성
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=5, border=4)
qr.add_data("https://example.com")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# QR 코드를 파일로 저장 (PNG 파일)
img.save("simple_qrcode.png")

print("간단한 QR코드 생성 및 저장 완료")

# 고급 QR 코드 생성
qr_advanced = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=2)
qr_advanced.add_data("https://example.com/some_page", optimize=0)
qr_advanced.make(fit=True)

img_advanced = qr_advanced.make_image(fill_color="blue", back_color="white")

# 고급 QR 코드를 파일로 저장(PNG 파일)
img_advanced.save("advanced_qrcode.png")

print("고급 QR코드 생성 및 저장 완료")
