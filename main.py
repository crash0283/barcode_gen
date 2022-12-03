import os.path
from io import BytesIO
from pathlib import Path
import sys

import img2pdf
import PySimpleGUI as sg

from barcode import EAN13, Code39
from barcode.writer import ImageWriter

render_options = {
    "font_path": "C:/Windows/fonts/Arial.ttf"
}


def process_images(barcode_nums: list, num_barcodes, prefix,  out_file):
    images = []
    rv = BytesIO()
    pth = Path(out_file.name)
    for i in barcode_nums:
        for j in range(0, num_barcodes):
            myCode = Code39(str(i), writer=ImageWriter())
            myCode.write(rv, render_options)
            with open(f"{pth.parent}/{prefix}_{str(i)}.jpeg", "wb") as f:
                myCode.write(f)
                images.append(f.name)
    out_file.write(img2pdf.convert(images))


def create_barcodes(fileName, barcodeList: list, max_barcode_num, prefix):
    with open(fileName, "wb") as o_file:
        process_images(barcodeList, max_barcode_num, prefix, o_file)


layout = [[sg.Text("Please Enter the Required Data Below:")],
          [sg.Text("Barcode Number 1"), sg.InputText()],
          [sg.Text("Barcode Number 2"), sg.InputText()],
          [sg.Text("Barcode Number 3"), sg.InputText()],
          [sg.Text("Barcode Number 4"), sg.InputText()],
          [sg.Text("Barcode Number 5"), sg.InputText()],
          [sg.Text("Barcode Number 6"), sg.InputText()],
          [sg.Text("Barcode Number 7"), sg.InputText()],
          [sg.Text("Barcode Number 8"), sg.InputText()],
          [sg.Text("Barcode Number 9"), sg.InputText()],
          [sg.Text("Barcode Number 10"), sg.InputText()],
          [sg.HorizontalSeparator()],
          [sg.Text("Number of Barcodes"), sg.InputText("1")],
          [sg.HorizontalSeparator()],
          [sg.Text("Export File"), sg.SaveAs(default_extension='pdf', key='Save')],
          [sg.HorizontalSeparator()],
          [sg.Text("Barcode Image Prefix"), sg.InputText("barcode_img")],
          [sg.HorizontalSeparator()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Gadget Lab Barcode PDF Generator', layout)

event, values = window.read()
window.close()

input_key_list = [key for key, value in window.key_dict.items()
                  if isinstance(value, sg.Input)]

if event == "Cancel":
    sys.exit()
elif event == "Submit":
    fList = list(filter(None, [values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7],
                               values[8], values[9]]))
    create_barcodes(values['Save'], fList, int(values[11]), values[14])
    sg.popup("Barcodes Successfully Created!", text_color="black")

    # if all(map(str.strip, [values[key] for key in input_key_list])):
    # else:
    #     print("Cancel")
else:
    sys.exit()

# text_input = values[0], values[1], values[2], values[3]

