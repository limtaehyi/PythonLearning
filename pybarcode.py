import barcode
from barcode.writer import ImageWriter

# EAN-13 바코드 생성
ean = barcode.get('ean13', '123456789102', writer=ImageWriter())

# 바코드를 파일로 저장 (PNG 파일)
ean.save('ean13_example')

print("EAN-13 바코드 생성 및 저장 완료")

# Code128 바코드 생성
code128 = barcode.get('code128', '123456789', writer=ImageWriter())

# 바코드를 파일로 저장 (PNG 파일)
code128.save('code128_example')

print("Code128 바코드 생성 및 저장 완료")
