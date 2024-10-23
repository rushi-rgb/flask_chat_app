# Real-Time Chat Application with Flask and SocketIO.

## Real-Time Chat Application with Flask and SocketIO

This project is a real-time chat application built with Flask and Flask-SocketIO, enabling seamless real-time communication between users. The app automatically assigns random usernames and avatars to connected users and allowing them to join the chat, send messages and update their usernames. All user activities such as joining, messaging, and leaving are broadcasted to all participants in real-time.

### Features:
- **Random Usernames & Avatars**: Each user is assigned a random username and avatar upon connection.
- **Real-Time Communication**: Messages are broadcasted to all connected users instantly using WebSockets.
- **Username Updates**: Users can change their usernames, and changes are reflected in real-time for all users.
- **User Join/Leave Notifications**: The application broadcasts notifications when users join or leave the chat.
- **WebSocket Events**:
  - `connect`: Assigns a random username and avatar to the user.
  - `disconnect`: Notifies others when a user leaves the chat.
  - `send_message`: Handles sending and broadcasting messages from users.
  - `update_username`: Allows users to update their username, notifying all participants of the change.
---

## Technologies Used:
- **Backend**: Flask, Flask-SocketIO (WebSockets for real-time communication).

- **Frontend**: HTML, CSS, JavaScript (SocketIO client library for real-time updates).
---

## How to Run:
To run the Flask-SocketIO app locally, follow these steps:

### Prerequisites:
- **Python** (3.x) installed on your machine.
- **pip** (Python package manager) installed.

### Steps:

1. **Clone the repository** (or download the project files):

   ```bash
   mkdir chat_app
   ```

   ```bash
   cd chat_app
   ```

   ```bash
   git clone https://github.com/prashantm1535/chat_app.git
   ```

2. **Create a virtual environment** (optional but recommended): This step isolates your project dependencies.
   
- On **Windows**:
  ```bash
  python -m venv .venv
  .venv\Scripts\activate
  ```
  
- On **macOS/Linux**:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

3. **Install dependencies**: Install the required Python packages using the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**: Run the app using the `socketio.run` function provided in the `app.py` file.
   
   ```bash
   python app.py
   ```

5. **Access the app in your browser**: Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```
---

### Optional:
- If you're developing the app and want the server to auto-reload upon file changes, ensure that `debug=True` is set in the following line:
   ```python
   socketio.run(app, debug=True)
   ```

By following these steps, the application should be fully operational on your local machine!

---

### Some resource links used in this projects : 

### Avatar URL :
[avatar url](https://avatar.iran.liara.run/public/boy?username=user_123)

---
