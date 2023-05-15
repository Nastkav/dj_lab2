import tkinter as tk
from tkinter import messagebox
import pymongo
from bson import ObjectId


def create_flight():
    # Отримати значення полів введення
    name = flight_name_entry.get()
    ship = flight_ship_entry.get()
    departure = flight_departure_entry.get()
    destination = flight_destination_entry.get()

    # Встановлення з'єднання з MongoDB Compass
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["ship_company"]
    collection_flights = database["flights"]

    # Створити новий запис про рейс
    flight_data = {
        "name": name,
        "ship": ship,
        "departure": departure,
        "destination": destination
    }
    flight_id = collection_flights.insert_one(flight_data).inserted_id

    # Повідомлення про успішне додавання рейсу
    messagebox.showinfo("Успіх", f"Рейс з ID {flight_id} успішно додано!")

def create_ticket():
    # Отримати значення полів введення
    flight_id = ticket_flight_id_entry.get()
    passenger_name = ticket_passenger_name_entry.get()
    ticket_price = float(ticket_price_entry.get())

    # Встановлення з'єднання з MongoDB Compass
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["ship_company"]
    collection_tickets = database["tickets"]

    # Створити новий запис про квиток
    ticket_data = {
        "flight_id": flight_id,
        "passenger_name": passenger_name,
        "ticket_price": ticket_price
    }
    ticket_id = collection_tickets.insert_one(ticket_data).inserted_id

    # Повідомлення про успішне додавання квитка
    messagebox.showinfo("Успіх", f"Квиток з ID {ticket_id} успішно додано!")

# Створення головного вікна
window = tk.Tk()
window.title("Довідкова інформаційна система")

flight_frame = tk.Frame(window)
flight_frame.pack(side="left", anchor="nw", padx=250)

# Елементи для додавання рейсу
flight_label = tk.Label(flight_frame, text="Додати рейс:")
flight_label.pack()

flight_name_label = tk.Label(flight_frame, text="Назва:")
flight_name_label.pack()
flight_name_entry = tk.Entry(flight_frame)
flight_name_entry.pack()

flight_ship_label = tk.Label(flight_frame, text="Корабель:")
flight_ship_label.pack()
flight_ship_entry = tk.Entry(flight_frame)
flight_ship_entry.pack()

flight_departure_label = tk.Label(flight_frame, text="Відправлення:")
flight_departure_label.pack()
flight_departure_entry = tk.Entry(flight_frame)
flight_departure_entry.pack()

flight_destination_label = tk.Label(flight_frame, text="Прибуття:")
flight_destination_label.pack()
flight_destination_entry = tk.Entry(flight_frame)
flight_destination_entry.pack()

# Кнопка для додавання рейсу
flight_button = tk.Button(flight_frame, text="Додати рейс", command=create_flight)
flight_button.pack()

separator = tk.Frame(flight_frame, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, pady=5)


ticket_frame = tk.Frame(window)
ticket_frame.pack(side="right", anchor="ne", padx=250)
# Елементи для додавання квитка

ticket_label = tk.Label(ticket_frame, text="Додати квиток:")
ticket_label.pack()

ticket_flight_id_label = tk.Label(ticket_frame, text="ID рейсу:")
ticket_flight_id_label.pack()
ticket_flight_id_entry = tk.Entry(ticket_frame)
ticket_flight_id_entry.pack()

ticket_passenger_name_label = tk.Label(ticket_frame, text="Ім'я пасажира:")
ticket_passenger_name_label.pack()
ticket_passenger_name_entry = tk.Entry(ticket_frame)
ticket_passenger_name_entry.pack()

ticket_price_label = tk.Label(ticket_frame, text="Ціна квитка:")
ticket_price_label.pack()
ticket_price_entry = tk.Entry(ticket_frame)
ticket_price_entry.pack()

# Кнопка для додавання квитка
ticket_button = tk.Button(ticket_frame, text="Додати квиток", command=create_ticket)
ticket_button.pack()

separator = tk.Frame(ticket_frame, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, pady=5)


# Роздільник
separator_frame = tk.Frame(window, width=2, bg='grey')
separator_frame.pack(side="left", fill="y", padx=5, pady=5)

def read_flights():
    # Встановлення з'єднання з MongoDB Compass
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["ship_company"]
    collection_flights = database["flights"]

    # Отримання списку всіх рейсів
    flights = []
    for flight in collection_flights.find():
        flight_info = (flight["_id"], flight["ship"], flight["name"], flight["departure"], flight["destination"])
        flights.append(flight_info)

    return flights


def read_tickets():
    # Встановлення з'єднання з MongoDB Compass
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["ship_company"]
    collection_tickets = database["tickets"]

    # Отримання списку всіх квитків
    tickets = []
    for ticket in collection_tickets.find():
        ticket_info = (ticket["_id"], ticket["ship"], ticket["name"], ticket["departure"], ticket["destination"])
        tickets.append(ticket_info)

    return tickets



def show_flights():
    flights = read_flights()
    flights_text = "\n".join([f" ID: {flight[0]}, {flight[1]} {flight[2]}: {flight[3]} - {flight[4]}" for flight in flights])
    flights_window = tk.Toplevel(window)
    flights_window.title("Список рейсів")
    flights_textbox = tk.Text(flights_window, height=10, width=50)
    flights_textbox.insert(tk.END, flights_text)
    flights_textbox.pack()


def show_tickets():
    tickets = read_tickets()
    tickets_text = "\n".join([f" ID: {ticket[0]}, {ticket[1]} {ticket[2]} {ticket[3]}" for ticket in tickets])
    tickets_window = tk.Toplevel(window)
    tickets_window.title("Список білетів")
    tickets_textbox = tk.Text(tickets_window, height=10, width=50)
    tickets_textbox.insert(tk.END, tickets_text)
    tickets_textbox.pack()

def update_flight():
    # Отримати значення полів введення
    flight_id = flight_id_entry.get()
    name = flight_uname_entry.get()
    ship = flight_uship_entry.get()
    departure = flight_udeparture_entry.get()
    destination = flight_udestination_entry.get()

    # Встановлення з'єднання з MongoDB Compass
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["ship_company"]
    collection_flights = database["flights"]

    # Оновити запис про рейс
    collection_flights.update_one({"_id": ObjectId(flight_id)}, {"$set": {
        "name": name,
        "ship": ship,
        "departure": departure,
        "destination": destination
    }})

    # Повідомлення про успішне оновлення рейсу
    messagebox.showinfo("Успіх", f"Рейс з ID {flight_id} успішно оновлено!")

def delete_flight():
    # Отримати значення полів введення
    flight_id = flight_did_entry.get()

    # Встановлення з'єднання з MongoDB Compass
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["ship_company"]
    collection_flights = database["flights"]

    # Видалити запис про рейс
    result = collection_flights.delete_one({"_id": ObjectId(flight_id)})

    # Повідомлення про успішне видалення рейсу
    if result.deleted_count > 0:
        messagebox.showinfo("Успіх", f"Рейс з ID {flight_id} успішно видалено!")
    else:
        messagebox.showwarning("Помилка", f"Рейс з ID {flight_id} не знайдено!")

def delete_ticket():
    # Отримати значення полів введення
    ticket_id = ticket_did_entry.get()

    # Встановлення з'єднання з MongoDB Compass
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    database = client["ship_company"]
    collection_tickets = database["tickets"]

    # Видалити запис про рейс
    result = collection_tickets.delete_one({"_id": ObjectId(ticket_id)})

    # Повідомлення про успішне видалення рейсу
    if result.deleted_count > 0:
        messagebox.showinfo("Успіх", f"Рейс з ID {ticket_id} успішно видалено!")
    else:
        messagebox.showwarning("Помилка", f"Рейс з ID {ticket_id} не знайдено!")

# Кнопки для виведення списку рейсів та квитків
show_flights_button = tk.Button(flight_frame, text="Список рейсів", command=show_flights)
show_flights_button.pack(pady=5)

show_tickets_button = tk.Button(ticket_frame, text="Список квитків", command=show_tickets)
show_tickets_button.pack(pady=5)

# Реалізація редагування
separator = tk.Frame(flight_frame, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, pady=5)

flight_id_label = tk.Label(flight_frame, text="ID рейсу:")
flight_id_label.pack()
flight_id_entry = tk.Entry(flight_frame)
flight_id_entry.pack()

flight_uname_label = tk.Label(flight_frame, text="Назва:")
flight_uname_label.pack()
flight_uname_entry = tk.Entry(flight_frame)
flight_uname_entry.pack()

flight_uship_label = tk.Label(flight_frame, text="Корабель:")
flight_uship_label.pack()
flight_uship_entry = tk.Entry(flight_frame)
flight_uship_entry.pack()

flight_udeparture_label = tk.Label(flight_frame, text="Відправлення:")
flight_udeparture_label.pack()
flight_udeparture_entry = tk.Entry(flight_frame)
flight_udeparture_entry.pack()

flight_udestination_label = tk.Label(flight_frame, text="Прибуття:")
flight_udestination_label.pack()
flight_udestination_entry = tk.Entry(flight_frame)
flight_udestination_entry.pack()

update_flight_button = tk.Button(flight_frame, text="Редагувати рейс", command=update_flight)
update_flight_button.pack()

separator = tk.Frame(ticket_frame, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, pady=5)

ticket_uflight_id_label = tk.Label(ticket_frame, text="ID рейсу:")
ticket_uflight_id_label.pack()
ticket_uflight_id_entry = tk.Entry(ticket_frame)
ticket_uflight_id_entry.pack()

ticket_upassenger_name_label = tk.Label(ticket_frame, text="Ім'я пасажира:")
ticket_upassenger_name_label.pack()
ticket_upassenger_name_entry = tk.Entry(ticket_frame)
ticket_upassenger_name_entry.pack()

ticket_uprice_label = tk.Label(ticket_frame, text="Ціна квитка:")
ticket_uprice_label.pack()
ticket_uprice_entry = tk.Entry(ticket_frame)
ticket_uprice_entry.pack()

update_uticket_button = tk.Button(ticket_frame, text="Редагувати білет", command=update_flight)
update_uticket_button.pack()


# Реалізація видалення
separator = tk.Frame(flight_frame, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, pady=5)

flight_did_label = tk.Label(flight_frame, text="ID рейсу:")
flight_did_label.pack()
flight_did_entry = tk.Entry(flight_frame)
flight_did_entry.pack()

delete_flight_button = tk.Button(flight_frame, text="Видалити рейс", command=delete_flight)
delete_flight_button.pack()

separator = tk.Frame(ticket_frame, height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, pady=5)

ticket_did_label = tk.Label(ticket_frame, text="ID рейсу:")
ticket_did_label.pack()
ticket_did_entry = tk.Entry(ticket_frame)
ticket_did_entry.pack()

delete_ticket_button = tk.Button(ticket_frame, text="Видалити білет", command=delete_ticket)
delete_ticket_button.pack()

# Запуск головного циклу програми
window.mainloop()


