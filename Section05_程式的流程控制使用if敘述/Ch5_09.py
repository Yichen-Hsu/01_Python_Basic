# Ch5_09.py if敘述與None的應用，不過注意的是，None在布林值運算時會被當作False

flag = None
if not flag:
    print("flag is undefined")
if flag:
    print("flag is defined")
else:
    print("flag is undefined")