from barcode import EAN13

my_code = EAN13("123456789012", writer=None)
my_code.save("ean13_barcode")
