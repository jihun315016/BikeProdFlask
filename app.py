from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():    
    return "Hello World"

@app.route('/saveImg', methods=['GET', 'POST']) 
def saveImg(): 
    if request.is_json:
        data = request.get_json()
        img = str(data["img"])
        file = str(data["fileName"])

        f = open(f"static/{file}.txt", 'w')
        f.write(img)
        f.close()

        return request.url
    else:
        return "저장에 실패했습니다."
        

@app.route('/getImg', methods=['GET', 'POST']) 
def getImg(): 
    if request.is_json:
        data = request.get_json()
        file = str(data["fileName"])

        f = open(f"static/{file}.txt", 'r')
        data = f.read()
        f.close()

        return data
    else:
        return "이미지 조회에 실패했습니다."


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0')
