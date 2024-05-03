import sqlite3

DATABASE = 'something.db'


def print_all_colour():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT colour_name, hex_code FROM Colour WHERE hex_code LIKE '%FF%';"
        cursor.execute(sql)
        results = cursor.fetchall()
        # print nicely
        for colour in results:
            print(f"Colour: {colour[0]}\nHex code: {colour[1]}\n")


if __name__ == "__main__":
    print_all_colour()
