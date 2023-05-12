import pymongo

try:
    # Встановлюємо з'єднання з MongoDB Compass
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Перевірка наявності з'єднання
    client.admin.command('ismaster')
    print("З'єднання з MongoDB Compass встановлено")

    # Вибір або створення бази даних
    database = client["ship_company"]
    collection_flights = database["flights"]
    collection_tickets = database["tickets"]

    # Приклад додавання запису в колекцію "Рейси"
    flight_data = {
        "name": "Flight 1",
        "ship": "Ship 1",
        "departure": "City A",
        "destination": "City B"
    }
    flight_id = collection_flights.insert_one(flight_data).inserted_id
    print("Доданий рейс з ID:", flight_id)

    # Приклад додавання запису в колекцію "Квитки"
    ticket_data = {
        "flight_id": flight_id,
        "passenger_name": "John Doe",
        "ticket_price": 100.0
    }
    ticket_id = collection_tickets.insert_one(ticket_data).inserted_id
    print("Доданий квиток з ID:", ticket_id)

except pymongo.errors.ConnectionFailure:
    print("Помилка підключення до MongoDB Compass")