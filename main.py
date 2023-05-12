import tkinter as tk
from tkinter import messagebox
import pymongo

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

# Елементи для додавання рейсу
flight_label = tk.Label(window, text="Додати рейс:")
flight_label.pack()

flight_name_label = tk.Label(window, text="Назва:")
flight_name_label.pack()
flight_name_entry = tk.Entry(window)
flight_name_entry.pack()

flight_ship_label = tk.Label(window, text="Корабель:")
flight_ship_label.pack()
flight_ship_entry = tk.Entry(window)
flight_ship_entry.pack()

flight_departure_label = tk.Label(window, text="Відправлення:")
flight_departure_label.pack()
flight_departure_entry = tk.Entry(window)
flight_departure_entry.pack()

flight_destination_label = tk.Label(window, text="Прибуття:")
flight_destination_label.pack()
flight_destination_entry = tk.Entry(window)
flight_destination_entry.pack()

# Кнопка для додавання рейсу
flight_button = tk.Button(window, text="Додати рейс", command=create_flight)
flight_button.pack()

# Роздільник між рейсами та квитками
separator = tk.Frame(height=2, bd=1, relief=tk.SUNKEN)
separator.pack(fill=tk.X, padx=5, pady=5)

# Елементи для додавання квитка
ticket_label = tk.Label(window, text="Додати квиток:")
ticket_label.pack()

ticket_flight_id_label = tk.Label(window, text="ID рейсу:")
ticket_flight_id_label.pack()
ticket_flight_id_entry = tk.Entry(window)
ticket_flight_id_entry.pack()

ticket_passenger_name_label = tk.Label(window, text="Ім'я пасажира:")
ticket_passenger_name_label.pack()
ticket_passenger_name_entry = tk.Entry(window)
ticket_passenger_name_entry.pack()

ticket_price_label = tk.Label(window, text="Ціна квитка:")
ticket_price_label.pack()
ticket_price_entry = tk.Entry(window)
ticket_price_entry.pack()

# Кнопка для додавання квитка
ticket_button = tk.Button(window, text="Додати квиток", command=create_ticket)
ticket_button.pack()

# Запуск головного циклу програми
window.mainloop()
