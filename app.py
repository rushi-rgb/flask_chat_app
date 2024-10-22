from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
socketio = SocketIO(app)

# python dict. store connected users. key is socketid value is username and avatarUrl
users = {}

# route for index page
@app.route('/')
def index():
    return render_template('index.html')

# we're listening for the connect event
@socketio.on("connect")
def handle_connect():
    username = f"user_{random.randint(1000,9999)}"
    gender = random.choice(["girl", "boy"])
    # https://avatar.iran.liara.run/public/boy?username=user_123
    avatar_url = f"https://avatar.iran.liara.run/public/{gender}?username={username}"
    
    # to get user from username and avatar url
    users[request.sid] = {"username":username, "avatar":avatar_url}
    
    # to get joined user info
    emit("user_joined", {"username":username, "avatar":avatar_url}, broadcast=True)
    
    # to notify about the joined user
    emit("set_username", {"username":username})
    
if __name__ == "__main__":
    socketio.run(app, debug=True)