class Bankacount:
    name = ""
    acount_number = ""
    balance = 0
    
    def show_info(self):
        print("name:", self.name)
        print("acount_number:", self.acount_number)
        print("balance", self.balance)
        
        
    def add_money(self, money):
        self.balance += money
        print("balance after money:", self.balance)
        
        
    def dell_money(self, dell):
        if dell <= self.balance:
            self.balance -= dell
            print("Withdrawable balance", self.balance)
        else:
            print("not enoph money in acount")
            
acc1 = Bankacount() 
acc1.show_info()

""" dadn vigegi be class"""
acc1.name = "ali"
acc1.acount_number = "123456789"
acc1.balance = 500000

"""megdar dadn be hesab"""
acc1.add_money(200000)
acc1.dell_money(100000)
acc1.dell_money(900000)
