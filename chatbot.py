from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from TextReader import chatbotContent
import time
time.clock = time.time

app = Flask(__name__)

chatbotFile = "chatbot.txt"

chatbot = ChatBot("ChatBot")

trainer = ListTrainer(chatbot)
chatbotContent =  chatbotContent(chatbotFile)
trainer.train(chatbotContent)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get", methods=["GET","POST"])
def chatbot_response():
    message = request.form["message"]
    response = chatbot.get.response(message)
    return str(response)

if __name__ == "__main__":
    app.run()
                           