from asyncio.windows_events import NULL
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import mysql.connector as mc
import ast



class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.pushButton.clicked.connect(self.loginfunction)
    
    def loginfunction(self):
        try : 
            username = self.user_name.text()
            password = self.user_password.text()
            
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "traffic_record"
                )
            mycursor = mydb.cursor()
            query = "SELECT * FROM users WHERE user_name='"+ username + "' and password='"+password+"'"
            mycursor.execute(query)
            result = mycursor.fetchone()
            if result :
                main = information()
                widget.addWidget(main)
                widget.setFixedWidth(1091)
                widget.setFixedHeight(768)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                print("Succesfully Logged in")
            else :
                #self.lblError.setText = "Wrong inputs"
                print("Wrong inputs")
        except mc.Error as e:
            print ("Error Accure")
    
    

    
class information(QDialog):
    
    def __init__(self):
        super(information,self).__init__()
        loadUi("information.ui",self)
        
        self.pushButton.clicked.connect(self.show_All_information)
        self.pushButton_2.clicked.connect(self.show_All_systematic)
        self.pushButton_3.clicked.connect(self.show_All_Excedded)
        self.log_out_Buttton.clicked.connect(self.logout_process)
            
        
    def clear_table(self):
        self.tableWidget.setRowCount(0)    
    def addtable(self,columns):
        
        rowposition=self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowposition)
        for i,column in enumerate(columns):
                self.tableWidget.setItem( rowposition,i,QtWidgets.QTableWidgetItem(str(column)))

        
    def Myconverter(self,mydata):
    
        def cvt(data):
            try :
                return ast.literal_eval(data)
            
            except Exception:
                return str(data)
        return tuple(map(cvt,mydata))     
    
    def show_All_information(self):
        self.clear_table()
        self.changed_label.setText("التقرير الكلي لحركة المرور")

        try : 
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "traffic_record"
                )
            
            mycursor = mydb.cursor()
            query = "select * from cars_information"
            mycursor.execute(query)
            result = mycursor.fetchall()
            print("result :",result)
                
            for row in result:
                
                self.addtable(self.Myconverter(row))
                print("Succesfully Logged in")
        except mc.Error as e:
            print ("Error Accure")
    def show_All_Excedded(self):
        self.clear_table()
        self.changed_label.setText("تقرير بجميع السيارات المخالفة")
        try : 
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "traffic_record"
                )
            
            mycursor = mydb.cursor()
            query = "select * from cars_information where speed>80"
            mycursor.execute(query)
            result = mycursor.fetchall()
            print("result :",result)
                
            for row in result:
                
                self.addtable(self.Myconverter(row))
                print("Succesfully Logged in")
        except mc.Error as e:
            print ("Error Accure")
    def show_All_systematic(self):
        self.clear_table()
        self.changed_label.setText("تقرير بجميع السيارات النظامية")
        try : 
            mydb = mc.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "traffic_record"
                )
            
            mycursor = mydb.cursor()
            query = "select * from cars_information where speed<=80"
            mycursor.execute(query)
            result = mycursor.fetchall()
            print("result :",result)
                
            for row in result:
                
                self.addtable(self.Myconverter(row))
                print("Succesfully Logged in")
        except mc.Error as e:
            print ("Error Accure")
    def logout_process(self):
        out=Logout()
        widget.addWidget(out)
        widget.setFixedWidth(531)
        widget.setFixedHeight(621)
        widget.setCurrentIndex(widget.currentIndex() - 1)
        
class Logout(QDialog):
    
    def __init__(self):
        super(Logout,self).__init__()
        loadUi("login.ui",self)        




app = QApplication(sys.argv)
mainwindow=Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(531)
widget.setFixedHeight(621)
widget.show()
app.exec_()

