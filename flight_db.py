import psycopg2
import environ

env = environ.Env()
environ.Env.read_env()

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    user='postgres',
    password=env('DBPASS'),
    database=env('DATABASE')
)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the flights table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS flights
             (id SERIAL PRIMARY KEY,
             flight_number TEXT NOT NULL,
             origin TEXT,
             destination TEXT,
             departure_time TIMESTAMP,
             arrival_time TIMESTAMP,
             capacity INTEGER,
             available_seats INTEGER)''')

# Insert sample flight details into the flights table
flights_data = [
    ("F123", "New York", "Los Angeles", '2023-08-10 10:00:00', '2023-08-10 14:00:00', 200, 150),
    ("F234", "Chicago", "Miami", '2023-08-12 08:30:00', '2023-08-12 12:30:00', 180, 120),
    ("F345", "Houston", "Denver", '2023-08-14 14:15:00', '2023-08-14 16:30:00', 220, 180),
    ("F456", "San Francisco", "Seattle", '2023-08-16 11:45:00', '2023-08-16 13:30:00', 190, 160),
    ("F567", "Boston", "Washington, D.C.", '2023-08-18 09:00:00', '2023-08-18 11:15:00', 210, 190),
    ("F678", "Dallas", "Phoenix", '2023-08-20 15:30:00', '2023-08-20 18:00:00', 240, 200)
]

for flight in flights_data:
    cursor.execute("INSERT INTO flights (flight_number, origin, destination, departure_time, arrival_time, capacity, "
                   "available_seats) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (flight[0], flight[1], flight[2], flight[3], flight[4], flight[5], flight[6]))

# Commit the changes and close the connection
conn.commit()
conn.close()
