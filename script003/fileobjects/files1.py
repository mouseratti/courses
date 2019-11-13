# ========= ===============================================================
# Character Meaning
# --------- ---------------------------------------------------------------
# 'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
# 'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
# 'b'       binary mode
# 't'       text mode (default)
# '+'       open a disk file for updating (reading and writing)
#     'U'       universal newline mode (deprecated)
# ========= ===============================================================
from string import ascii_letters
from random import choice
f  = open("filename.txt", "a+")
LINES_NUMBER = 16
LINE_LENGTH = 35

for line_number in range(LINES_NUMBER):
    line = ''.join(choice(ascii_letters) for x in range(LINE_LENGTH))
    f.write(line); f.write("\n")
    # f.writelines()


f.seek(0)

print(f.read())
print(f.read())
f.seek(0)
for line in f:
    print(line)
f.close()

f.read()

f  = open("filename.txt", "rb")
for line in f: print(line)