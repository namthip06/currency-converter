#tkinker
#https://github.com/ParthJadhav/Tkinter-Designer
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Listbox, Label

#converter
#https://pypi.org/project/forex-python/
from forex_python.converter import CurrencyRates
c = CurrencyRates(force_decimal=True)

#datetime
from datetime import datetime, timedelta
today = datetime.today()
yesterday = today - timedelta(days=1)
one_week_ago = today - timedelta(days=7)
one_month_ago = today - timedelta(days=30)
one_year_ago = today - timedelta(days=365)

#change file location don't forget to change this too
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Administrator\Documents\GitHub\Currency_Converter\Currency Converter\assets\frame0")

#list
myList = ['IDR','BGN','ILS','GBP','DKK','CAD','JPY','HUF','RON','MYR','SEK','SGD','HKD','AUD','CHF',
          'KRW','CNY','TRY','HRK','NZD','THB','EUR','NOK','RUB','INR','MXN','CZK','BRL','PLN','PHP','ZAR']

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def input_from():
    pass

def convert():
    m1 = 'THB'
    m2 = 'JPY'

    t1 = '%.3f' %(float(c.convert(m1, m2, int(entry_2.get()), today)))
    t2 = '%.3f' %(float(c.get_rate(m1, m2, yesterday)))
    t3 = '%.3f' %(float(c.get_rate(m1, m2, one_week_ago)))
    t4 = '%.3f' %(float(c.get_rate(m1, m2, one_month_ago)))
    t5 = '%.3f' %(float(c.get_rate(m1, m2, one_year_ago)))

    t2 = f'{m1} : {m2}  ' + str(t2)
    t3 = f'{m1} : {m2}  ' + str(t3)
    t4 = f'{m1} : {m2}  ' + str(t4)
    t5 = f'{m1} : {m2}  ' + str(t5)

    entry_5.configure(text=t1, anchor="w")
    entry_1.configure(text=t2, anchor="center")
    entry_6.configure(text=t3, anchor="center")
    entry_7.configure(text=t4, anchor="center")
    entry_8.configure(text=t5, anchor="center")

    entry_3.configure(text=m1, anchor="w")
    entry_4.configure(text=m2, anchor="w")

window = Tk()

window.geometry("1200x830")
window.configure(bg = "#FFFFFF")
window.title("Currency Converter")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 830,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    332.00000000000045,
    302.8709716796875,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    332.00000000000045,
    493.19354248046875,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=convert,
    relief="flat"
)
button_1.place(
    x=221.00000000000045,
    y=368.0,
    width=221.09677124023438,
    height=64.263427734375
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    846.0000000000005,
    386.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    845.0000000000005,
    124.0,
    image=image_image_4
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    852.9233398437505,
    270.19801330566406,
    image=entry_image_1
)
entry_1 = Label(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Work Sans", 20 * -1)
)
entry_1.place(
    x=686.4621582031255,
    y=250.93020629882812,
    width=332.92236328125,
    height=36.535614013671875
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    258.50000000000045,
    303.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Work Sans", 20 * -1)
)
entry_2.place(
    x=159.00000000000045,
    y=284.0,
    width=199.0,
    height=37.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    411.00000000000045,
    303.5,
    image=entry_image_3
)
entry_3 = Label(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Work Sans", 20 * -1)
)
entry_3.place(
    x=367.00000000000045,
    y=284.0,
    width=88.0,
    height=37.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    411.00000000000045,
    493.0,
    image=entry_image_4
)
entry_4 = Label(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Work Sans", 20 * -1)
)
entry_4.place(
    x=367.00000000000045,
    y=473.0,
    width=88.0,
    height=38.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    258.50000000000045,
    493.5,
    image=entry_image_5
)
entry_5 = Label(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Work Sans", 20 * -1)
)
entry_5.place(
    x=159.00000000000045,
    y=474.0,
    width=199.0,
    height=37.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    852.284301757813,
    383.30006408691406,
    image=entry_image_6
)
entry_6 = Label(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Work Sans", 20 * -1)
)
entry_6.place(
    x=685.823120117188,
    y=364.0322570800781,
    width=332.92236328125,
    height=36.535614013671875
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    852.284301757813,
    496.5904235839844,
    image=entry_image_7
)
entry_7 = Label(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Work Sans", 20 * -1)
)
entry_7.place(
    x=685.823120117188,
    y=477.3226318359375,
    width=332.92236328125,
    height=36.53558349609375
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    852.284301757813,
    612.3323059082031,
    image=entry_image_8
)
entry_8 = Label(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Work Sans", 20 * -1)
)
entry_8.place(
    x=685.823120117188,
    y=593.0645141601562,
    width=332.92236328125,
    height=36.53558349609375
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    699.430786132813,
    220.1337890625,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    700.3034667968755,
    333.8454284667969,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    700.3034667968755,
    445.6618957519531,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    700.3034667968755,
    557.478271484375,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    292.00000000000045,
    733.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    385.00000000000045,
    625.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    489.00000000000045,
    680.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    220.00000000000045,
    648.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    92.00000000000045,
    752.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    593.0000000000005,
    617.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    68.00000000000045,
    649.8298950195312,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    629.0000000000005,
    742.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    925.0000000000005,
    747.0,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    742.0000000000005,
    758.522216796875,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    383.0127563476567,
    745.0,
    image=image_image_19
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    1115.0000000000005,
    777.51611328125,
    image=image_image_20
)

image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    1118.3994140625005,
    682.1935424804688,
    image=image_image_21
)

image_image_22 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(
    1114.0000000000005,
    565.0,
    image=image_image_22
)

canvas.create_text(
    133.00000000000045,
    96.0,
    anchor="nw",
    text="Currency ",
    fill="#000000",
    font=("ArchivoBlack Regular", 65 * -1,"bold")
)

canvas.create_text(
    133.00000000000045,
    166.80645751953125,
    anchor="nw",
    text="Converter!",
    fill="#000000",
    font=("Work Sans", 64 * -1,"bold")
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=input_from,
    relief="flat"
)
button_2.place(
    x=467.00000000000045,
    y=277.0,
    width=59.0,
    height=54.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=input_from,
    relief="flat"
)
button_3.place(
    x=463.00000000000045,
    y=469.0,
    width=63.0,
    height=49.0
)

canvas.create_text(
    728.547241210938,
    205.02896118164062,
    anchor="nw",
    text="1 Day",
    fill="#000000",
    font=("Work Sans", 28 * -1,"bold")
)

canvas.create_text(
    732.5784301757817,
    316.8454284667969,
    anchor="nw",
    text="1 Week",
    fill="#000000",
    font=("Work Sans", 28 * -1,"bold")
)

canvas.create_text(
    732.5784301757817,
    428.6618957519531,
    anchor="nw",
    text="1 Month",
    fill="#000000",
    font=("Work Sans", 28 * -1,"bold")
)

canvas.create_text(
    732.5784301757817,
    540.478271484375,
    anchor="nw",
    text="1 Year",
    fill="#000000",
    font=("Work Sans", 28 * -1,"bold")
)
window.resizable(False, False)
window.mainloop()