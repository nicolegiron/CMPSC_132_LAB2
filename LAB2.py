# LAB2
#Due Date: 02/13/2021, 11:59PM

"""
### Collaboration Statement:

"""


class VendingMachine:

    '''
        >>> x=VendingMachine()
        >>> x.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> x.restock(215, 9)
        'Invalid item'
        >>> x.isStocked
        True
        >>> x.restock(156, 1)
        'Current item stock: 4'
        >>> x.getStock
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> x.purchase(156)
        'Please deposit $1.5'
        >>> x.purchase(156,2)
        'Please deposit $3.0'
        >>> x.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> x.deposit(3)
        'Balance: $3'
        >>> x.purchase(156,3)
        'Please deposit $1.5'
        >>> x.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> x.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> x.deposit(300)
        'Balance: $300'
        >>> x.purchase(876)
        'Invalid item'
        >>> x.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> x.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> x.purchase(156,3)
        'Please deposit $4.5'
        >>> x.deposit(4.5)
        'Balance: $4.5'
        >>> x.purchase(156,3)
        'Item dispensed'
        >>> x.getStock
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> x.purchase(156)
        'Item out of stock'
        >>> x.deposit(6)
        'Balance: $6'
        >>> x.purchase(254,3)
        'Item dispensed'
        >>> x.deposit(9)
        'Balance: $9'
        >>> x.purchase(879,3)
        'Item dispensed'
        >>> x.isStocked
        False
        >>> x.deposit(5)
        'Machine out of stock. Take your $5 back'
        >>> x.purchase(156,2)
        'Machine out of stock'
        >>> y=VendingMachine()
        >>> x.setPrice(156, 2.5)
        >>> x.getStock
        {156: [2.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> y.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
    '''

    def __init__(self):
        self.balance = 0
        self.stock = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}



    def purchase(self, item, qty=1):
        if self.isStocked == True:
            if item in self.stock:
                if self.stock.get(item)[1] != 0:
                    if qty <= self.stock.get(item)[1]:
                        if self.balance == (self.stock.get(item)[0]*qty):
                            self.balance = 0
                            self.stock.get(item)[1] -= qty
                            return "Item dispensed"
                        elif self.balance > (self.stock.get(item)[0]*qty):
                            balance = self.balance - (self.stock.get(item)[0]*qty)
                            self.balance = 0
                            self.stock.get(item)[1] -= qty
                            return "Item dispensed, take your ${} back".format(balance)
                        else:
                            return "Please deposit ${}".format(self.stock.get(item)[0]*qty-self.balance)
                    else:
                        return "Current {} stock: {}, try again".format(item, self.stock.get(item)[1])
                else:
                    return "Item out of stock"
            else:
                return "Invalid item"
        else:
            return "Machine out of stock"


    def deposit(self, amount):
        if self.isStocked == False:
            return "Machine out of stock. Take your ${} back".format(amount)
        else:
            self.balance+=amount
            return "Balance: ${}".format(self.balance)


    def restock(self, item, stock):
        if item in self.stock:
            self.stock.get(item)[1] += stock
            return "Current item stock: {}".format(self.stock.get(item)[1])
        else:
            return "Invalid item"


    @property
    def isStocked(self):
        zero = 0
        for value in self.stock.values():
            if value[1] == 0:
                zero+=1
        if zero == 4:
            return False
        else:
            return True


    @property
    def getStock(self):
        return self.stock


    def setPrice(self, item, new_price):
        if item in self.stock:
            self.stock.get(item)[0] = new_price
            return None
        else:
            return "Invalid item"


## Section 2
class Complex:

    '''
        >>> a=Complex(5.2,-6)
        >>> b=Complex(2,14)
        >>> a+b
        (7.2, 8i)
        >>> a-b
        (3.2, -20i)
        >>> a*b
        (94.4, 60.8i)
        >>> a/b
        (-0.368, -0.424i)
        >>> b*5
        (10, 70i)
        >>> 5*b
        (10, 70i)
        >>> 5+a
        (10.2, -6i)
        >>> a+5
        (10.2, -6i)
        >>> 5-b
        (3, -14i)
        >>> b-5
        (-3, 14i)
        >>> print(a)
        5.2-6i
        >>> print(b)
        2+14i
        >>> b
        (2, 14i)
        >>> isinstance(a+b, Complex)
        True
        >>> a.conjugate
        (5.2, 6i)
        >>> b.conjugate
        (2, -14i)
        >>> isinstance(b.conjugate, Complex)
        True
        >>> b==Complex(2,14)
        True
        >>> a==b
        False
        >>> a==9.5
        False
    '''

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def conjugate(self):
        return Complex(self.real, -self.imag)


    def __str__(self):
        if self.real == 0:
            return "{}i".format(self.imag)
        elif self.imag == 0:
            return "{}".format(self.real)
        else:
            if self.imag < 0:
                return "{}{}i".format(self.real, self.imag)
            else:
                return "{}+{}i".format(self.real, self.imag)


    def __repr__(self):
        return "({}, {}i)".format(self.real, self.imag)


    def __eq__(self, other):
        if type(self) != type(other):
            return False
        else:
            return self.real == other.real and self.imag == other.imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __radd__(self, other):
        return Complex(self.real + other, self.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __rsub__(self, other):
        return Complex(other.real - self.real, other.imag - self.imag)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag, self.real*other.imag + self.imag*other.real)

    def __rmul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag, self.real*other.imag + self.imag*other.real)

    def __truediv__(self, other):
        return Complex((self.real*other.real + self.imag*other.imag) / (other.real**2 + other.imag**2), (self.imag*other.real - self.real*other.imag) / (other.real**2 + other.imag**2))
