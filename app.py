from flask import Flask, render_template, jsonify
from facereconize_auto import verify_face

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/verify')
def verify():
    result, name = verify_face()
    if result:
        return jsonify({'status': 'Verified', 'name': name})
    else:
        return jsonify({'status': 'Not Verified'})

if __name__ == '__main__':
    app.run(debug=True)
