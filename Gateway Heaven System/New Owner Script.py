import sqlite3

# Insert Owner

conn = sqlite3.connect('GatewayHeaven.db')
c = conn.cursor()

exe = """
        INSERT INTO owner (
        oFName, oLName, address, email, phoneNumber)
        VALUES (?, ?, ?, ?, ?);"""
                # CHANGE DATA IN QUOTATION MARKS #
c.execute(exe, ("First Name", "Last Name","Address", "email", "Phone Number"))
conn.commit()