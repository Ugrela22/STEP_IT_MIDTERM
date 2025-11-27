import os

class ATM:
    def __init__(self):
        self.file = "users.txt"
        self.user = None
        if not os.path.exists(self.file):
            with open(self.file, 'w', encoding='utf-8') as f:
                f.write("1234,1111,გიორგი,5000.00\n")
                f.write("5678,2222,ნინო,3500.00\n")
                f.write("9999,3333,ლევან,10000.00\n")
    
    def read_users(self):
        users = []
        with open(self.file, 'r', encoding='utf-8') as f:
            for line in f:
                d = line.strip().split(',')
                if len(d) == 4:
                    # Remove spaces from balance before converting to float
                    balance_clean = d[3].replace(' ', '')
                    users.append({'card': d[0], 'pin': d[1], 'name': d[2], 'balance': float(balance_clean)})
        return users
    
    def save_users(self, users):
        with open(self.file, 'w', encoding='utf-8') as f:
            for u in users:
                f.write(f"{u['card']},{u['pin']},{u['name']},{u['balance']:.2f}\n")
    
    def find_user(self, card):
        for u in self.read_users():
            if u['card'] == card:
                return u
        return None
    
    def update_balance(self, new_balance):
        users = self.read_users()
        for u in users:
            if u['card'] == self.user['card']:
                u['balance'] = new_balance
        self.save_users(users)
        self.user['balance'] = new_balance
    
    def login(self):
        print("\n" + "="*40)
        print(" ბანკომატი". center(40))
        print("="*40)
        print("\n ტესტი: 1234/1111, 5678/2222, 9999/3333\n")
        
        for i in range(3):
            card = input(" ბარათი: ").strip()
            if not card:
                continue
            
            u = self.find_user(card)
            if not u:
                print(f" ბარათი არ მოიძებნა! დარჩენილი მცდელობები: {2-i}")
                continue
            
            pin = input(" PIN: ").strip()
            if u['pin'] == pin:
                self.user = u
                print(f"✅ მოგესალმებით, {u['name']}!\n")
                return True
            print(f" არასწორი PIN კოდი! დარჩენილი მცდელობები: {2-i}")
        
        print(" ბარათი დაბლოკილია! დაუკავშირდით ბანკს.")
        return False
    
    def balance(self):
        print(f"\n ბალანსი: {self.user['balance']:.2f} ₾")
        input("Enter...")
    
    def withdraw(self):
        print(f"\n ბალანსი: {self.user['balance']:.2f} ₾")
        print("1. 20₾  2.50₾  3.100₾  4.სხვა  0. უკან")
        
        choice = input("➤ ").strip()
        amounts = {'1': 20, '2': 50, '3': 100}
        
        if choice == '0':
            return
        elif choice in amounts:
            amount = amounts[choice]
        elif choice == '4':
            a = input("თანხა: ").strip()
            if not a.replace('.','',1).isdigit():
                print(" არასწორი თანხის ფორმატი!")
                return
            amount = float(a)
        else:
            print(" არასწორი არჩევანი! გთხოვთ აირჩიოთ 0-4.")
            return
        
        if amount <= 0:
            print(" თანხა უნდა იყოს დადებითი რიცხვი!")
            return
        if amount > self.user['balance']:
            print(" არასაკმარისი თანხა!")
            print(f" ხელმისაწვდომი ბალანსი: {self.user['balance']:.2f} ₾")
            return
        
        self.update_balance(self.user['balance'] - amount)
        print(f" ოპერაცია წარმატებული!")
        print(f" გატანილი თანხა: {amount:.2f} ₾")
        print(f" ახალი ბალანსი: {self.user['balance']:.2f} ₾")
        input("დააჭირეთ Enter-ს გასაგრძელებლად...")
    
    def deposit(self):
        print(f"\n ბალანსი: {self.user['balance']:.2f} ₾")
        
        a = input("თანხა (0-უკან): "). strip()
        if not a.replace('.','',1).isdigit():
            print(" არასწორი თანხის ფორმატი!")
            return
        
        amount = float(a)
        if amount == 0:
            return
        if amount <= 0:
            print(" თანხა უნდა იყოს დადებითი რიცხვი!")
            return
        if amount > 10000:
            print(" მაქსიმალური შეტანის ლიმიტი: 10,000 ₾")
            return
        
        self.update_balance(self.user['balance'] + amount)
        print(f" ოპერაცია წარმატებული!")
        print(f" შეტანილი თანხა: {amount:.2f} ₾")
        print(f" ახალი ბალანსი: {self.user['balance']:.2f} ₾")
        input("დააჭირეთ Enter-ს გასაგრძელებლად...")
    
    def menu(self):
        while True:
            print("\n" + "-"*40)
            print(f" {self.user['name']} |  {self.user['balance']:.2f}₾")
            print("-"*40)
            print("1. ბალანსი  2.გატანა  3.შეტანა  4.გასვლა")
            
            c = input("➤ ").strip()
            
            if c not in ['1', '2', '3', '4']:
                print(" არასწორი არჩევანი! გთხოვთ აირჩიოთ 1-4.")
                input("დააჭირეთ Enter-ს გასაგრძელებლად...")
                continue
            
            if c == '1':
                self.balance()
            elif c == '2':
                self.withdraw()
            elif c == '3':
                self.deposit()
            elif c == '4':
                print("\n მადლობა ჩვენი ბანკომატის გამოყენებისთვის!")
                print(" გთხოვთ, აიღოთ თქვენი ბარათი")
                break
    
    def run(self):
        if self.login():
            self.menu()


if __name__ == "__main__":
    ATM().run()