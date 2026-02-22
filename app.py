import os
import random
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from google import genai

# ==============================
# LOAD ENVIRONMENT VARIABLES
# ==============================

load_dotenv()

app = Flask(__name__)

# ==============================
# GEMINI CONFIGURATION
# ==============================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    client = genai.Client(api_key="GEMINI_API_KEY")
else:
    client = None

# ==============================
# MITRE ATTACK SIMULATION DATA
# ==============================

MITRE_ATTACKS = {
    "phishing": {
        "technique": "T1566",
        "description": "Phishing",
        "severity": "High"
    },
    "ransomware": {
        "technique": "T1486",
        "description": "Data Encrypted for Impact",
        "severity": "Critical"
    },
    "bruteforce": {
        "technique": "T1110",
        "description": "Brute Force",
        "severity": "Medium"
    }
}

COUNTRIES = ["China", "Russia", "USA", "Brazil", "Germany"]

# ==============================
# ROUTE: SIMULATE ATTACK
# ==============================

@app.route("/simulate", methods=["POST"])
def simulate_attack():
    data = request.get_json()
    attack_type = data.get("attack_type")

    if attack_type not in MITRE_ATTACKS:
        return jsonify({"error": "Invalid attack type"}), 400

    attack_data = MITRE_ATTACKS[attack_type]

    event = {
        "event_id": random.randint(100000, 999999),
        "attack_type": attack_type,
        "mitre_technique": attack_data["technique"],
        "mitre_description": attack_data["description"],
        "severity": attack_data["severity"],
        "country": random.choice(COUNTRIES)
    }

    return jsonify({
        "message": "Attack simulated successfully",
        "soc_event": event
    })

# ==============================
# ROUTE: ANALYZE WITH GEMINI
# ==============================

@app.route("/analyze", methods=["POST"])
def analyze_attack():

    if not client:
        return jsonify({"error": "Gemini API Key not configured"}), 500

    event_data = request.get_json()

    prompt = f"""
You are a Senior SOC Analyst.

Analyze the following security event and provide:

1. Risk level assessment
2. Possible business impact
3. Recommended mitigation steps
4. Detection improvement suggestions

Event:
{event_data}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # ✅ MODELO ATUAL
            contents=prompt,
        )

        return jsonify({
            "analysis": response.text
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

# ==============================
# OPTIONAL ROOT ROUTE (TEST)
# ==============================

@app.route("/")
def home():
    return "Cyber Attack Simulation Lab API is running 🚀"

# ==============================
# MAIN
# ==============================

if __name__ == "__main__":
    app.run(debug=True)