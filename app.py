from flask import Flask, request, jsonify
import ollama

app = Flask(__name__)
@app.route("/generate-email", methods=["POST"])
def generate_email():
    data = request.get_json()
    subject = data.get("subject", "")
    recipient = data.get("recipient", "Colleague")
    date = data.get("date", "")
    background = data.get("background", "")
    tone = data.get("tone", "formal")
    salutation = data.get("salutation", "Dear")
    closing = data.get("closing", "Regards")
    sender = data.get("sender", "Your Name")

    # 👇 Combine salutation + recipient into one line
    salutation_line = f"{salutation} {recipient},"

    prompt = f"""
    You are an assistant that writes {tone} professional emails for office communication.

    Subject: {subject}
    Date: {date}

    Background: {background}

    Start the email with this salutation line:
    {salutation_line}

    End the email with this closing:
    {closing},
    {sender}

    Make sure the email includes a greeting, clear body, and polite closing.
    """

    response = ollama.chat(
        model="llama3.2:latest",
        messages=[
            {"role": "system", "content": "You are an expert at writing workplace emails."},
            {"role": "user", "content": prompt}
        ]
    )

    return jsonify({"email": response['message']['content']})


if __name__ == "__main__":
    app.run(debug=True)
