from flask import Flask, request

app = Flask(__name__)
@app.route('/git1')

def pickingNumbers():

    maksimum = request.get_json()
    arr = maksimum["data"]
    max1 = 0
    for item in arr:
        objek1 = arr.count(item)
        objek2 = arr.count(item + 1)
        hitung = objek1 + objek2
        for i in arr:
            if hitung > i:
                max1 = hitung
    return str(max1)
