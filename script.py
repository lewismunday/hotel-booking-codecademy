import sqlite3


con = sqlite3.connect("hotel_booking.db")
cur = con.cursor()


bra = cur.execute("SELECT * FROM booking_summary WHERE country = 'BRA';")
bra = bra.fetchall()

cur.execute("""CREATE TABLE IF NOT EXISTS bra_customers (
  num INTEGER, hotel TEXT, is_cancelled INTEGER, lead_time INTEGER, arrival_date_year INTEGER, arrival_date_month TEXT, arrival_date_day_of_month INTEGER, adults INTEGER, children INTEGER, country TEXT, adr REAL, special_requests INTEGER
);
""")

cur.executemany("""INSERT INTO bra_customers VALUES (?,?,?,?,?,?,?,?,?,?,?,?);
""", bra)

lead_time_can = cur.execute("SELECT * FROM bra_customers WHERE is_cancelled = 1;").fetchall()

sum = 0
for num in lead_time_can:
  sum += num[0]

average_lead_time_can = sum / len(lead_time_can)

lead_time = cur.execute("SELECT * FROM bra_customers WHERE is_cancelled = 0;").fetchall()


lead_sum = 0

for num in lead_time:
  lead_sum += num[0]

average_lead_time = sum / len(lead_time)


special_requests_can = cur.execute("SELECT special_requests FROM bra_customers WHERE is_cancelled = 1;").fetchall()

num_of_special_requests_can = 0

for num in special_requests_can:
  num_of_special_requests_can += num[0]


special_requests = cur.execute("SELECT special_requests FROM bra_customers WHERE is_cancelled = 0;").fetchall()


num_of_special_requests = 0

for num in special_requests:
  num_of_special_requests += num[0]

con.close()
