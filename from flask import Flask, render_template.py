from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time

# Flask App Initialize
app = Flask(_name_)

# ChatBot Initialization
chatbot = ChatBot("MyChatBot")
trainer = ListTrainer(chatbot)

# Training the ChatBot
trainer.train([
    "Hello",
    "Hi there!",
    "How are you?",
    "I'm good, thank you!",
    "What's your name?",
    "I'm a chatbot, created by you.",
    "Bye",
    "Goodbye!"
])

# Flask Routes
@app.route("/")
def index():
    return render_template("index.html")  # Ensure you have this HTML file

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.form["message"]
    bot_response = chatbot.get_response(user_message)
    return str(bot_response)

if _name_ == "_main_":
    app.run(debug=True)