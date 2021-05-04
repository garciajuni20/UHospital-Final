class Admin:
    def __init__(self, first_name, last_name, date, gender, nickname, password, phone ,typeUser):
        self.first_name = first_name
        self.last_name = last_name
        self.date = date
        self.gender = gender
        self.nickname = nickname
        self.password = password
        self.phone = phone
        self.typeUser = typeUser


class Medicine:
     def __init__(self, name,price,description,quantity):
         self.name = name
         self.price = price
         self.description = description
         self.quantity = quantity


class Doctor:
    def __init__(self, first_name, last_name, date, gender, nickname, password, specialty, phone, typeUser):
        self.first_name = first_name
        self.last_name = last_name
        self.date = date
        self.gender = gender
        self.nickname = nickname
        self.password = password
        self.specialty = specialty
        self.phone = phone
        self.typeUser = typeUser

        


class Nursery:
    def __init__(self, first_name, last_name, date, gender, nickname, password, phone, typeUser):
        self.first_name = first_name
        self.last_name = last_name
        self.date = date
        self.gender = gender
        self.nickname = nickname
        self.password = password
        self.phone = phone
        self.typeUser = typeUser



class Patient:
    def __init__(self, first_name, last_name, date, gender, nickname, password, phone, typeUser):
        self.first_name = first_name
        self.last_name = last_name
        self.date = date
        self.gender = gender
        self.nickname = nickname
        self.password = password
        self.phone = phone
        self.typeUser = typeUser



class Cita:
    def __init__(self, patient_nickname, time, date, motivo, estado, doctor_name):
        self.patient_nickname = patient_nickname
        self.time = time
        self.date = date
        self.motivo = motivo
        self.estado = estado
        self.doctor_name = doctor_name



class Factura:
    def __init__(self, date, patient_name, doctor_name, precio_consulta, precio_operacion, precio_internado, total, ):
        self.date = date
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.precio_consulta = precio_consulta
        self.precio_operacion = precio_operacion
        self.precio_internado = precio_internado
        self.total = total

