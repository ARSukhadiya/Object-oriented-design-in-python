from abc import ABC, abstractmethod, abstractproperty
from typing import Optional

class FranceDateFormatter:
    def formatDate(self, y, m, d):
        y, m, d = (str(x) for x in (y,m,d))
        y = '20' + y if len(y) == 2 else y
        m = '0' + m if len(m) == 1 else m
        d = '0' + d if len(d) == 1 else d
        return("{0}/{1}/{2}".format(d,m,y))

class USADateFormatter:
    def formatDate(self, y, m, d):
        y, m, d = (str(x) for x in (y,m,d))
        y = '20' + y if len(y) == 2 else y
        m = '0' + m if len(m) == 1 else m
        d = '0' + d if len(d) == 1 else d
        return("{0}-{1}-{2}".format(m,d,y))

class FranceCurrencyFormatter:
    def formatCurrency(self, base, cents):
        base, cents = (str(x) for x in (base, cents))
        if len(cents) == 0:
            cents = '00'
        elif len(cents) == 1:
            cents = '0' + cents

        digits = []
        for i,c in enumerate(reversed(base)):
            if i and not i % 3:
                digits.append(' ')
            digits.append(c)
        base = ''.join(reversed(digits))
        return "{0}€{1}".format(base, cents)

class USACurrencyFormatter:
    def formatCurrency(self, base, cents):
        base, cents = (str(x) for x in (base, cents))
        if len(cents) == 0:
            cents = '00'
        elif len(cents) == 1:
            cents = '0' + cents
        digits = []
        for i,c in enumerate(reversed(base)):
            if i and not i % 3:
                digits.append(',')
            digits.append(c)
        base = ''.join(reversed(digits))
        return "${0}.{1}".format(base, cents)

class FormatterFactory(ABC):
    @abstractmethod
    def createDateFormatter(self):
        pass
    @abstractmethod
    def createCurrencyFormatter(self):
        pass
    
class USAFormatterFactory(FormatterFactory):
    def createDateFormatter(self):
        return USADateFormatter()
    def createCurrencyFormatter(self):
        return USACurrencyFormatter()

class FranceFormatterFactory(FormatterFactory):
    def createDateFormatter(self):
        return FranceDateFormatter()
    def createCurrencyFormatter(self):
        return FranceCurrencyFormatter()

class ClientFormatterFactory:
    def createFormatterFactory(self, countryCode) -> FormatterFactory:
        factoryMap = {
            "US": USAFormatterFactory,
            "FR": FranceFormatterFactory}
        formatterFactory = factoryMap.get(countryCode)
        
        if formatterFactory is None:
            print("Could not find the country code!")

        # else:
        return formatterFactory()
        

def main():
    countryCode = input("Enter the country code: ")
    try:
        formatterFactory = ClientFormatterFactory().createFormatterFactory(countryCode)
        if formatterFactory is not None:
            formatter = formatterFactory.createDateFormatter()
            if formatter is not None:
                print(formatter.formatDate(2021, 3, 17))
            formatter = formatterFactory.createCurrencyFormatter()
            if formatter is not None:
                print(formatter.formatCurrency(899, 99))
    except ValueError as e:
        print(e)

main()