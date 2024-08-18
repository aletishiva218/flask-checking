from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
data = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"},
]

# Route to get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)