from flask import Flask, render_template, request, jsonify     #, send_file
from proto import hide_message, extract_message

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hide_message', methods=['POST'])
def hide():
    message = request.form['message']
    image = request.files['image']
    output_image_path = "output_image.png"
    hide_message(image, message, output_image_path)
    return jsonify({"success": True})

@app.route('/extract_message', methods=['POST'])
def extract():
    image = request.files['image']
    extracted_message = extract_message(image)
    # return send_file("output_image.png", as_attachment=True)
    return jsonify({"message": extracted_message})

if __name__ == '__main__':
    app.run(debug=True)