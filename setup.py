import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("apt install python")
    os.system("apt install python2")
    os.system("apt install python3")
    os.system("apt install colorama")
    os.system("apt install requests")

elif c == "1":

    os.system("apt install python")
    os.system("apt install python2")
    os.system("apt install python3")
    os.system("apt install colorama")
    os.system("apt install requests")
print("Done.")
