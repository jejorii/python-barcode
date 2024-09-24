import barcode
from barcode.writer import SVGWriter

# تحديد نوع الباركود والرقم
barcode_class = barcode.get_barcode_class('ean13')
barcode_number = '22022885071'

# إنشاء الباركود وحفظه كملف SVG
ean = barcode_class(barcode_number, writer=SVGWriter())

# حفظ الباركود
svg_file_path = 'barcode_22022885071_ean13.svg'
ean.save(svg_file_path)
