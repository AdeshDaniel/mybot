from flask import Flask, request, render_template
import jwt
import time
import hashlib
import hmac
import requests

app = Flask(__name__)

BOT_TOKEN = '7688238747:AAFyyAnQxrEijQ8Zzo6UZ1oY8CjmgT2DXDs'
ADMIN_ID = '5452541589'
SECRET_KEY = '80caf0ca13d7d868a70b5796855323cbb09e389bc2414ef4ce08d66bd3cda564'  # For JWT

# Calculate Telegram Login verification key
TELEGRAM_SECRET = hashlib.sha256(BOT_TOKEN.encode()).digest()

def verify_telegram_auth(data):
    received_hash = data.pop('hash')
    data_check = '\n'.join([f"{k}={v}" for k, v in sorted(data.items())])
    hmac_hash = hmac.new(TELEGRAM_SECRET, data_check.encode(), 'sha256').hexdigest()
    return hmac_hash == received_hash

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/verify", methods=["POST"])
def verify():
    data = request.json
    if not verify_telegram_auth(data.copy()):
        return {"error": "Verification failed"}, 403

    # Generate JWT
    token = jwt.encode({
        "id": data["id"],
        "username": data.get("username"),
        "first_name": data.get("first_name"),
        "exp": time.time() + 3600  # 1 hour expiry
    }, SECRET_KEY, algorithm="HS256")

    # Send to admin via bot
    login_link = f"https://mybot-3ha8.onrender.com/login?token={token}"

    message = (
        f"🧾 New Login:\n\n"
        f"👤 Name: {data.get('first_name')} {data.get('last_name', '')}\n"
        f"🔗 Username: @{data.get('username')}\n"
        f"🆔 ID: {data.get('id')}\n\n"
        f"🔐 JWT Login: {login_link}"
    )

    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={
        "chat_id": ADMIN_ID,
        "text": message
    })

    return {"status": "success"}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
