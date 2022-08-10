import sqlite3

# Insert Property

conn = sqlite3.connect('GatewayHeaven.db')
c = conn.cursor()

exe = """
        INSERT INTO property (
        dateOwned, ownerID, planID, lot)
        VALUES (?, ?, ?, ?);"""
              #  DATE    OWNER ID   PLAN ID     LOT ID #
c.execute(exe, ("2020/11/08", "7","Bone Crypt", "Crypt Lot 6"))
conn.commit()

# Insert Property in Lot

conn = sqlite3.connect('GatewayHeaven.db')
c = conn.cursor()

exe = """
        UPDATE lot SET
        propertyID = ?
        WHERE lotID = ?;"""
              #  PROPERTY ID
c.execute(exe, (7,"Crypt Lot 6"))
conn.commit()

"""
Information:

    PLAN ID:
        - Ash Urn Burial
        - Ash Crypt
        - Bone Crypt
        - Full Body Crypt
        - Lawn Lot

    LOT ID:
        - Crypt Lot 1 - 10
        - Ash Burial 1 - 10
        - Lawn Lot 1 - 10



"""
