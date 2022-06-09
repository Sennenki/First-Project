# ====================================
#           Configuration
# ====================================

from flask import Flask, flash, render_template, request, redirect
from flask_login import UserMixin, LoginManager, login_required, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from AllForm import *
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime   
import uuid as uuid
import os

app = Flask(__name__)

app.config["SECRET_KEY"]='password'

# link old database
# app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///database.db'

# link new database 'mysql://username:password@localhot/Database'
app.config["SQLALCHEMY_DATABASE_URI"]='mysql+pymysql://root:$Enn3nK1@localhost/flaskProject'

# Get database model to SQLAlchemy
db = SQLAlchemy(app)
# Get database model to Migrate
migrate = Migrate(app, db)

# Path Upload Image
UPLOAD_IMG_FOLDER = 'static\Product_IMG'
app.config['UPLOAD_FOLDER'] = UPLOAD_IMG_FOLDER

#Setup Login System
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'Login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ====================================
#              Route Path
# ====================================

# ////////////////////////////// User PHASE ////////////////////////////////////

# User Home page
# ==========================================

@app.route('/', methods=["GET","POST"])
def Home():

    allowSearch = "yes"
    findItem = SearchForm()

    callItem = ProductData.query

    PromotionProduct = callItem.filter_by(group = "PM").all()
    BoxsetProduct = callItem.filter_by(group = "BS").all()

    stickyRice = callItem.filter_by(type = "SR").all()
    whiteRice = callItem.filter_by(type = "WR").all()

    PreOrderProduct = callItem.filter_by(group = "PO").all()

    return render_template('Client/HomePage.html',
            PromotionProduct=PromotionProduct,
            BoxsetProduct=BoxsetProduct,
            stickyRice=stickyRice,
            whiteRice=whiteRice,
            PreOrderProduct=PreOrderProduct,
            findItem=findItem,
            allowSearch=allowSearch
            )

@app.route('/SearchforItem', methods=["GET","POST"])
def SearchItem():
    allowSearch = "yes"
    findItem = SearchForm()
    keyWord = findItem.search.data

    itemFound = ProductData.query.filter(ProductData.name.like(f"%{keyWord}%")).all()
    countItem = len(itemFound)

    return render_template('Client/HomePage.html',
            findItem=findItem,
            itemFound=itemFound,
            countItem=countItem,
            allowSearch=allowSearch
            )

# User Login page
# ==========================================

@app.route('/Login', methods=["GET","POST"])
def Login():

    form = LoginForm()

    if request.method == "POST":

        userId = form.email.data
        userPassword = form.password.data

        readUser = User.query
        getUser = readUser.filter_by(email = userId).first()

        if getUser:

            if check_password_hash(getUser.encrypt_password, userPassword):
                login_user(getUser)
                return redirect(f'/Account/id={getUser.email}')

            else:
                flash("Something wrong, Try again !!")
                form.password.data = ''
                redirect ('/Login')
        
        else:
            flash("User doesn't exist, Try again !!")
            form.email.data = ''
            redirect ('/Login')


    return render_template('Client/login.html',
            form=form
            )

# User Logout page
# ==========================================

@app.route('/Logout', methods=["GET","POST"])
@login_required
def Logout():
    logout_user()
    flash("You have been logged out.")

    return redirect('/Login')

# User Register page
# ==========================================

@app.route('/Register', methods=["GET","POST"])
def Register():

    form = RegisterForm()

    state = None

    if request.method == "POST":
        fname = form.fname.data 
        lname = form.lname.data 
        email = form.email.data 
        password = form.password.data 
        confirm = form.conpassword.data 
        accept = form.accept.data 

        loadUser = User.query.filter_by(email = email).first()

        if loadUser:
            flash("This account already use! Try again...")
            form.email.data = ""

        else:
            if confirm == password:

                hashed = generate_password_hash(password)
            # INSERT INTO User (fname, lname, bla, bla,) VALUES (fname, lname, bla, bla)
                newAccount = User(
                    fname = fname,
                    lname = lname,
                    email = email,
                    encrypt_password = hashed,
                    accept = accept
                )

                db.session.add(newAccount)
                db.session.commit()

                state = "Accept"

                return render_template('Client/Register.html',
                        form=form,
                        state=state,
                        fname=fname,
                        lname=lname
                        )

            else:
                flash("The password must match! Try again...")

    return render_template('Client/Register.html',
            form=form,
            state=state
            )

# User Member page
# ==========================================

@app.route('/Account/id=<input>', methods=["GET","POST"])
@login_required
def Member(input):

    allowSearch = "yes"

    findItem = SearchForm()

    callItem = ProductData.query

    PromotionProduct = callItem.filter_by(group = "PM").all()
    BoxsetProduct = callItem.filter_by(group = "BS").all()

    stickyRice = callItem.filter_by(type = "SR").all()
    whiteRice = callItem.filter_by(type = "WR").all()

    PreOrderProduct = callItem.filter_by(group = "PO").all()

    callOrder = OrderList.query.filter_by(client = input).all()
    counter = len(callOrder)

    return render_template('Client/HomePage.html',
            PromotionProduct=PromotionProduct,
            BoxsetProduct=BoxsetProduct,
            stickyRice=stickyRice,
            whiteRice=whiteRice,
            PreOrderProduct=PreOrderProduct,
            counter=counter,
            findItem=findItem,
            allowSearch=allowSearch
            )


@app.route('/Account/id=<input>/AddtoCart/code=<code>', methods=["GET","POST"])
def AddtoCart(input,code):

    current_user = User.query.filter_by(email = input).first()

    callOrder = OrderList.query.filter_by(client = input).filter_by(code = code).first()

    if callOrder:
        pass
    else:
        addOrder = OrderList(
            code = code,
            client = input,
            amount = 0
        )

        db.session.add(addOrder)
        db.session.commit()

    return redirect(f'/Account/id={current_user.email}')

@app.route('/Account/id=<input>/SearchforItem', methods=["GET","POST"])
@login_required
def loggedSearchItem(input):
    allowSearch = "yes"
    findItem = SearchForm()
    keyWord = findItem.search.data

    itemFound = ProductData.query.filter(ProductData.name.like(f"%{keyWord}%")).all()
    countItem = len(itemFound)

    current_user = User.query.filter_by(email = input).first()

    return render_template('Client/HomePage.html',
            current_user=current_user,
            findItem=findItem,
            itemFound=itemFound,
            countItem=countItem,
            allowSearch=allowSearch
            )

# User Member Profile page
# ==========================================

@app.route('/Account/id=<input>/Profile', methods=["GET","POST"])
@login_required
def Profile(input):

    updateProfile = RegisterForm()
    updatePassword = RegisterForm()
    updateLocation = DeliveryForm()

    current_user=User.query.filter_by(email = input).first()
    print(current_user.password)

    identity = Address.query.filter(Address.email.like(f"%{current_user.email}%")).order_by(Address.date_log.desc()).first()
    getName = identity.name
    theName = getName.split(" ")
    fname = theName[0]    
    lname = theName[1]    

    updateLocation.province.choices = [(identity.province, identity.province)]
    updateLocation.district.choices = [(identity.district, identity.district)]
    updateLocation.subDistrict.choices = [(identity.subDistrict, identity.subDistrict)]

    return render_template('Client/MemberProfile.html',
            current_user=current_user,
            updateProfile=updateProfile,
            updateLocation=updateLocation,
            updatePassword=updatePassword,
            identity=identity,
            fname=fname,
            lname=lname
            )

@app.route('/Account/id=<input>/Profile/UploadIMG', methods=["GET","POST"])
def EditProfileIMG(input):

    current_user=User.query.get_or_404(input)

    nameFile = request.files['file']
    saveFile = secure_filename(nameFile.filename)
    uniqueName = str(uuid.uuid1()) + "_" + saveFile

    current_user.file = uniqueName

    db.session.commit()
    nameFile.save(os.path.join(app.config['UPLOAD_FOLDER'], uniqueName))

    
    return redirect(f'/Account/id={current_user.email}/Profile')

@app.route('/Account/id=<input>/Profile/UpdateLocation', methods=["GET","POST"])
def EditLocation(input):

    current_user = User.query.get_or_404(input)
    locate = Address.query.filter(Address.email.like(f"%{current_user.email}%")).order_by(Address.date_log.desc()).first()
    locate = Address.query.get_or_404(locate.id)

    updateLocation = DeliveryForm()

    locate.email = updateLocation.email.data
    locate.fname = updateLocation.fname.data
    locate.lname = updateLocation.lname.data
    locate.address = updateLocation.address.data
    locate.province = updateLocation.province.data
    locate.district = updateLocation.district.data
    locate.subDistrict = updateLocation.subDistrict.data
    locate.postCode = updateLocation.postcode.data
    locate.telephone = updateLocation.telNumber.data

    db.session.commit()

    
    return redirect(f'/Account/id={current_user.email}/Profile')

@app.route('/Account/id=<input>/Profile/RePassword', methods=["GET","POST"])
def RePassword(input):

    updateProfile = RegisterForm()

    current_user = User.query.get_or_404(input)
    getpassword = updateProfile.password.data
    print(getpassword)
    current_user.password = request.values['password']

    db.session.commit()

    
    return redirect(f'/Account/id={current_user.email}/Profile')

# User Cart page
# ==========================================

@app.route('/Account/id=<input>/Cart', methods=["GET","POST"])
@login_required
def Cart(input):

    current_user=User.query.filter_by(email = input).first()

    callOrder = OrderList.query.filter_by(client = input).all()

    userCart = []
    sequence = 0

    for eachOrder in callOrder:
        callItem = ProductData.query.filter_by(code = eachOrder.code).first()

        obj = {}
        obj['id'] = eachOrder.id
        obj['file'] = callItem.file
        obj['name'] = callItem.name
        obj['price'] = int(callItem.price)
        obj['amount'] = int(eachOrder.amount)
        obj['sequence'] = int(sequence)

        userCart.append(obj)

        sequence = sequence+1

    counter = len(callOrder)

    return render_template('Client/MemberCart.html',
            current_user=current_user,
            callOrder=callOrder,
            counter=counter,
            userCart=userCart
            )

@app.route('/Account/id=<input>/Cart/Additem=<id>', methods=["GET","POST"])
def AddItem(input,id):

    getItem = OrderList.query.filter_by(client = input).filter_by(id = id).first()

    newAmount = int(getItem.amount)+1

    getItem.amount = newAmount

    db.session.commit()

    return redirect(f'/Account/id={input}/Cart')

@app.route('/Account/id=<input>/Cart/Removeitem=<id>', methods=["GET","POST"])
def RemoveItem(input,id):

    getItem = OrderList.query.filter_by(client = input).filter_by(id = id).first()

    newAmount = int(getItem.amount)-1

    getItem.amount = newAmount

    db.session.commit()

    return redirect(f'/Account/id={input}/Cart')

@app.route('/Account/id=<input>/Cart/Delete', methods=["GET","POST"])
def DeleteItem(input):

    callOrder = OrderList.query.filter_by(client = input).all()

    for eachItem in callOrder:
        id = eachItem.id
        dataUser = OrderList.query.get_or_404(id)

        db.session.delete(dataUser)
        db.session.commit()

    print("Delete Done")

    return redirect(f'/Account/id={input}/Cart')

# User Information page
# ==========================================

@app.route('/Account/id=<input>/Information', methods=["GET","POST"])
@login_required
def Informationt(input):

    Delivery = DeliveryForm()
    
    current_user = User.query.filter_by(email = input).first()

    test = Address.query.order_by(Address.date_log.desc()).all()

    callOrder = OrderList.query.filter_by(client = input).filter(OrderList.amount.notlike("0%")).all()

    userCart = []

    for eachOrder in callOrder:
        callItem = ProductData.query.filter_by(code = eachOrder.code).first()

        obj = {}
        obj['id'] = eachOrder.id
        obj['file'] = callItem.file
        obj['name'] = callItem.name
        obj['price'] = int(callItem.price)
        obj['amount'] = int(eachOrder.amount)

        userCart.append(obj)

    return render_template('Client/Payment.html', 
            current_user=current_user, 
            userCart=userCart, 
            Delivery=Delivery,
            test=test
            )

@app.route('/Account/id=<input>/Information/getAddress', methods=["GET","POST"])
def GetInformationt(input):

    Delivery = DeliveryForm()

    getUser = User.query.filter_by(email = input).first()
    print(getUser)

    if request.method == "POST":

        destination = Delivery.other.data 
        print("other",destination)
        
        if destination == True:
            fname = Delivery.fname2.data 
            lname = Delivery.lname2.data 
            email = Delivery.email2.data 
            address = Delivery.address2.data 
            province = Delivery.province2.data 
            district = Delivery.district2.data 
            subDistrict = Delivery.subDistrict2.data 
            postCode = Delivery.postcode2.data 
            telephone = Delivery.telNumber2.data
            destination = "Other"


        else:
            fname = Delivery.fname.data 
            lname = Delivery.lname.data 
            email = Delivery.email.data 
            address = Delivery.address.data 
            province = Delivery.province.data 
            district = Delivery.district.data 
            subDistrict = Delivery.subDistrict.data 
            postCode = Delivery.postcode.data 
            telephone = Delivery.telNumber.data 
            destination = "Owner"

        newAddress = Address(
            name= fname + " " + lname,
            email=email,
            address=address,
            province=province,
            district=district,
            subDistrict=subDistrict,
            postCode=postCode,
            telephone=telephone,
            destination=destination,
            taxName = Delivery.Tax_company.data,
            taxPayer = Delivery.Tax_payer.data,
            taxAddress = Delivery.Tax_location.data 
        )

        db.session.add(newAddress)
        db.session.commit()

        return redirect(f'/Account/id={getUser.email}/Payment')

    return redirect(f'/Account/id={getUser.email}/Information')

# User Payment page
# ==========================================

@app.route('/Account/id=<input>/Payment', methods=["GET","POST"])
@login_required
def Payment(input):

    payment = UserPayment()
    
    accept = None
    
    current_user = User.query.filter_by(email = input).first()

    account = current_user.email
    owner = Address.query.filter_by(email = account).first()

    callOrder = OrderList.query.filter_by(client = input).filter(OrderList.amount.notlike("0%")).all()

    userCart = []

    for eachOrder in callOrder:
        callItem = ProductData.query.filter_by(code = eachOrder.code).first()

        obj = {}
        obj['id'] = eachOrder.id
        obj['file'] = callItem.file
        obj['name'] = callItem.name
        obj['price'] = int(callItem.price)
        obj['amount'] = int(eachOrder.amount)

        userCart.append(obj)

    return render_template('Client/Payment_method.html', 
            current_user=current_user, 
            userCart=userCart, 
            payment=payment,
            owner=owner
            )

@app.route('/Account/id=<input>/Payment/getPayment', methods=["GET","POST"])
def GetPayment(input):
    
    payment = UserPayment()

    getUser = User.query.filter_by(email = input).first()

    select_choices= request.values['select_choices']

    if request.method == "POST":

        nameFile = request.files['file']
        saveFile = secure_filename(nameFile.filename)
        uniqueName = str(uuid.uuid1()) + "_" + saveFile

        newPayment = PaymentInfo(
            select_choices=select_choices,
            name= payment.name.data,
            email= payment.email.data,
            telephone= payment.phone.data,
            date= payment.date.data,
            time= payment.time.data,
            cost= payment.cost.data,
            file= uniqueName,
            serial= payment.serial.data,
            description= payment.description.data,
        )

        db.session.add(newPayment)
        db.session.commit()
        nameFile.save(os.path.join(app.config['UPLOAD_FOLDER'], uniqueName))

        return redirect(f'/Account/id={getUser.email}/Payment/accept')

    return redirect(f'/Account/id={getUser.email}/Payment')

@app.route('/Account/id=<input>/Payment/<result>', methods=["GET","POST"])
@login_required
def acceptPayment(input,result):

    payment = UserPayment()

    accept = result
    
    current_user = User.query.filter_by(email = input).first()

    user = current_user.email
    order_bill = PaymentInfo.query.filter_by(email = user).order_by(PaymentInfo.date_log.desc()).first()

    callOrder = OrderList.query.filter_by(client = input).filter(OrderList.amount.notlike("0%")).all()
    countOrder = len(callOrder)

    userCart = []

    for eachOrder in callOrder:
        callItem = ProductData.query.filter_by(code = eachOrder.code).first()

        obj = {}
        obj['id'] = eachOrder.id
        obj['code'] = eachOrder.code
        obj['file'] = callItem.file
        obj['name'] = callItem.name
        obj['price'] = int(callItem.price)
        obj['amount'] = int(eachOrder.amount)

        userCart.append(obj)

    return render_template('Client/Payment_method.html', 
            current_user=current_user, 
            userCart=userCart, 
            payment=payment,
            order_bill=order_bill,
            accept=accept,
            countOrder=countOrder
            )

@app.route('/SendOrder/id=<input>', methods=["GET","POST"])
def SendOrder(input):

    getUser = User.query.filter_by(email = input).first()

    callOrder = OrderList.query.filter_by(client = input).filter(OrderList.amount.notlike("0%")).all()

    for eachOrder in callOrder:

        getProduct = ProductData.query.filter_by(code = eachOrder.code).first()
        getaddress = Address.query.filter_by(email = getUser.email).order_by(Address.date_log.desc()).first()

        Send = OrderConfirm(
            item = getProduct.id,
            owner = getaddress.id,
            amount = eachOrder.amount
        )

        db.session.add(Send)
        db.session.commit()

    for eachOrder in callOrder:
        id = eachOrder.id
        getid = OrderList.query.get_or_404(id)
        db.session.delete(getid)
        db.session.commit()
    
    return redirect(f'/Account/id={getUser.email}')
    

# ////////////////////////////// ADMIN PHASE ////////////////////////////////////

# Admin Login page
# ==========================================

@app.route('/LoginForAdmin', methods=["GET","POST"] )
def AdminLogin():
    AdLog = LoginForm()

    loadUser = User.query.filter(User.email.like("Admin%")).first()

    if request.method == "POST":

        getUser = request.values['email']
        getPassword = request.values['password']

        if getUser != loadUser.email:

            flash("User doesn't exist, Try again !!")
            redirect ('/LoginForAdmin')

        else:

            if check_password_hash(loadUser.encrypt_password, getPassword):
                login_user(loadUser)
                return redirect('/DashboardForAdmin')

            else:
                flash("Something wrong, Try again !!")
                redirect ('/LoginForAdmin')


    return render_template("Admin/AdminCheckpoint.html", AdLog=AdLog)

# Admin Logout page
# ==========================================

@app.route('/LogoutForAdmin', methods=["GET","POST"] )
@login_required
def AdminLogout():
    logout_user()
    flash("You have been logged out.")

    return redirect('/LoginForAdmin')

# Admin Dashboard page
# ==========================================

@app.route('/DashboardForAdmin', methods=["GET","POST"] )
@login_required
def AdDashboard():

    CurrentDate = datetime.now().strftime("%Y-%b-%d | %H : %M")

    Information = User.query.order_by(User.id).all()
    AmountUser = len(Information)
    
    Detail = ProductData.query.order_by(ProductData.id).all()
    AmountProduct = len(Detail)

    getOrder = OrderConfirm.query.group_by(OrderConfirm.date_log).all()
    countOrder = len(getOrder)
    allItem = OrderConfirm.query.order_by(OrderConfirm.id).all()

    return render_template("Admin/Adminpage.html",
            CurrentDate=CurrentDate,
            AmountUser=AmountUser,
            AmountProduct=AmountProduct,
            getOrder=getOrder,
            allItem=allItem,
            countOrder=countOrder
            )


@app.route('/DashboardForAdmin/Delete/<input>', methods=["GET","POST"] )
def DelOrder(input):

    Order = OrderConfirm.query.filter_by(date_log = input).all()
    for each in Order:
        item = each.id
        delId = OrderConfirm.query.get_or_404(item)
        db.session.delete(delId)
        db.session.commit()

    return redirect('/DashboardForAdmin')

@app.route('/DashboardForAdmin/DeleteAll', methods=["GET","POST"] )
def DelAllOrder():

    Order = OrderConfirm.query.order_by(OrderConfirm.id).all()
    print(Order)
    for each in Order:
        item = each.id
        delId = OrderConfirm.query.get_or_404(item)
        db.session.delete(delId)
        db.session.commit()

    return redirect('/DashboardForAdmin')

# Admin Customer page
# ==========================================

@app.route('/CustomerForAdmin', methods=["GET","POST"] )
@login_required
def Customer():
    dataUser = RegisterForm()

    Information = User.query.order_by(User.id).all()

    return render_template("Admin/AdminCustomer.html", 
            dataUser=dataUser, 
            Information=Information
            )

@app.route('/CustomerForAdmin/Add', methods=["GET","POST"])
def AddCustomer():

    getPassword = request.values['password'] 
    hashed_password = generate_password_hash(getPassword, "sha256")

    dataUser = User(
        fname = request.values['fname'],
        lname = request.values['lname'],
        email = request.values['email'],
        encrypt_password = hashed_password
    )

    db.session.add(dataUser)
    db.session.commit()

    return redirect('/CustomerForAdmin')

@app.route('/CustomerForAdmin/Update/<input>', methods=["GET","POST"])
def UpdateCustomer(input):

    dataUser = User.query.get_or_404(input)

    getPassword = request.values['password'] 
    hashed_password = generate_password_hash(getPassword, "sha256")

    if request.method == "POST":

        nameFile = request.files['file']
        saveFile = secure_filename(nameFile.filename)
        uniqueName = str(uuid.uuid1()) + "_" + saveFile

        dataUser.fname = request.values['fname'],
        dataUser.lname = request.values['lname'],
        dataUser.email = request.values['email'],
        dataUser.encrypt_password = hashed_password
        dataUser.file = uniqueName

        db.session.commit()

        nameFile.save(os.path.join(app.config['UPLOAD_FOLDER'], uniqueName))

    return redirect('/CustomerForAdmin')

@app.route('/CustomerForAdmin/Delete/<input>')
def DeleteCustomer(input):

    dataUser = User.query.get_or_404(input)

    db.session.delete(dataUser)
    db.session.commit()

    return redirect('/CustomerForAdmin')

# Admin Product page
# ==========================================

@app.route('/ProductForAdmin', methods=["GET","POST"] )
@login_required
def Product():
    dataProduct = ProductForm()

    Detail = ProductData.query.order_by(ProductData.id).all()

    test = ProductData.query.order_by(ProductData.file).all()

    return render_template("Admin/AdminProduct.html", 
            dataProduct=dataProduct, 
            Detail=Detail,
            test=test
            )

@app.route('/ProductForAdmin/Add', methods=["GET","POST"])
def AddProduct():
    if request.method == "POST":

        nameFile = request.files['file']
        saveFile = secure_filename(nameFile.filename)
        uniqueName = str(uuid.uuid1()) + "_" + saveFile

        dataProduct = ProductData(
            type = request.values['type'],
            group = request.values['group'],
            code = request.values['code'],
            name = request.values['name'],
            price = request.values['price'],
            deal = request.values['deal'],
            file = uniqueName,
        )

        db.session.add(dataProduct)
        db.session.commit()

        nameFile.save(os.path.join(app.config['UPLOAD_FOLDER'], uniqueName))

    return redirect('/ProductForAdmin')

@app.route('/ProductForAdmin/Update/<input>', methods=["GET","POST"])
def UpdateProduct(input):

    dataProduct = ProductData.query.get_or_404(input)

    nameFile = request.files['file']
    saveFile = secure_filename(nameFile.filename)

    
    if request.method == "POST":

        if nameFile:
            uniqueName = str(uuid.uuid1()) + "_" + saveFile
            dataProduct.file = uniqueName,
            nameFile.save(os.path.join(app.config['UPLOAD_FOLDER'], uniqueName))

        else:
            dataProduct.file = dataProduct.file

        dataProduct.type = request.values['type'],
        dataProduct.group = request.values['group'],
        dataProduct.code = request.values['code'],
        dataProduct.name = request.values['name'],
        dataProduct.price = request.values['price'],
        dataProduct.deal = request.values['deal'],

        db.session.commit()


    return redirect('/ProductForAdmin')

@app.route('/ProductForAdmin/Delete/<input>')
def DeleteProduct(input):

    dataProduct = ProductData.query.get_or_404(input)

    db.session.delete(dataProduct)
    db.session.commit()

    return redirect('/ProductForAdmin')


# =========================
#          Sample
# =========================

# @app.route('/', methods=["GET","POST"] )
# def index():
#     form = simpleForm()
#     if request.method == "POST":
#         newUser = User(
#             name = request.values['name'],
#             age = request.values['age'],
#             gender = request.values['gender'],
#             activity = request.values['activity'],
#             color = request.values['color']
#         )
#         db.session.add(newUser)
#         db.session.commit()

#         return redirect('/get')

#     pizza = ["cheese", "pepparoni", "ham", 10]
#     return render_template("index.html", pizza=pizza, form=form)

# @app.route('/get', methods=["GET","POST"] )
# def get():

#     dataUser = User.query.filter(User.id).all()
#     print(dataUser)

#     return render_template("get.html", dataUser=dataUser)

# @app.route('/update/<input>', methods=["GET","POST"] )
# def update(input):
#     form = simpleForm()
#     dataUser = User.query.get_or_404(input)
#     form.name.data = dataUser.name
#     form.age.data = dataUser.age
#     form.gender.data = dataUser.gender
#     form.activity.data = dataUser.activity
#     form.color.data = dataUser.color

#     if request.method == "POST":
#         dataUser.name = request.values['name']
#         dataUser.age = request.values['age']
#         dataUser.gender = request.values['gender']
#         dataUser.activity = request.values['activity']
#         dataUser.color = request.values['color']

#         db.session.commit()

#         return redirect('/update/'+ str(dataUser.id))

#     return render_template("update.html", dataUser=dataUser, form=form)

# @app.route('/delete/<input>', methods=["GET","POST"] )
# def delete(input):

#     dataUser = User.query.get_or_404(input)

#     db.session.delete(dataUser)
#     db.session.commit()

#     return redirect('/get')

# ====================================
#               Database
# ====================================

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    encrypt_password = db.Column(db.String(128))
    accept = db.Column(db.String(8))
    file = db.Column(db.String(100))
    date_log = db.Column(db.DateTime, default=datetime.now())

    @property
    def password(self):
        raise AttributeError('password is not readable attribute.')

    @password.setter
    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    # Create return data
    def __repr__(self):
        return '<User %r>' % self.email

class ProductData(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    type = db.Column(db.String(2))
    group = db.Column(db.String(2))
    code = db.Column(db.String(20))
    name = db.Column(db.String(50))
    price = db.Column(db.String(10))
    deal = db.Column(db.String(50))
    file = db.Column(db.String(100))

    order = db.relationship('OrderConfirm', backref='product', lazy=True)

    date_log = db.Column(db.DateTime, default=datetime.now())

    # Create return data
    def __repr__(self):
        return '<User %r>' % self.id

class OrderList(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    code = db.Column(db.String(20))
    client = db.Column(db.String(50))
    amount = db.Column(db.String(40))
    date_log = db.Column(db.DateTime, default=datetime.now())

    # Create return data
    def __repr__(self):
        return '<User %r>' % self.client

class OrderConfirm(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    item = db.Column(db.Integer, db.ForeignKey('product_data.id'))
    owner = db.Column(db.Integer, db.ForeignKey('address.id'))
    amount = db.Column(db.String(40))
    date_log = db.Column(db.DateTime, default=datetime.now())

    # Create return data
    def __repr__(self):
        return '<User %r>' % self.id

class PaymentInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    date = db.Column(db.Date())
    time = db.Column(db.Time())
    select_choices = db.Column(db.String(50))
    cost = db.Column(db.String(20))
    file = db.Column(db.String(200))
    serial = db.Column(db.String(10))
    description = db.Column(db.String(500))
    name = db.Column(db.String(200))
    email = db.Column(db.String(50))
    telephone = db.Column(db.String(20))
    date_log = db.Column(db.DateTime, default=datetime.now())

    # Create return data
    def __repr__(self):
        return '<User %r>' % self.client

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(50))
    address = db.Column(db.String(300))
    province = db.Column(db.String(40))
    district = db.Column(db.String(40))
    subDistrict = db.Column(db.String(40))
    telephone = db.Column(db.String(20))
    postCode = db.Column(db.String(5))
    destination = db.Column(db.String(10))

    taxName = db.Column(db.String(100))
    taxPayer = db.Column(db.String(20))
    taxAddress = db.Column(db.String(300))

    order = db.relationship('OrderConfirm', backref='locate', lazy=True)

    date_log = db.Column(db.DateTime, default=datetime.now())

    # Create return data
    def __repr__(self):
        return '<User %r>' % self.id


if __name__ == "__main__":
    app.run()