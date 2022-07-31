from tkinter import *
from bs4 import BeautifulSoup
import requests

root = Tk()
root.geometry("800x550")
root.resizable(0,0)
root.title("Adithegeek.exe")
root.config(bg = "LightGreen")

print_panel = StringVar()

def Intel_Core_i5_9400F():
    url = "https://www.newegg.com/intel-core-i5-9th-gen-core-i5-9400f/p/N82E16819117981?Description=Intel%20Core%20i5-9400F&cm_re=Intel_Core%20i5-9400F-_-19-117-981-_-Product"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text="$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def Intel_Core_i9_11900K():
    url = "https://www.newegg.com/Intel-Core-i9-11900K-Core-i9-11th-Gen/p/19-118-231"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text="$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def Intel_Core_i7_12700K():
    url = "https://www.newegg.com/intel-core-i7-12700k-core-i7-12th-gen/p/N82E16819118343?Description=processor&cm_re=processor-_-19-118-343-_-Product"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def Intel_Core_i5_12600():
    url = "https://www.newegg.com/intel-core-i5-12600-core-i5-12th-gen/p/N82E16819118371?Description=intel&cm_re=intel-_-19-118-371-_-Product"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def AMD_Ryzen_3_3200G():
    url = "https://www.newegg.com/amd-ryzen-3-3200g/p/N82E16819113571?Description=AMD%20Ryzen%203%203200G&cm_re=AMD_Ryzen%203%203200G-_-19-113-571-_-Product&quicklink=true"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def AMD_Ryzen_5_3400G():
    url = "https://www.newegg.com/amd-ryzen-5-3400g/p/N82E16819113570"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def AMD_Ryzen_9_5900X():
    url = "https://www.newegg.com/AMD-Ryzen-9-5900X/p/19-113-664"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def AMD_Ryzen_7_5700X():
    url = "https://www.newegg.com/amd-ryzen-7-5700x-ryzen-7-5000-series/p/N82E16819113735?Description=processor&cm_re=processor-_-19-113-735-_-Product&quicklink=true"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def Intel_Core_i9_12900KS():
    url = "https://www.newegg.com/intel-core-i9-12900ks-core-i9-12th-gen/p/N82E16819118392?Description=intel&cm_re=intel-_-19-118-392-_-Product"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)


def AMD_Ryzen_5_4600G():
    url = "https://www.newegg.com/amd-ryzen-5-4600g-ryzen-5-4000-g-series/p/N82E16819113744?Description=amd&cm_re=amd-_-19-113-744-_-Product&quicklink=true"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)


def AMD_Ryzen_Threadripper_2nd_Gen():
    url = "https://www.newegg.com/amd-ryzen-threadripper-2970wx/p/N82E16819113546?Description=threadripper&cm_re=threadripper-_-19-113-546-_-Product&quicklink=true"
    request = requests.get(url)
    doc = BeautifulSoup(request.text, "html.parser")
    tags = doc.find_all(text = "$")
    parent = tags[0].parent
    strong = parent.find("strong")
    printgtx = "$" + strong.string
    print_panel.set(printgtx)

def EXIT():
    root.destroy()

Label(root, text = "Intel", font="AgencyFb", bg= "LightGreen").place(x=300, y=30)
Label(root, text = "Amd Ryzen", font="AgencyFb", bg= "LightGreen").place(x=50, y=30)
Label(root, text = "Special Editions", font="AgencyFb", bg= "LightGreen").place(x=500, y=30)

Label(root, text = "Price: ", font=("AgencyFb", 15), bg = "LightGreen").place(x=165, y=355)
Entry(root,textvariable = print_panel, font = ("Arial", 15 ), bg = "LightGreen").place(x=220, y=355)


Button(root,text = "Quit", font = "ColonnaMT", command = EXIT, bg= "SlateGray").place(x=500, y=400)

#intel
Button(root,text = "Intel Core i5 9400F", font = "ColonnaMT", command = Intel_Core_i5_9400F, bg= "SlateGray3",).place(x=250, y=110)
Button(root,text = "Intel Core i9-11900K", font = "ColonnaMT", command = Intel_Core_i9_11900K, bg= "SlateGray3").place(x=250, y=160)
Button(root,text = "Intel Core i7-12700K", font = "ColonnaMT", command = Intel_Core_i7_12700K, bg= "SlateGray3").place(x=250, y=210)
Button(root,text = "Intel Core i5-12600", font = "ColonnaMT", command = Intel_Core_i5_12600, bg= "SlateGray3").place(x=250, y=260)
#amd
Button(root,text = "AMD Ryzen 3 3200G", font = "ColonnaMT", command = AMD_Ryzen_3_3200G, bg= "SlateGray3").place(x=25, y=100)
Button(root,text = "AMD Ryzen 5 3400G", font = "ColonnaMT", command = AMD_Ryzen_5_3400G, bg= "SlateGray3").place(x=25, y=150)
Button(root,text = "AMD Ryzen 9 5900X", font = "ColonnaMT", command = AMD_Ryzen_9_5900X, bg= "SlateGray3").place(x=25, y=200)
Button(root,text = "AMD Ryzen 7 5700X", font = "ColonnaMT", command = AMD_Ryzen_7_5700X, bg= "SlateGray3").place(x=25, y=250)
Button(root,text = "AMD Ryzen 5 4600G", font = "ColonnaMT", command = AMD_Ryzen_5_4600G, bg= "SlateGray3").place(x=25, y=300)
#special edition
Button(root,text = "Intel Core i9-12900KS", font = "ColonnaMT", command = Intel_Core_i9_12900KS, bg= "SlateGray3").place(x=470, y=110)
Button(root,text = "AMD Ryzen Threadripper 2nd Gen", font = "ColonnaMT", command = AMD_Ryzen_Threadripper_2nd_Gen, bg= "SlateGray3").place(x=470, y=160)
#run
root.mainloop()