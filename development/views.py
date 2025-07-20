import sqlite3
from builtins import id

from django.contrib.messages.storage import session
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,"home.html")
def login(request):
    return render(request,"login.html")
def aboutus(request):
    return render(request,"aboutus.html")
def signup(request):
    return render(request,"signup.html")
def contactus(request):
    return render(request, "contactus.html")

def mall(request):
    return render(request, "mall.html")
def customer(request):
    return render(request,"customer.html")

def AdminHome(request):
    if session is None:
        return render("home.html")
    return render(request,"AdminHome.html")

def CustomerHome(request):
    return render(request,"CustomerHome.html")

def AdminSetting(request):
    return render(request,"AdminSetting.html")
def AdminAddress(request):
    return render(request,"AdminAddress.html")
def AdminContact(request):
    return render(request,"AdminContact.html")

def AdminEmail(request):
    return render(request,"AdminEmail.html")
def AdminPassword(request):
    return render(request,"AdminPassword.html")
def AccountCreation(request):
    return render(request,"AccountCreation.html")

def CustomerSetting(request):
    return render(request,"CustomerSetting.html")

def book(request):
    return render(request,"Booking.html")
def CustomerPassword(request):
    return render(request,"CustomerPassword.html")
def CustomerCity(request):
    return render(request,"CustomerCity.html")
def CustomerEmail(request):
    return render(request,"CustomerEmail.html")
def CustomerContact(request):
    return render(request,"CustomerContact.html")

def Account(request):
    return render(request,"Account.html")

def AccountDelete(request):
    return render(request,"EmployeeAccountDelete.html")

def SearchAccount(request):
    return render(request,"SearchAccount.html")

def GamingZone(request):
    return render(request,"GamingZone.html")

def AdminView(request):
    return render(request,"AdminView.html")

def Complaint(request):
    return render(request,"Complaint.html")

def EmployeeHome(request):
    return render(request,"EmployeeHome.html")

def EmployeeSetting(request):
    return render(request,"EmployeeSetting.html")

def EmployeeView(request):
    return render(request,"EmployeeView.html")

def EmpPassword(request):
    return render(request,"EmpPassword.html")

def EmpContact(request):
    return render(request,"EmpContact.html")

def EmpCity(request):
    return render(request,"EmpCity.html")

def EmpAddress(request):
    return render(request,"EmpAddress.html")

def EmpAccount(request):
    return render(request,"EmpAccount.html")

def EmpGamingZone(request):
    return render(request,"EmpGamingZone.html")

def EmpAccountDelete(request):
    return render(request,"EmpAccountDelete.html")

def logout(request):
    del request.session['auth']
    return render(request,"home.html")



def CustomerView(request):
    con = sqlite3.connect('db.sqlite3')
    operation = con.cursor()
    sql = 'select * from development_gamezonedetails'
    operation.execute(sql)
    records = operation.fetchall()
    return render(request,"CustomerView.html", {'recor': records})

def ViewGamingZone(request):
    con = sqlite3.connect('db.sqlite3')
    operation = con.cursor()
    sql = 'select * from development_gamezonedetails'
    operation.execute(sql)
    records = operation.fetchall()
    return render(request,"ViewGamingZone.html", {'recor': records})

def ViewEmpGamingZone(request):
    con = sqlite3.connect('db.sqlite3')
    operation = con.cursor()
    sql = 'select * from development_gamezonedetails'
    operation.execute(sql)
    records = operation.fetchall()
    return render(request,"ViewEmpGamingZone.html", {'recor': records})

def ViewComplaint(request):
    con = sqlite3.connect('db.sqlite3')
    operation = con.cursor()
    sql = 'select * from development_complaint'
    operation.execute(sql)
    records = operation.fetchall()
    context ={'my_data': records}
    return render(request, "ViewEmpComplaint.html", context)

def ViewEmpComplaint(request):
    con = sqlite3.connect('db.sqlite3')
    operation = con.cursor()
    sql = 'select * from development_complaint'
    operation.execute(sql)
    records = operation.fetchall()
    return render(request, "ViewEmpComplaint.html", {'recor': records})

def ViewBooking(request):
    con = sqlite3.connect('db.sqlite3')
    operation = con.cursor()
    sql = 'select * from development_booking'
    operation.execute(sql)
    records = operation.fetchall()
    context = {'my_data': records}
    return render(request, "ViewBooking.html", context)

def ViewEmpBooking(request):
    con = sqlite3.connect('db.sqlite3')
    operation = con.cursor()
    sql = 'select * from development_booking'
    operation.execute(sql)
    records = operation.fetchall()
    return render(request, "ViewEmpBooking.html", {'recor': records})

def Login(request):
    if request.method == "POST":
        id = request.POST.get("uid")
        Password = request.POST.get("pwd")
        user = request.POST.get("user")

        con = sqlite3.connect("db.sqlite3")
        operation=con.cursor()
        if user == 'Admin':
            request.session['auth'] = id
            sql = 'select * from development_admin where id = ? and password = ?'
            values = (id, Password)
            operation.execute(sql, values)
            records = operation.fetchone()
            if records is None:
                return render(request,"login.html",{'message':'Username or Password is incorrect'})
            else:
                return render(request, "AdminHome.html")
        elif user == 'Customer':
            request.session['auth'] = id
            sql = 'select * from development_customer where id = ? and password = ?'
            values = (id, Password)
            operation.execute(sql, values)
            records = operation.fetchone()
            if records is None:
                return render(request,"login.html",{'message':'Username or Password is incorrect'})
            else:
                return render(request, "customerHome.html")
        elif user == 'Operator':
            request.session['auth'] = id
            sql = 'select * from development_employee where id = ? and password = ?'
            values = (id, Password)
            operation.execute(sql, values)
            records = operation.fetchone()
            if records is None:
                return render(request,"login.html",{'message':'Username or Password is incorrect'})
            else:
                return render(request, "EmployeeHome.html")

def Booking(request):
    if request.method == "POST":
        bookingid = request.POST["bid"]
        customerid = request.POST["uid"]
        date_of_booking = request.POST["dOB"]
        date_for_booking = request.POST["dFB"]
        amount = request.POST["amount"]
        amountstatus = request.POST["status"]

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'insert into development_booking values(?,?,?,?,?,?)'
        values = (bookingid, customerid, date_of_booking, date_for_booking, amount, amountstatus,)
        operation.execute(sql, values)
        con.commit()
        con.close()

    return render(request, "CustomerHome.html")

def ComplaintRegister(request):
    if request.method == "POST":
        complaint_id = request.POST["cid"]
        fullname = request.POST["fName"]
        complaint = request.POST["complaint"]
        complaint_date = request.POST["cDate"]
        contact = request.POST["contact"]
        complaint_status = request.POST["status"]
        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'insert into development_complaint values(?,?,?,?,?,?)'
        values = (complaint_id, fullname, complaint, complaint_date, contact, complaint_status)
        operation.execute(sql, values)
        con.commit()
        con.close()
    return render(request, "CustomerSetting.html")
def AdminRegister(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        password = request.POST.get('pwd')
        fullname = request.POST.get('fname')
        email = request.POST.get('mail')
        contact = request.POST.get('cont')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('dob')
        address = request.POST.get('address')
        registration_number = request.POST.get('regno')
        organisation_name = request.POST.get('orgname')

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'insert into development_admin values(?,?,?,?,?,?,?,?,?,?)'
        values = (id, password, fullname, email, contact, gender, date_of_birth, address, registration_number,
            organisation_name)
        operation.execute(sql, values)
        con.commit()
        con.close()

    return render(request, "AdminHome.html")


def CustomerRegister(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        password = request.POST.get('pwd')
        fullname = request.POST.get('fname')
        email = request.POST.get('mail')
        dOB = request.POST.get('dob')
        gender = request.POST.get('gender')
        contact = request.POST.get('cont')
        city = request.POST.get('city')

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'insert into development_customer values(?,?,?,?,?,?,?,?)'
        values = (id, password, fullname, email, dOB,  gender, contact, city)
        operation.execute(sql, values)
        con.commit()
        con.close()

    return render(request, "CustomerHome.html")

def EmployeeRegister(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        password = request.POST.get('pwd')
        fullname = request.POST.get('fname')
        post = request.POST.get('post')
        salary = request.POST.get('salary')
        date_of_birth = request.POST.get('dob')
        contact = request.POST.get('cont')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        city = request.POST.get('city')

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'insert into development_employee values(?,?,?,?,?,?,?,?,?,?)'
        values = (id, password, fullname, post, salary, date_of_birth, contact, gender, address, city)
        operation.execute(sql, values)
        con.commit()
        con.close()

    return render(request, "AdminHome.html")

def GamingZoneRegister(request):
    if request.method == "POST":
        regno = request.POST.get('regno')
        place_Name = request.POST.get('pName')
        details = request.POST.get('details')
        contact = request.POST.get('cont')
        service = request.POST.get('services')
        charge = request.POST.get('charges')
        address = request.POST.get('address')

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'insert into development_gamezonedetails values(?,?,?,?,?,?,?)'
        values = (regno, place_Name, details, contact, service, charge, address)
        operation.execute(sql, values)
        con.commit()
        con.close()
    return render(request, "AdminHome.html")

def EmpGamingZoneRegister(request):
    if request.method == "POST":
        regno = request.POST.get('regno')
        place_Name = request.POST.get('pName')
        details = request.POST.get('details')
        contact = request.POST.get('cont')
        service = request.POST.get('services')
        charge = request.POST.get('charges')
        address = request.POST.get('address')

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'insert into development_gamezonedetails values(?,?,?,?,?,?,?)'
        values = (regno, place_Name, details, contact, service, charge, address)
        operation.execute(sql, values)
        con.commit()
        con.close()
    return render(request, "EmployeeHome.html")

def AdminPasswordChange(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        oldPassword = request.POST.get('Opwd')
        newPassword = request.POST.get('Npwd')
        ConfirmPassword = request.POST.get('Cpwd')

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'select * from development_admin where id = ? and password = ?'
        values = (id, oldPassword)
        operation.execute(sql, values)
        records = operation.fetchone()
        if records is None:
            return render(request,"AdminPassword.html",{'message':'Username or Password is incorrect'})
        else:
            if newPassword == ConfirmPassword:
                sql = 'update development_admin set password=? where id=?'
                values = (newPassword, id)
                operation.execute(sql, values)
                con.commit()
                con.close()
                return render(request, 'AdminSetting.html')
            else:
                return render(request,"AdminPassword.html",{'message':'Password does not match'})

def AdminAddressChange(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        newAddress = request.POST.get('nAddress')

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'update development_admin set address=? where id=?'
        values = (newAddress, id)
        operation.execute(sql, values)
        con.commit()
        con.close()
    return render(request, 'AdminSetting.html')
def AdminEmailChange(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        newEmail = request.POST.get('nEmail')

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'update development_admin set email=? where id=?'
        values = (newEmail, id)
        operation.execute(sql, values)
        con.commit()
        con.close()
    return render(request, 'AdminSetting.html')

def AdminContactChange(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        newContact = request.POST.get('nContact')

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'update development_admin set contact=? where id=?'
        values = (newContact, id)
        operation.execute(sql, values)
        con.commit()
        con.close()
    return render(request, 'AdminSetting.html')

def CustomerPasswordChange(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        oldPassword = request.POST.get('Opwd')
        newPassword = request.POST.get('Npwd')
        ConfirmPassword = request.POST.get('Cpwd')

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'select * from development_customer where id = ? and password = ?'
        values = (id, oldPassword)
        operation.execute(sql, values)
        records = operation.fetchone()
        if records is None:
            return render(request,"CustomerPassword.html",{'message':'Username or Password is incorrect'})
        else:
            if newPassword == ConfirmPassword:
                sql = 'update development_customer set password=? where id=?'
                values = (newPassword, id)
                operation.execute(sql, values)
                con.commit()
                con.close()
                return render(request, 'CustomerSetting.html')
            else:
                return JsonResponse({'error': 'No such user'})
                return render(request, "CustomerPassword.html", {'message': 'Password does not match'})

def CustomerCityChange(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        newCity = request.POST.get('nCity')

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'update development_customer set city=? where id=?'
        values = (newCity, id)
        operation.execute(sql, values)
        con.commit()
        con.close()
    return render(request, 'CustomerSetting.html')
def CustomerEmailChange(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        newEmail = request.POST.get('nEmail')

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'update development_customer set email=? where id=?'
        values = (newEmail, id)
        operation.execute(sql, values)
        con.commit()
        con.close()
    return render(request, 'CustomerSetting.html')

def CustomerContactChange(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        newContact = request.POST.get('nContact')

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'update development_customer set contact=? where id=?'
        values = (newContact, id)
        operation.execute(sql, values)
        con.commit()
        con.close()
    return render(request, 'CustomerSetting.html')

def ViewAllAccount(request):
    con = sqlite3.connect('db.sqlite3')
    operation = con.cursor()
    sql = 'select * from development_employee'
    operation.execute(sql)
    records = operation.fetchall()
    return render(request, 'ViewAllAccount.html', {'recor': records})

def EmployeeAccountDelete(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'delete from development_employee where id=?'
        values = (id,)
        operation.execute(sql, values)
        con.commit()
        con.close()
    return render(request, 'Account.html')

def EmpAccountDeletetion(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        password = request.POST.get('pwd')
        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'select * from development_employee where id = ? and password = ?'
        values = (id,password)
        operation.execute(sql, values)
        records = operation.fetchone()
        if records is None:
            return render(request,"EmpAccountDelete.html",{'message':'id or Password is incorrect'})
        else:
            sql = 'delete from development_employee where id = ?'
            values = (id,)
            operation.execute(sql, values)
            con.commit()
            con.close()
    return render(request, 'home.html')

def SearchEmployee(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'select * from development_employee where id=?'
        values = (id,)
        operation.execute(sql, values)
        records = operation.fetchone()
        con.close()
    return render(request, 'ViewAllAccount.html', {'recor': records})

def EmpCityChange(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        newCity = request.POST.get('nCity')

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'update development_employee set city=? where id=?'
        values = (newCity, id)
        operation.execute(sql, values)
        con.commit()
        con.close()
    return render(request, 'EmployeeSetting.html')

def EmpPasswordChange(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        oldPassword = request.POST.get('Opwd')
        newPassword = request.POST.get('Npwd')
        ConfirmPassword = request.POST.get('Cpwd')

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'select * from development_employee where id = ? and password = ?'
        values = (id, oldPassword)
        operation.execute(sql, values)
        records = operation.fetchone()
        if records is None:
            return render(request,"EmpPassword.html",{'message':'Username or Password is incorrect'})
        else:
            if newPassword == ConfirmPassword:
                sql = 'update development_employee set password=? where id=?'
                values = (newPassword, id)
                operation.execute(sql, values)
                con.commit()
                con.close()
                return render(request, 'EmployeeSetting.html')
            else:
                return render(request,"EmpPassword.html",{'message':'Passwords does not match'})

def EmpAddressChange(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        newAddress = request.POST.get('nAddress')

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'update development_employee set address=? where id=?'
        values = (newAddress, id)
        operation.execute(sql, values)
        con.commit()
        con.close()
    return render(request, 'EmployeeSetting.html')

def EmpContactChange(request):
    if request.method == "POST":
        id = request.POST.get('uid')
        newContact = request.POST.get('nContact')

        con = sqlite3.connect('db.sqlite3')
        operation = con.cursor()
        sql = 'update development_employee set contact=? where id=?'
        values = (newContact, id)
        operation.execute(sql, values)
        con.commit()
        con.close()
    return render(request, 'EmployeeSetting.html')