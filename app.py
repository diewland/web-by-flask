from flask import Flask, render_template, request, jsonify
import base64

app = Flask(__name__)

# front
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/webcam')
def webcam():
    return render_template('webcam.html')

# process
def process(input_val):
    return input_val * 3

# controller
@app.route('/trible', methods=['POST'])
def trible():
    input_val = request.json.get('input')
    output_val = process(input_val)
    print("input => %s" % input_val)
    print("output => %s" % output_val)
    return jsonify({
        'success': True,
        'data': output_val,
    })

@app.route('/save_photo', methods=['POST'])
def save_photo():
    b64img = request.json.get('img')
    b64img = b64img.split(',')[1] # remove "data:image/jpeg;base64,"

    with open("./static/latest.jpg", "wb") as fh:
        fh.write(base64.decodebytes(b64img.encode()))

    return jsonify({
        'success': True,
        'message': 'done',
    })

if __name__ == '__main__':
    app.run(debug=True)
