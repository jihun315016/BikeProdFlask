from flask import Flask, request, jsonify

import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)

# 예를 들어 존재하지 않는 경로에 접근하면 이슈가 기록되는 것을 확인할 수 있다.
if not app.debug:
    # 로깅 파일 설정
    file_handler = RotatingFileHandler('myFlask.log', maxBytes=2000, backupCount=10)
    
    # 어느 단계까지 로깅을 할지 선택
    # DEBUG > INFO > WARNING > ERROR > Critical
    # 아무것도 입력하지 않을 때 기본값이 WARNING
    file_handler.setLevel(logging.WARNING)

    # app.logger.addHandler()에 로거 등록
    app.logger.addHandler(file_handler)

@app.route('/')
def index():    
    return "Hello World"

@app.route('/saveImg', methods=['GET', 'POST']) 
def saveImg(): 
    if request.is_json:
        data = request.get_json()
        return str(data["test_params"])
    else:
        return jsonify("저장에 실패했습니다.")
        

@app.route('/method', methods=['GET', 'POST']) 
def method(): 
    if request.is_json:
        data = request.get_json()
        f = open(f"satic/{file}.txt", 'w')
        f.write(byte)
        f.close()
        return str(data["test_params"])
    data = 1
    return jsonify(data)
    

if __name__ == '__main__':
    app.debug = False
    app.run(host='127.0.0.1', port=5000)