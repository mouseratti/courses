

try:
    open("new file")
except FileNotFoundError as e:
    print(e)
else:
    print("there was no exception!")
finally:
    print("this is finally block")



try:
    1 / 0
except:
    print("any error will be cought here!")


class MyException(Exception): pass


try:
    raise MyException("new error")
except Exception as e:
    print(e)


# try:
#     1 / 0
# except: pass

