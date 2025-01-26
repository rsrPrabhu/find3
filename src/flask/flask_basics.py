from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Path to the local JSON data file
DATA_FILE = 'data.json'


# 1. Read the data from the local file (JSON)
def load_data():
    if not os.path.exists(DATA_FILE):
        return {'users': []}  # Return empty data if the file doesn't exist
    with open(DATA_FILE, 'r') as file:
        return json.load(file)


# 2. Write data back to the local file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)


# 3. Define the API endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    data = load_data()  # Load data from the file
    return jsonify(data['users'])  # Return the list of users as JSON


# 4. Define the API endpoint to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = load_data()  # Load current data
    new_user = request.get_json()  # Get new user data from the request

    # Make sure the new user has the required fields
    if 'name' not in new_user or 'age' not in new_user:
        return jsonify({'error': 'Missing name or age'}), 400

    # Add the new user to the data
    new_user['id'] = len(data['users']) + 1  # Generate a new user ID
    data['users'].append(new_user)

    # Save the updated data back to the file
    save_data(data)

    return jsonify({'message': 'User added successfully', 'user': new_user}), 201


# 5. Define the API endpoint to get a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    data = load_data()
    user = next((u for u in data['users'] if u['id'] == user_id), None)

    if user is None:
        return jsonify({'error': 'User not found'}), 404

    return jsonify(user)


# 6. Define the API endpoint to update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = load_data()
    user = next((u for u in data['users'] if u['id'] == user_id), None)

    if user is None:
        return jsonify({'error': 'User not found'}), 404

    # Update user data from the request
    updated_info = request.get_json()
    user.update(updated_info)

    # Save the updated data back to the file
    save_data(data)

    return jsonify({'message': 'User updated successfully', 'user': user})


# 7. Define the API endpoint to delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    data = load_data()
    user = next((u for u in data['users'] if u['id'] == user_id), None)

    if user is None:
        return jsonify({'error': 'User not found'}), 404

    data['users'] = [u for u in data['users'] if u['id'] != user_id]

    # Save the updated data back to the file
    save_data(data)

    return jsonify({'message': 'User deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
