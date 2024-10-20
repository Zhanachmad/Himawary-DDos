import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("pkg install python")
    os.system("pkg install python2")
    os.system("pkg install python3")
    os.system("pip install colorama")
    os.system("pip install requests")

elif c == "1":

    os.system("pkg install python")
    os.system("pkg install python2")
    os.system("pkg install python3")
    os.system("pip install colorama")
    os.system("pip install requests")
print("Done.")
