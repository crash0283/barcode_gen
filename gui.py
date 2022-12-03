import PySimpleGUI as sg

layout = [[sg.Text("Hello World!")], [sg.Text("Barcode Number"), sg.InputText()],
          [sg.Text("Number of Barcodes"), sg.InputText()],
          [sg.Text("Output File Name (Please include .pdf)"), sg.InputText()],
          [sg.Text("Barcode Prefix"), sg.InputText()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Gadget Lab Barcode Generator', layout)

event, values = window.read()
window.close()

text_input = values[0], values[1], values[2], values[3]
sg.popup("My Submitted Info", text_input)
