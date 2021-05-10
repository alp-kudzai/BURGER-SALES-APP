#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import date
import pickle
import pysnooper

class INVENTORY(object):
    '''
    Contains the stock items that are hard to measure per burger(till we get a scale)
    '''
    def __init__(self):
        self.inventory = {}

    #def build_inv(self)

    def set_inventory(self, name, price, amount):
        price, amount = float(price), int(amount)
        if name in self.inventory:
            self.inventory[name][0] += price
            self.inventory[name][1] += amount
        else:
            self.inventory[name] = [price, amount]
    #@pysnooper.snoop()
    def rm_inventory(self, name, amount):
        amount = int(amount)
        inv_amount = int(self.inventory[name][1])
        try:
            # print(self.inventory[name])
            # print(self.inventory[name][1])
            # print(amount)
            if (inv_amount - amount) <= 0:
                removed = self.inventory.pop(name)
                print(f'{removed} was removed!')
            else:
                self.inventory[name][0] -= round((self.inventory[name][0]/self.inventory[name][1])*amount, 2)
                self.inventory[name][1] -= amount
        except KeyError as e:
            print(f'{e} not in {type(self).__name__}')

    def get_itemInfo(self, name):
        #Can improve such that the display changes is there is one item left
        if name in self.inventory:
            dis = f'There are {self.inventory[name][1]} {name}s, Total cost => {self.inventory[name][0]}'
            return dis #self.inventory[name][0], self.inventory[name][1]
        else:
            return f'IndexError: {name} is not in the database!'

    def get_totalValue(self):
        value = 0
        for i in self.inventory.items():
            #print(i[1][0])
            value += float(i[1][0])
        return round(value, 2)

    def get_NumINV(self):
        '''
        Returns the total number of items in the inventory
        '''
        return len(self.inventory)

    def save_inventory(self, filename):
        filename += '.txt'
        Outfile = open(filename, 'w')
        _ = ''
        for i in self.inventory.items():
            _ += f'{i[0]} {i[1][0]} {i[1][1]}\n'
        Outfile.write(_[:-1])
        Outfile.close()

    def load_inventory(self, filename):
        filename += '.txt'
        inputfile = open(filename, 'r')
        print('opened file')
        data = inputfile.read().split('\n')
        inputfile.close()
        for d in data:
            if len(d) > 0:
                name, price, amount = d.split(' ')
                self.set_inventory(name, price, amount)
        
    def __repr__(self):
        display = f'*-*-*-*-*-*-*{type(self).__name__.upper()}-*-*-*-*-*-*-*-\n'
        for i in self.inventory.items():
            display += str(i[0])+'-->'+'R'+str(i[1][0])+', '+str(i[1][1]) + '\n'
        return display[:-1]

    def __str__(self):
        display = f'*-*-*-*-*-*-*{type(self).__name__.upper()}-*-*-*-*-*-*-*-\n'
        for i in self.inventory.items():
            display += str(i[0])+'-->'+'R'+str(i[1][0])+', '+str(i[1][1]) + '\n'
        return display[:-1]

class STOCK(INVENTORY):
    pass

#TODO: Make burger Superclass

class BURGER(object):
    '''
    Burger superclass
    '''
    def __init__(self):
        raise NotImplementedError
        self.price = None
        self.ingried = None
        
    def get_price(self):
        return self.price

    def get_ingried(self):
        return self.ingried

    def __repr__(self):
        return f'{type(self).__name__}({self.price}, {self.ingried})'

    def __str__(self):
        _ = ''
        for i in  self.ingried.items():
            _ += f'{i[1]} {i[0]}\n' 
        out = f'{type(self).__name__} price and ingriedients\n'\
            f'Price --> R{self.price}\nIngriedients --> {_[:-1]}'
        return out
#price and ingriedient variables for each type of burger#
#Standard burger
SBURGER_P = 13
SBURGER_I = {'cheese': 1, 'bun': 1, 'pattie':1, 'egg':0}
#Double Cheese Burger
DCBURGER_P = 16
DCBURGER_I = {'cheese': 2, 'bun': 1, 'pattie':1, 'egg':0}

#Egg Burger
EBURGER_P = 16
EBURGER_I = {'cheese': 1, 'bun': 1, 'pattie':1, 'egg':1}
#Double Cheese Egg Burger
DCEBURGER_P = 19
DCEBURGER_I = {'cheese': 2, 'bun': 1, 'pattie':1, 'egg':1}

#Double Pattie
DPBURGER_P = 21
DPBURGER_I = {'cheese': 1, 'bun': 1, 'pattie':2, 'egg':0}
#Double Pattie & Egg
DPEBURGER_P = 24
DPEBURGER_I = {'cheese': 1, 'bun': 1, 'pattie':2, 'egg':1}
#Double Pattie Double Cheese
DPDC_P = 24
DPDC_I = {'cheese': 2, 'bun': 1, 'pattie':2, 'egg':0}
#Double Pattie Double Cheese & Egg
DPDCE_P = 27
DPDCE_I = {'cheese': 2, 'bun': 1, 'pattie':2, 'egg':1}

class SBURGER(BURGER):
    def __init__(self):
        self.price = SBURGER_P
        self.ingried = SBURGER_I

class DCBURGER(BURGER):
    def __init__(self):
        self.price = DCBURGER_P
        self.ingried = DCBURGER_I

class EBURGER(BURGER):
    def __init__(self):
        self.price = EBURGER_P
        self.ingried = EBURGER_I

class DCEBURGER(BURGER):
    def __init__(self):
        self.price = DCEBURGER_P
        self.ingried = DCEBURGER_I

class DPBURGER(BURGER):
    def __init__(self):
        self.price = DPBURGER_P
        self.ingried = DPBURGER_I

class DPEBURGER(BURGER):
    def __init__(self):
        self.price = DPEBURGER_P
        self.ingried = DPEBURGER_I

class DPDC_BURGER(BURGER):
    def __init__(self):
        self.price = DPDC_P
        self.ingried = DPDC_I

class DPDCE_BURGER(BURGER):
    def __init__(self):
        self.price = DPDCE_P
        self.ingried = DPDCE_I

class SALES(object):
    def __init__(self):
        self.sales = {}
    #Creates a list of dictionaries
    #@pysnooper.snoop()
    def mksale(self, Burger, Stock, date_given=False):
        if Burger == 'SB': Burger = SBURGER()
        elif Burger == 'EB': Burger = EBURGER()
        elif Burger == 'DPB': Burger = DPBURGER()
        elif Burger == 'DCB': Burger = DCBURGER()
        elif Burger == 'DCEB': Burger = DCEBURGER()
        elif Burger == 'DPEB': Burger = DPEBURGER()
        elif Burger == 'DPDC': Burger = DPDC_BURGER()
        elif Burger == 'DPDCE': Burger = DPDCE_BURGER()
        else: raise Exception('There is no such burger name')
        print(Burger)
        if date_given:
            if date_given in self.sales:
                self.sales[date_given].append({f'{type(Burger).__name__}': Burger})
                for i in Burger.get_ingried().items():
                    Stock.rm_inventory(i[0], i[1])
                print('Sale made')
            else:
                self.sales[date_given] = []
                self.sales[date_given].append({f'{type(Burger).__name__}': Burger})
                for i in Burger.get_ingried().items():
                    Stock.rm_inventory(i[0], i[1])
                print('Sale made')
        elif str(date.today()) in self.sales:
            self.sales[str(date.today())].append({f'{type(Burger).__name__}': Burger})
            for i in Burger.get_ingried().items():
                Stock.rm_inventory(i[0], i[1])
            print('Sale existed, and is appended')
        else:
            self.sales[str(date.today())] = []
            self.sales[str(date.today())].append({f'{type(Burger).__name__}': Burger})
            for i in Burger.get_ingried().items():
                Stock.rm_inventory(i[0], i[1])
            print('Sale made')
    
    def rmsale(self, Burger, Stock, date_given=False):
        '''
        Burger --> is the burgers name not burger object
        Stock --> is the stock object
        '''
        if date_given:
            for i in self.sales[date_given]:
                if Burger in i.keys():
                    i.clear()
                    self.sales[date_given].pop(self.sales[date_given].index({}))
                    print(f'{Burger} removed.')
                    break
        else:
            if str(date.today()) in self.sales:
                for i in self.sales[str(date.today())]:
                    if Burger in i.keys():
                        i.clear()
                        self.sales[str(date.today())].pop(self.sales[str(date.today())].index({}))
                        print(f'{Burger} removed.')
                        break
            else:
                print('No sales made today')

    def get_sales(self, date_given=False):
        '''
        Returns sales that are recorded for today or any date given.(yyyy-mm-dd)
        '''
        if date_given and date_given in self.sales:
            l_sales = self.sales[date_given]
            dis = f'Sales for {date_given}\n-------------------------------\n'
            total = 0
            for d in l_sales:
                print(f'd is: {d} > {type(d)}')
                for th in d.items():
                    dis += '    {th[0]}\n'
                    total += th[1].get_price()
            dis += f'Total money made in sales: R{total}'
            return dis
            # for i in l_sales:
            #     dis += f'{i.keys()}\n'
            #     total_p += i.values().get_price()
            # dis += f'Total amount sold: {total_p}'
            # return dis
        elif str(date.today()) in self.sales:
            dis = f'Sales for today: {str(date.today())}.\n-------------------------------\n'
            l_sales = self.sales[str(date.today())]
            total = 0
            #print(l_sales)
            for d in l_sales:
                #print(f'd is: {d} > {type(d)}')
                for th in d.items():
                    dis += f'    {th[0]}\n'
                    total += th[1].get_price()
            dis += f'Total money made in sales: R{total}'
            return dis


            # l_sales = self.sales[str(date.today())]
            # dis = f'Sales for today {str(date.today())}\n-------------------------------\n'
            # total_p = 0
            # for i in l_sales:
            #     dis += f'{i.keys()}\n'
            #     total_p += i.values().get_price()
            # dis += f'Total amount sold: R{total_p}'
            # return dis

    def save_sales(self, filename):
        filename = filename + '.dat'
        outfile = open(filename, 'wb')
        _ = pickle.dump(self.sales, outfile, fix_imports=True)
        outfile.close()
        return print(f'We pickled sales in {filename} : {_}')

    def load_sales(self, filename):
        filename = filename + '.dat'
        infile = open(filename, 'rb')
        self.sales = pickle.load(infile)
        return print(f'We unpickled the data from {filename}: {self.sales}')

    def __repr__(self):
        dis = f'SALES({self.sales})'
        return dis
        
    def __str__(self):
        dis = 'Sales in database. \n'+'------------------- \n'
        total = 0
        for d in self.sales.items():
            dis += f'Sales for date -> {d[0]}\n'
            for b in d[1]:
                #print(f'b is a : {type(b)}')
                for l in b.items():
                    #print(f'l is a :{l[0]} => {type(l)}')
                    dis += f'   {l[0]} \n'
                    total += l[1].get_price()
        dis += f'Total Value in Sales Database --> R {total}'
        return dis


