from flask import Flask, request

app = Flask(__name__)
@app.route('/k/<k>')

def hurdleRace(k):

    height1 = request.get_json()
    arr = height1["data"]

    maxi = max(arr)
    hasil = 0

    if (maxi-int(k)) < 0 :
        return "0"
    else :
        hasil = maxi - int(k)
        return {
                "min_doses " : hasil
                }   

# print(hurdleRace(4,[1,6,3,5,2]))
