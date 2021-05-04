import objects
from xhtml2pdf import pisa
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

medicines = []
doctors = []
nurserys = []
patients = []
admins = []
citas = []
facturas =[]


# type user 1 Patient , Type user 2 Nursery , Typeuser 3 Doctor , TypeUser 4 Admin


@app.route("/reports/medicine")
def medicines_report():
    html = '<!DOCTYPE html>'
    html += '<html lang="en">'
    html += '<head>'
    html += "<title>Medicines</title>"
    html += "</head>"
    html += "<body>"
    html += '<table style="width:100%; border: 1px solid black; margin: 5px">'
    html += '<tr><th>Name</th><th>Description</th><th>Quantity</th><th>Price</th></tr>'
    for medicine in medicines:
        html += "<tr>"
        html += "<td>" + medicine.name + "</td>"
        html += "<td>" + medicine.description + "</td>"
        html += "<td>" + str(medicine.quantity) + "</td>"
        html += "<td>" + str(medicine.price) + "</td>"
        html += "</tr>"
    html += "</table>"
    html += "</body>"
    html += '</html >'
    result_file = open("./static/medicines.pdf", "w+b")
    pisa_status = pisa.CreatePDF(html, dest=result_file)
    result_file.close()
    return app.send_static_file("medicines.pdf")


@app.route("/reports/factura")
def factura_report():
    html = '<!DOCTYPE html>'
    html += '<html lang="en">'
    html += '<head>'
    html += "<title>Factura</title>"
    html += "</head>"
    html += "<body>"
    html += '<table style="width:100%; border: 1px solid black; margin: 5px">'
    html += '<tr><th>Fecha</th><th>Nombre Paciente</th><th>Nombre Doctor</th><th>Precio consulta</th><th>Costo Operacion</th><th>Costo Internado</th><th>Total</th></tr>'
    for factura in facturas:
        html += "<tr>"
        html += "<td>" + factura.date + "</td>"
        html += "<td>" + factura.patient_name + "</td>"
        html += "<td>" + factura.doctor_name + "</td>"
        html += "<td>" + factura.precio_consulta + "</td>"
        html += "<td>" + factura.precio_operacion + "</td>"
        html += "<td>" + factura.precio_internado + "</td>"
        html += "<td>" + factura.total + "</td>"
        html += "</tr>"
    html += "</table>"
    html += "</body>"
    html += '</html >'
    result_file = open("./static/factura.pdf", "w+b")
    pisa_status = pisa.CreatePDF(html, dest=result_file)
    result_file.close()
    return app.send_static_file("factura.pdf")


@app.route("/reports/patient")
def patients_report():
    html = '<!DOCTYPE html>'
    html += '<html lang="en">'
    html += '<head>'
    html += "<title>Pacientes</title>"
    html += "</head>"
    html += "<body>"
    html += '<table style="width:100%; border: 1px solid black; margin: 5px">'
    html += '<tr><th>First Name</th><th>Last Name</th><th>Date of Birth</th><th>Gender</th><th>Nickname</th><th>Password</th><th>Phone</th></tr>'
    for patient in patients:
        html += "<tr>"
        html += "<td>" + patient.first_name + "</td>"
        html += "<td>" + patient.last_name + "</td>"
        html += "<td>" + patient.date + "</td>"
        html += "<td>" + patient.gender + "</td>"
        html += "<td>" + patient.nickname + "</td>"
        html += "<td>" + patient.password + "</td>"
        html += "<td>" + patient.phone + "</td>"
        html += "</tr>"
    html += "</table>"
    html += "</body>"
    html += '</html >'
    result_file = open("./static/patients.pdf", "w+b")
    pisa_status = pisa.CreatePDF(html, dest=result_file)
    result_file.close()
    return app.send_static_file("patients.pdf")


@app.route("/reports/nursery")
def nurserys_report():
    html = '<!DOCTYPE html>'
    html += '<html lang="en">'
    html += '<head>'
    html += "<title>Enfermeras</title>"
    html += "</head>"
    html += "<body>"
    html += '<table style="width:100%; border: 1px solid black; margin: 5px">'
    html += '<tr><th>First Name</th><th>Last Name</th><th>Date of Birth</th><th>Gender</th><th>Nickname</th><th>Password</th><th>Phone</th></tr>'
    for nursery in nurserys:
        html += "<tr>"
        html += "<td>" + nursery.first_name + "</td>"
        html += "<td>" + nursery.last_name + "</td>"
        html += "<td>" + nursery.date + "</td>"
        html += "<td>" + nursery.gender + "</td>"
        html += "<td>" + nursery.nickname + "</td>"
        html += "<td>" + nursery.password + "</td>"
        html += "<td>" + nursery.phone + "</td>"
        html += "</tr>"
    html += "</table>"
    html += "</body>"
    html += '</html >'
    result_file = open("./static/nurserys.pdf", "w+b")
    pisa_status = pisa.CreatePDF(html, dest=result_file)
    result_file.close()
    return app.send_static_file("nurserys.pdf")


@app.route("/reports/doctor")
def doctors_report():
    html = '<!DOCTYPE html>'
    html += '<html lang="en">'
    html += '<head>'
    html += "<title>Doctores</title>"
    html += "</head>"
    html += "<body>"
    html += '<table style="width:100%; border: 1px solid black; margin: 5px">'
    html += '<tr><th>First Name</th><th>Last Name</th><th>Date of Birth</th><th>Gender</th><th>Nickname</th><th>Password</th><th>Specialty</th><th>Phone</th></tr>'
    for doctor in doctors:
        html += "<tr>"
        html += "<td>" + doctor.first_name + "</td>"
        html += "<td>" + doctor.last_name + "</td>"
        html += "<td>" + doctor.date + "</td>"
        html += "<td>" + doctor.gender + "</td>"
        html += "<td>" + doctor.nickname + "</td>"
        html += "<td>" + doctor.password + "</td>"
        html += "<td>" + doctor.specialty + "</td>"        
        html += "<td>" + doctor.phone + "</td>"
        html += "</tr>"
    html += "</table>"
    html += "</body>"
    html += '</html >'
    result_file = open("./static/doctors.pdf", "w+b")
    pisa_status = pisa.CreatePDF(html, dest=result_file)
    result_file.close()
    return app.send_static_file("doctors.pdf")


@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    first_name = data["first_name"]
    last_name = data["last_name"]
    date = data["date"]
    gender = data["gender"]
    nickname = data["nickname"]
    password = data["password"]
    phone = data["phone"]
    typeUser = 1
    valid_patient = True

    for patient in patients:
        if patient.nickname == nickname:
            valid_patient = False
    if valid_patient:
        patients.append(objects.Patient(first_name, last_name,
                                  date, gender, nickname, password, phone, typeUser))
        return jsonify(request.get_json()), 200
    else:
        return jsonify({"message": "Nickname Repetido"}),400


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    nickname = data["nickname"]
    password = data["password"]
    for patient in patients:
        if patient.nickname == nickname:
            if patient.password == password:
                return jsonify({
                    "first_name": patient.first_name,
                    "last_name": patient.last_name,
                    "date": patient.date,
                    "gender": patient.gender,
                    "nickname": patient.nickname,
                    "password": patient.password,
                    "phone": patient.password,
                    "typeUser": patient.typeUser
                    }), 200
            else:
                return jsonify({"message": "bad credentials"}), 400
    for nursery in nurserys:
        if nursery.nickname == nickname:
            if nursery.password == password:
                return jsonify({
                    "first_name": nursery.first_name,
                    "last_name": nursery.last_name,
                    "date": nursery.date,
                    "gender": nursery.gender,
                    "nickname": nursery.nickname,
                    "password": nursery.password,
                    "phone": nursery.password,
                    "typeUser": nursery.typeUser
                    }), 200
            else:
                return jsonify({"message": "bad credentials"}), 400
    for doctor in doctors:
        if doctor.nickname == nickname:
            if doctor.password == password:
                return jsonify({
                    "first_name": doctor.first_name,
                    "last_name": doctor.last_name,
                    "date": doctor.date,
                    "gender": doctor.gender,
                    "nickname": doctor.nickname,
                    "password": doctor.password,
                    "specialty": doctor.specialty,
                    "phone": doctor.password,
                    "typeUser": doctor.typeUser
                    }), 200
            else:
                return jsonify({"message": "bad credentials"}), 400

    if nickname == "admin":
        if password == "1234":
            return jsonify({
                    "first_name":"Guillermo",
                    "last_name":"Peitzner",
                    "date":"01/12/1996",
                    "gender":"m",
                    "nickname":"admin",
                    "password":"1234",
                    "phone": "24102030",
                    "typeUser": 4
                    }), 200
        else:
            return jsonify({"message": "bad credentials"}), 400


@app.route("/medicine", methods=["GET", "POST", "PUT", "DELETE"])
def medicine():
    if request.method == "GET":
        tmp = []
        for medicine in medicines:
            tmp.append({"name": medicine.name, "price": medicine.price,
                       "description": medicine.description, "quantity": medicine.quantity})
        return jsonify(tmp), 200
    elif request.method == "POST":
        data = request.get_json()
        name = data["name"]
        price = data["price"]
        description = data["description"]
        quantity = data["quantity"]
        valid_medicine = True
        for medicine in medicines:
            if medicine.name == name:
                valid_medicine = False
        if valid_medicine:
            medicines.append(objects.Medicine(name, price, description, quantity))
            return jsonify(request.get_json()), 200
        else:
            return jsonify({"message": "medicine Repeated"}),400
    elif request.method == "PUT":
        data = request.get_json()
        name = data["name"]
        price = data["price"]
        description = data["description"]
        quantity = data["quantity"]
        for medicine in medicines:
            if medicine.name == name:
                medicine.price = price
                medicine.description = description
                medicine.price = price
        return jsonify({"message": "medicine edited"}), 200
    elif request.method == "DELETE":
        name = request.args.get("name")
        for medicine in medicines:
            if medicine.name == name:
                medicines.remove(medicine)
        return jsonify({"message": "Medicina"}), 200


@app.route("/doctor", methods=["GET", "POST", "PUT", "DELETE"])
def doctor():
    if request.method == "GET":
        tmp = []
        for doctor in doctors:
            tmp.append({"first_name": doctor.first_name, "last_name": doctor.last_name,
                       "date": doctor.date, "gender": doctor.gender,
                       "nickname": doctor.nickname, "password": doctor.password,
                       "specialty": doctor.specialty, "phone": doctor.phone,
                       "typeUser": doctor.typeUser})
        return jsonify(tmp), 200
    elif request.method == "POST":
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        date = data["date"]
        gender = data["gender"]
        nickname = data["nickname"]
        password = data["password"]
        specialty = data["specialty"]
        phone = data["phone"]   
        typeUser = data["typeUser"]                 
        valid_doctor = True
        for doctor in doctors:
            if doctor.nickname == nickname:
                valid_doctor = False
        if valid_doctor:
            doctors.append(objects.Doctor(first_name, last_name, date, gender, nickname, password, specialty, phone, typeUser))
            return jsonify(request.get_json()), 200
        else:
            return jsonify({"message": "Doctor Repeated"}),400
    elif request.method == "PUT":
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        date = data["date"]
        gender = data["gender"]
        nickname = data["nickname"]
        password = data["password"]
        specialty = data["specialty"]
        phone = data["phone"]    
        typeUser = data["typeUser"]      
        for doctor in doctors:
            if doctor.nickname == nickname:
                doctor.first_name = first_name
                doctor.last_name = last_name
                doctor.date = date
                doctor.gender = gender
                doctor.password = password
                doctor.specialty = specialty
                doctor.phone = phone
                doctor.typeUser = typeUser
        return jsonify({"message": "Doctor edited"}), 200
    elif request.method == "DELETE":
        nickname = request.args.get("nickname")
        for doctor in doctors:
            if doctor.nickname == nickname:
                doctors.remove(doctor)
        return jsonify({"message": "Doctor Eliminado"}), 200


@app.route("/nursery", methods=["GET", "POST", "PUT", "DELETE"])
def nursery():
    if request.method == "GET":
        tmp = []
        for nursery in nurserys:
            tmp.append({"first_name": nursery.first_name, "last_name": nursery.last_name,
                       "date": nursery.date, "gender": nursery.gender,
                       "nickname": nursery.nickname, "password": nursery.password,
                       "phone": nursery.phone, "typeUser": nursery.typeUser})
        return jsonify(tmp), 200
    elif request.method == "POST":
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        date = data["date"]
        gender = data["gender"]
        nickname = data["nickname"]
        password = data["password"]
        phone = data["phone"]
        typeUser = data["typeUser"]                
        valid_nursery = True
        for nursery in nurserys:
            if nursery.nickname == nickname:
                valid_nursery = False
        if valid_nursery:
            nurserys.append(objects.Nursery(first_name, last_name, date, gender, nickname, password, phone, typeUser))
            return jsonify(request.get_json()), 200
        else:
            return jsonify({"message": "Nursery Repeated"}),400
    elif request.method == "PUT":
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        date = data["date"]
        gender = data["gender"]
        nickname = data["nickname"]
        password = data["password"]
        phone = data["phone"]      
        typeUser = data["typeUser"]                
        for nursery in nurserys:
            if nursery.nickname == nickname:
                nursery.first_name = first_name
                nursery.last_name = last_name
                nursery.date = date
                nursery.gender = gender
                nursery.password = password
                nursery.phone = phone
                nursery.typeUser = typeUser
        return jsonify({"message": "Nursery edited"}), 200
    elif request.method == "DELETE":
        nickname = request.args.get("nickname")
        for nursery in nurserys:
            if nursery.nickname == nickname:
                nurserys.remove(nursery)
        return jsonify({"message": "Nursery Eliminada"}), 200



@app.route("/patient", methods=["GET", "POST", "PUT", "DELETE"])
def patient():
    if request.method == "GET":
        tmp = []
        for patient in patients:
            tmp.append({"first_name": patient.first_name, "last_name": patient.last_name,
                       "date": patient.date, "gender": patient.gender,
                       "nickname": patient.nickname, "password": patient.password,
                       "phone": patient.phone, "typeUser": patient.typeUser})
        return jsonify(tmp), 200
    elif request.method == "POST":
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        date = data["date"]
        gender = data["gender"]
        nickname = data["nickname"]
        password = data["password"]
        phone = data["phone"]   
        typeUser = data["typeUser"]            
        valid_patient = True
        for patient in patients:
            if patient.nickname == nickname:
                valid_patient = False
        if valid_patient:
            patients.append(objects.Patient(first_name, last_name, date, gender, nickname, password, phone,typeUser))
            return jsonify(request.get_json()), 200
        else:
            return jsonify({"message": "Patient Repeated"}),400
    elif request.method == "PUT":
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        date = data["date"]
        gender = data["gender"]
        nickname = data["nickname"]
        password = data["password"]
        phone = data["phone"] 
        typeUser = data["typeUser"]      
        for patient in patients:
            if patient.nickname == nickname:
                patient.first_name = first_name
                patient.last_name = last_name
                patient.date = date
                patient.gender = gender
                patient.password = password
                patient.phone = phone
                patient.typeUser = typeUser
                
        return jsonify({"message": "Patient edited"}), 200
    elif request.method == "DELETE":
        nickname = request.args.get("nickname")
        for patient in patients:
            if patient.nickname == nickname:
                patients.remove(patient)
        return jsonify({"message": "Patient Eliminada"}), 200



@app.route("/cita", methods=["GET", "POST", "PUT", "DELETE"])
def cita():
    if request.method == "GET":
        tmp = []
        for cita in citas:
            tmp.append({"patient_nickname": cita.patient_nickname, "time": cita.time,
                       "date": cita.date, "motivo": cita.motivo,
                       "estado": cita.estado, "doctor_name": cita.doctor_name})
        return jsonify(tmp), 200
    elif request.method == "POST":
        data = request.get_json()
        patient_nickname = data["patient_nickname"]
        time = data["time"]
        date = data["date"]
        motivo = data["motivo"]
        estado = data["estado"]
        doctor_name = data["doctor_name"]          
        valid_cita = True
        for cita in citas:
            if cita.estado == "Pendiente" or cita.estado == "Aceptada":
                if cita.patient_nickname == patient_nickname:
                    valid_cita = False
        if valid_cita:
            citas.append(objects.Cita(patient_nickname, time, date, motivo, estado, doctor_name))
            return jsonify(request.get_json()), 200
        else:
            return jsonify({"message": "Cita Repeated"}),400
    elif request.method == "PUT":
        data = request.get_json()
        patient_nickname = data["patient_nickname"]
        time = data["time"]
        date = data["date"]
        motivo = data["motivo"]
        estado = data["estado"]
        doctor_name = data["doctor_name"]       
        for cita in citas:
            if cita.patient_nickname == patient_nickname:
                cita.time = time
                cita.date = date
                cita.motivo = motivo
                cita.estado = estado
                cita.doctor_name = doctor_name                
        return jsonify({"message": "Cita Editada"}), 200
    elif request.method == "DELETE":
        patient_nickname = request.args.get("patient_nickname")
        for cita in citas:
            if cita.patient_nickname == patient_nickname:
                citas.remove(cita)
        return jsonify({"message": "Cita Eliminada"}), 200



@app.route("/factura", methods=["GET", "POST"])
def factura():
    if request.method == "GET":
        tmp = []
        for factura  in facturas:
            tmp.append({"date": factura.date, "patient_name": factura.patient_name,
                       "doctor_name": factura.doctor_name, "precio_consulta": factura.precio_consulta,
                       "precio_operacion": factura.precio_operacion, "precio_internado": factura.precio_internado, "total": factura.total})
        return jsonify(tmp), 200
    elif request.method == "POST":
        data = request.get_json()
        date = data["date"]
        patient_name = data["patient_name"]
        doctor_name = data["doctor_name"]
        precio_consulta = data["precio_consulta"]
        precio_operacion = data["precio_operacion"]
        precio_internado = data["precio_internado"]      
        total = data["total"]             
        facturas.append(objects.Factura(date, patient_name, doctor_name, precio_consulta, precio_operacion, precio_internado, total))
        return jsonify(request.get_json()), 200