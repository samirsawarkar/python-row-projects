bookstore = ["book1","books2","books3","books4"]
rented_books =[]



class LibMang():
    def __init__(self,ll) -> None:
        self.name = ll
        
    def rent (sel,na):
        if na in bookstore and not na in rented_books :
            rented_books.append(na)
            print('heelo')
        else :
            print('sorry')    
    def returned(sel,na):
        if  na in bookstore and  na in rented_books :
            rented_books.remove(na)
        else :
            print("you want to donote this book")    

if __name__ == "__main__":
    

    ob = LibMang(bookstore)
    
    while True:
        print('''
        press 1 for see books \n
        press 2 for rent book \n
        press 3 for retun book \n
        press 4 for exit 
        ''')
        user = int(input('press ....'))

        if user == 1 :
            print(bookstore)
        elif user == 2:
            book = input("name of book")
            ob.rent(book)
        elif user == 3:
            book = input("name of book")
            ob.returned(book)    
        elif user == 4 :
            exit()
        else :
            print("invaild sytax")            