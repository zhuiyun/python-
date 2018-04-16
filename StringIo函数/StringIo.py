from io import StringIO

io_val=StringIO()
io_val = StringIO('Hello\nWorld!\nWelcome!')
for line in io_val:
    print(line)