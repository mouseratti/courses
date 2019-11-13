# http://www.fileformat.info/info/charset/UTF-8/list.htm?start=1024
# https://unicode-table.com/en/
# ASCII is a table of symbols and encoding
# UNICODE is only a table of symbols


ascii_ura = 'ura'
unicode_ura = '\u0443\u0440\u0430'

print(unicode_ura)
print(ascii_ura)

print(ascii_ura.encode()) # byte representation
print(ascii_ura.encode()[0]) # first byte in decimal representation
print(hex(ascii_ura.encode()[0]))  # first byte hexadecimal


print(unicode_ura.encode()) # to utf-8 by default
print(unicode_ura.encode("cp1251"), len(unicode_ura.encode("cp1251"))) # to win1251


ascii_ura.encode("ascii") == ascii_ura.encode()
print(ascii_ura.encode("ascii"))

unicode_ura.encode("ascii") # UnicodeEncodeError

unicode_ura_encoded_utf8 = unicode_ura.encode()
unicode_ura_encoded_utf8.decode()

unicode_ura_encoded_1251 = unicode_ura.encode("cp1251")
unicode_ura_encoded_1251.decode() # UnicodeDecodeError
unicode_ura_encoded_1251.decode("cp1251")
