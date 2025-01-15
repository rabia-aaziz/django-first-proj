from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS)
from flask_cors import CORS
CORS(app)

# Load the chatbot model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

@app.route("/")
def home():
    """Render the chatbot interface."""
    return render_template("chat.html")

@app.route("/chat", methods=["GET"])
def chat():
    """Handle chatbot responses."""
    user_input = request.args.get("msg")
    if user_input:
        inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
        outputs = model.generate(inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
        return jsonify({"response": response})
    return jsonify({"response": "I didn't understand that. Could you please rephrase?"})

if __name__ == "__main__":
    app.run(debug=True)