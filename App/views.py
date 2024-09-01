from pymongo import MongoClient
from models import users, tasks
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify, request
from bson.objectid import ObjectId


def sign_up():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    if users.find_one({"username": username}):
        return jsonify({"message": "Username already exists"}), 400

    hashed_password = generate_password_hash(password)

    user_id = ObjectId()
    user = {
        "_id": user_id,
        "username": username,
        "password": hashed_password
    }

    users.insert_one(user)

    return jsonify({"message": "User registered successfully", "user_id": str(user_id)}), 201


def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    user = users.find_one({"username": username})
    if not user:
        return jsonify({"message": "Invalid username or password"}), 401

    if not check_password_hash(user['password'], password):
        return jsonify({"message": "Invalid username or password"}), 401

    return jsonify({"message": "Login successful", "user_id": str(user['_id'])}), 200


def add_task():
    data = request.get_json()
    task_title = data.get('title')
    task_description = data.get('description')

    task = {
        "title": task_title,
        "description": task_description,
        "completed": False
    }

    tasks.insert_one(task)
    return jsonify({"message": "Task added successfully"}), 201

//omo

