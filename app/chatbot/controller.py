from app import app
from flask import render_template, request, Blueprint, jsonify 
from config import *
import os
import openai
import json
from dotenv import load_dotenv
load_dotenv()

chatbot_page = Blueprint('chatbot', __name__, url_prefix='/chatbot')

from flask import Flask, render_template, request, redirect, url_for, send_from_directory

token = GPT_TOKEN
openai.api_key = token

print("token:", token)

def generate_response(prompt):
    result = openai.ChatCompletion.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature = 0.7
    )

    print("waiting response from OPEN AI.")

    message = result.choices[0].message['content']
    return message

@chatbot_page.route('/')
def home():
    return render_template('chatbot/index.html')

@chatbot_page.route('/text')
def text():
    return "Chào Fen !"

@chatbot_page.route("/", methods=["POST"])
def chatbot():
    data = request.get_json()
    prompt = data["prompt"]
    message = generate_response(prompt)
    print(message)
    return message

@chatbot_page.route('/test')
def test():
    return generate_response("chào bạn")