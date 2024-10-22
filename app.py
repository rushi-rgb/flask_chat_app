from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import random

# Flask and SocketIO Initialization
app = Flask(__name__)
socketio = SocketIO(app)

# python dictionary to store connected users. key is socket id, value is username and avatarUrl
users = {}


# Route for home page
@app.route('/')
def index():
    return render_template('index.html')


# Handling User Connection (Socket Event `connect`)
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
    

# Handling User Disconnection (Socket Event `disconnect`)
@socketio.on("disconnect")
def handle_disconnect():
    user = users.pop(request.sid, None)
    
    if user:
        emit("user_left",{"username":user["username"]}, broadcast=True)
 
     
# Handling Send Message Event (Socket Event `send_message`)
@socketio.on("send_message")
def handle_message(data):
    user = users.get(request.sid)
    
    if user:
        emit("new_message",{
            "username":user["username"],
            "avatar":user["avatar"],
            "message":data["message"]
        },broadcast=True)


# Handling Update Username Event (Socket Event `update_username`)
@socketio.on("update_username")
def handle_update_username(data):
    old_username = users[request.sid]["username"]
    new_username = data["username"]
    users[request.sid]["username"] = new_username

    emit("username_updated",{
        "old_username":old_username,
        "new_username":new_username
    },broadcast=True)


# Running the Flask-SocketIO Application
if __name__ == "__main__":
    socketio.run(app, debug=True)