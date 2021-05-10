#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Classes import *
import PySimpleGUI as sg
import pysnooper

#COLUMN 1
sg.theme('DarkTanBlue')
col1_func = (
    'Set Inventory', 'Load Inventory', 'Save Inventory', 'Show Inventory', 'Remove Item',
    'Get Item Info', 'Total Cost', 'Get Number of Items' 
)
txt_col1 = [
    [sg.Txt('Name', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))],
    [sg.Txt('Price', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))],
    [sg.Txt('Amount', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))]
]
input_col1 = [
    [sg.Input('', size=(20,1), key='-inv_na-', do_not_clear=True)],
    [sg.Input('', size=(20,1), key='-inv_pr-', do_not_clear=True)],
    [sg.Input('', size=(20,1), key='-inv_am-', do_not_clear=True)]
    ]
col1 = [
    [sg.Txt('Inventory', relief=sg.RELIEF_RIDGE, font=('Helvetica', 15), justification='center', tooltip='Inventory are stock items that are hard to quantify per sale.')],
    [sg.Image(filename='stock-button1.png', background_color=None, size=(150, 150))],
    [sg.InputCombo(col1_func,size=(35,1), default_value='Inventory Commamnds', enable_events=False, key='-col1_func-')],
    [sg.Frame('Inventory', layout=[ [sg.Column(txt_col1, justification='center', element_justification='center'), sg.Column(input_col1, justification='center', element_justification='center')]], background_color=None)],
    [sg.Button('Submit', button_color=sg.TRANSPARENT_BUTTON, border_width=0, tooltip='Inventory: Make sure fields are filled aptly.', enable_events=True, focus=True, key='-Isubmit-', image_filename='button-green1.png', image_size=(50, 50))]
]

#COLUMN 2
col2_func =(
    'Set Stock', 'Load Stock', 'Save Stock', 'Show Stock', 'Remove Item',
    'Get Item Info', 'Total Cost', 'Get Number of Items'
)
txt_col2 = [
    [sg.Txt('Name', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))],
    [sg.Txt('Price', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))],
    [sg.Txt('Amount', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))]
]
input_col2 = [
    [sg.Input('', size=(20,1), key='-st_na-', do_not_clear=True)],
    [sg.Input('', size=(20,1), key='-st_pr-', do_not_clear=True)],
    [sg.Input('', size=(20,1), key='-st_am-', do_not_clear=True)]
    ]
col2 = [
    [sg.Txt('Stock', relief=sg.RELIEF_RIDGE, font=('Helvetica', 15), justification='center', tooltip='Stock items are: bun, cheese, pattie, egg!')],
    [sg.Image(filename='cheese-stock1.png', background_color=None, size=(150, 150))],
    [sg.InputCombo(col2_func,size=(35,1), default_value='Stock Commamnds', enable_events=False, key='-col2_func-')],
    [sg.Frame('Stock', layout=[ [sg.Column(txt_col2, justification='center', element_justification='center', background_color=None), sg.Column(input_col2, justification='center', element_justification='center', background_color=None)]], background_color=None)],
    [sg.Button('Submit', button_color=sg.TRANSPARENT_BUTTON, border_width=0, tooltip='Stock: Make sure fields are filled aptly.', enable_events=True, focus=True, key='-Ssubmit-', image_filename='button-green1.png', image_size=(50, 50))]
]

#COLUMN 3
col3_func = (
    'Make Sale', 'Load Sales', 'Get Sales', 'Show all Sales', 'Remove Sales', 'Save Sales'
)
txt_col3 = [
    [sg.Txt('Name', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))],
    [sg.Txt('Date', relief=sg.RELIEF_RIDGE, font=('Helvetica', 10))],
    [sg.Txt('')]
]
input_col3 = [
    [sg.Input('', size=(20,1), key='-sls_na-', do_not_clear=True)],
    [sg.Input('', size=(20,1), key='-sls_dte-', do_not_clear=True)],
    [sg.Txt('', size=(20,1), k='pad-blank')]
]
col3 = [
    [sg.Txt('Sales', relief=sg.RELIEF_RIDGE, font=('Helvetica', 15), justification='center', tooltip='The burger names are the same names as the classes(Noxie: Eg-> egg burger is EBURGER)')],
    [sg.Image(filename='hamburgers-button1.png', background_color=None, size=(150, 150))],
    [sg.InputCombo(col3_func,size=(35,1), default_value='Sales Commamnds', enable_events=False, key='-col3_func-')],
    [sg.Frame('Sales', layout=[ [sg.Column(txt_col3, justification='center', element_justification='center'), sg.Column(input_col3, justification='center', element_justification='center')]], background_color=None)],
    [sg.Button('Submit', button_color=sg.TRANSPARENT_BUTTON, border_width=0, tooltip='Sales: Make sure fields are filled aptly.', enable_events=True, focus=True, key='-SLsubmit-', image_filename='button-green1.png', image_size=(50, 50))]
]

#GENERAL OVERLAY
layout = [
    [sg.Frame(title='Kudzai\'s Stock App', layout=[ [sg.Column(col1, justification='center', element_justification='center'), sg.Column(col2, justification='center', element_justification='center'), sg.Column(col3, justification='center', element_justification='center')]], element_justification='center', font='Helvetica', background_color=None)],
    [sg.Multiline('', size=(50,10), key='DIS')],
    [sg.Exit()]
]

#MAKING THE WINDOW
sg.theme('DarkTanBlue')
window = sg.Window('BURGER APP', layout, element_justification='center', background_color=None, alpha_channel=1.5, button_color=sg.TRANSPARENT_BUTTON,)
INV = INVENTORY()
STK = STOCK()
SLS = SALES()
#@pysnooper.snoop()
while True:
    try:
        event, values = window.read()
        if event in ('Exit', None) or event == sg.WIN_CLOSED:
            break
        elif values['-col1_func-'] == 'Set Inventory' and event in ('-Isubmit-'):
            name, price, amount = values['-inv_na-'], values['-inv_pr-'], values['-inv_am-']
            if name and price and amount:
                INV.set_inventory(name, price, amount)
                window['DIS'].update(INV)
            else:
                window['DIS'].update('ERROR: Fill in the fields please!')
        elif values['-col1_func-'] == 'Load Inventory' and event in ('-Isubmit-'):
            FILENAME = values['-inv_na-']
            if FILENAME:
                INV.load_inventory(FILENAME)
                window['DIS'].update(INV)
            else:
                window['DIS'].update('ERROR: Fill in the fields please!')
        elif values['-col1_func-'] == 'Save Inventory' and event in ('-Isubmit-'):
            FILENAME = values['-inv_na-']
            if FILENAME:
                INV.save_inventory(FILENAME)
                window['DIS'].update(f'Inventory is saved to {FILENAME}.txt')
            else:
                window['DIS'].update('ERROR: Fill in the fields please!')
        elif values['-col1_func-'] == 'Show Inventory' and event in ('-Isubmit-'):
            window['DIS'].update(INV)
        elif values['-col1_func-'] == 'Remove Item' and event in ('-Isubmit-'):
            name, amount = values['-inv_na-'], values['-inv_am-']
            if name and amount:
                INV.rm_inventory(name, amount)
                window['DIS'].update(INV)
            else:
                window['DIS'].update('ERROR: Fill in the fields please!')
        elif values['-col1_func-'] == 'Get Item Info' and event in ('-Isubmit-'):
            name = values['-inv_na-']
            if name:
                window['DIS'].update(INV.get_itemInfo(name))
            else:
                window['DIS'].update('ERROR: Fill in the fields please!')
        elif values['-col1_func-'] == 'Total Cost' and event in ('-Isubmit-'):
            window['DIS'].update(f'Total cost of inventory => R{INV.get_totalValue()}')
        elif values['-col1_func-'] == 'Get Number of Items' and event in ('-Isubmit-'):
            window['DIS'].update(f'The number of items in inventory => {INV.get_NumINV()}')
        ####################################################################################

        elif values['-col2_func-'] == 'Set Stock' and event in ('-Ssubmit-'):
            name, price, amount = values['-st_na-'], values['-st_pr-'], values['-st_am-']
            if name and price and amount:
                STK.set_inventory(name, price, amount)
                window['DIS'].update(STK)
            else:
                window['DIS'].update('ERROR: Fill in the fields please!')
        elif values['-col2_func-'] == 'Load Stock' and event in ('-Ssubmit-'):
            FILENAME = values['-st_na-']
            if FILENAME:
                STK.load_inventory(FILENAME)
                window['DIS'].update(STK)
            else:
                window['DIS'].update('ERROR: Fill in the fields please!')
        elif values['-col2_func-'] == 'Save Stock' and event in ('-Ssubmit-'):
            FILENAME = values['-st_na-']
            if FILENAME:
                STK.save_inventory(FILENAME)
                window['DIS'].update(f'Stock is saved to {FILENAME}.txt')
            else:
                window['DIS'].update('ERROR: Fill in the fields please!')
        elif values['-col2_func-'] == 'Show Stock' and event in ('-Ssubmit-'):
            window['DIS'].update(STK)
        elif values['-col2_func-'] == 'Remove Item' and event in ('-Ssubmit-'):
            name, amount = values['-st_na-'], values['-st_am-']
            if name and amount:
                STK.rm_inventory(name, amount)
                window['DIS'].update(STK)
            else:
                window['DIS'].update('ERROR: Fill in the fields please!')
        elif values['-col2_func-'] == 'Get Item Info' and event in ('-Ssubmit-'):
            name = values['-st_na-']
            if name:
                window['DIS'].update(STK.get_itemInfo(name))
            else:
                window['DIS'].update('ERROR: Fill in the fields please!')
        elif values['-col2_func-'] == 'Total Cost' and event in ('-Ssubmit-'):
            window['DIS'].update(f'Total cost of stock => R{STK.get_totalValue()}')
        elif values['-col2_func-'] == 'Get Number of Items' and event in ('-Ssubmit-'):
            window['DIS'].update(f'The number of items in Stock => {STK.get_NumINV()}')

        ####################################################################################
        elif values['-col3_func-'] == 'Make Sale' and event in ('-SLsubmit-'):
            name, date = values['-sls_na-'], values['-sls_dte-']
            if name and date == '':
                SLS.mksale(name, STK)
                window['DIS'].update(SLS.get_sales())
            elif name and not date == '':
                SLS.mksale(name, STK, date_given=date)
                window['DIS'].update(SLS.get_sales(date))
            else:
                window['DIS'].update('ERROR: Fill in the fields please!')
            # with pysnooper.snoop():
            #     n = values['-sls_na-']
            #     d = values['-sls_dte-']
            #     print(n, d)
        elif values['-col3_func-'] == 'Load Sales' and event in ('-SLsubmit-'):
            FILENAME = values['-sls_na-']
            if FILENAME:
                SLS.load_sales(FILENAME)
                window['DIS'].update(SLS)
            else:
                window['DIS'].update('ERROR: Fill in the fields please!')
        elif values['-col3_func-'] == 'Get Sales' and event in ('-SLsubmit-'):
            date = values['-sls_dte-']
            if not date:
                window['DIS'].update(SLS.get_sales())
            elif date:
                window['DIS'].update(SLS.get_sales(date))
            else:
                window['DIS'].update('ERROR: Fill in the fields please!')
        elif values['-col3_func-'] == 'Show all Sales' and event in ('-SLsubmit-'):
            window['DIS'].update(SLS)
        elif values['-col3_func-'] == 'Remove Sales' and event in ('-SLsubmit-'):
            name, date = values['-sls_na-'], values['-sls_dte-']
            if name and not date:
                SLS.rmsale(name, STK)
                window['DIS'].update(f'{name} removed.\n{SLS.get_sales()}')
            elif name and date:
                SLS.rmsale(name, STK, date_given=date)
                window['DIS'].update(f'{name} removed.\n{SLS.get_sales(date_given=date)}')
            else:
                window['DIS'].update('ERROR: Fill in the fields please!')
        elif values['-col3_func-'] == 'Save Sales' and event in ('-SLsubmit-'):
            FILENAME = values['-sls_na-']
            if FILENAME:
                SLS.save_sales(FILENAME)
                window['DIS'].update(f'Sales saved to {FILENAME}.dat')
            else:
                window['DIS'].update('ERROR: Fill in the fields please!')
    except:
        window['DIS'].update(f'ERROR: not a normal error!!\nValues ==> {values}\nEvent ==> {event}')

    # with pysnooper.snoop():
    #     v = values
    #     e = event
    #     print(v,'\n', event)

window.close()
