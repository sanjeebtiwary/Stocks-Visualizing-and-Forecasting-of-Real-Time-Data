import PySimpleGUIWeb as sg
form = sg.FlexForm('Simple data entry form')  # begin with a blank form

layout = [
          [sg.Text('Please enter your Name, Address, Phone')],
          [sg.Text('Name', size=(15, 1)), sg.InputText('name')],
          [sg.Text('Address', size=(15, 1)), sg.InputText('address')],
          [sg.Text('Phone', size=(15, 1)), sg.InputText('phone')],
          [sg.Submit(), sg.Cancel()]
         ]

button, values = form.LayoutAndRead(layout)

print(button, values[0], values[1], values[2])