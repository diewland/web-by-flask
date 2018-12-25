from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# index
@app.route('/')
def hello():
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(debug=True)
