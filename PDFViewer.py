from flask import Flask, request

app = Flask(__name__)
@app.route('/pdf-viewer')

def designerPdfViewer():
    height = request.get_json()
    arr = height["height"]
    word = request.args.get("word")
    alphabet = list(map(chr, range(97, 123)))
    dict1 = {}
    lst = []

    for i in range(len(alphabet)):
        for j in range(len(arr)):
            if i == j:
                dict1[alphabet[i]] = arr[j]

    for k in word:
        lst.append(dict1.get(k))
        o = max(lst) * len(lst) 
    
    return { "Area " : str(o) } 
    

# print(designerPdfViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5],"torn"))