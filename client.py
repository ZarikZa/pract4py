import sqlite3
import SQL
import datetime


class Client:
    def vibor(login, pasword):
        conn = sqlite3.connect('proverka.db')
        cursor = conn.cursor()
        sql = f"SELECT id FROM Clients WHERE username ='{login}' AND password ='{pasword}'"
        cursor.execute(sql)
        result = cursor.fetchall()
        a = result[0]
        Client_ID = a[0]
        while True:
            print("Выберите функцию:\n1. Сделать заказ\n2. Изменить имя или пароль\n3. Посмотреть свои заказы\n4. Вернуться в главное меню")
            vibor = input()
            if vibor == "1":
                Client.order(Client_ID)
            elif vibor == "2":
                Client.zamena(login, pasword, Client_ID)
            elif vibor == "3":
                Client.allzakazs(Client_ID)
            elif vibor == "4":
                break
            else:
                print("Неверная операция")

    def order(Client_ID):
        conn = sqlite3.connect('proverka.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM Products")
        a = cursor.fetchall()
        if a == []:
            margo = {
                "Product": "Маргаритта",
                "Price": 500
            }
            havai = {
                "Product": "Гавайская",
                "Price": 600
            }
            pep = {
                "Product": "Пепперони",
                "Price": 400
            }
            cola = {
                "Product": "Coca-Cola",
                "Price": 100
            }
            fant = {
                "Product": "Fanta",
                "Price": 100,
            }
            sprite = {
                "Product": "Sprite",
                "Price": 120,
            }

            SQL.SQLmy.insertdata('Products', margo)
            SQL.SQLmy.insertdata('Products', havai)
            SQL.SQLmy.insertdata('Products', pep)
            SQL.SQLmy.insertdata('Products', cola)
            SQL.SQLmy.insertdata('Products', fant)
            SQL.SQLmy.insertdata('Products', sprite)
        SQL.SQLmy.vivod('Products')
        print("Выберите товары: ")
        print("\"Закончить\" - чтобы закончить заказ, \"Удалить\" - чтобы удалить позицию ")
        order = []
        price = 0
        while True:
            print("----------------------------")
            chooce = input("Выбор: ")
            if chooce == "Закончить":
                for j in range(len(order)):
                    sql = f"SELECT Price FROM Products WHERE Product ='{order[j]}'"
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    a = result[0]
                    b = a[0]
                    price += b
                for pos in range(len(order)):
                    data = {
                        "Products": order[pos],
                        "Datebill": datetime.datetime.today(),
                        "PriceOfOrd": price,
                        "Client_ID": Client_ID
                    }
                    SQL.SQLmy.insertdata('Bill', data)
                break
            elif chooce == "Удалить":
                chislo = int(input("Введите номер товара: "))
                order.pop(chislo)
            else:
                try:
                    sql = f"SELECT Product FROM Products WHERE id = {chooce}"
                    cursor.execute(sql)
                    sqlproduct = cursor.fetchall()
                    products = sqlproduct[0]
                    order.append(products[0])
                except:
                    print("Число слишко большое/маленькое или это текст, боже")
                for i in range(len(order)):
                    print(i, order[i])


    def zamena(login, pasword, Client_ID):
        print("Что изменять??\n1. Пароль\n2. Логин")
        vibor = input()
        if vibor == "1":
            print("Введите новый пароль: ")
            pasword_new = input()
            newdata = {
                "Username": login,
                "Password": pasword_new,
                "Dolznost_ID": 3
            }
            SQL.SQLmy.updateData('Clients', newdata, Client_ID)

        elif vibor == "2":
            print("Введите новый логин: ")
            login_new  = input()
            newdata = {
                "Username": login_new,
                "Password": pasword,
                "Dolznost_ID": 3
            }
            SQL.SQLmy.updateData('Clients', newdata, Client_ID)


    def allzakazs(Client_ID):
        conn = sqlite3.connect('proverka.db')
        cursor = conn.cursor()
        sql = f"SELECT * FROM Bill WHERE Client_ID = {Client_ID}"
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in range(len(result)):
            print(result[i])
