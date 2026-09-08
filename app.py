from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>My Customer Chatbot</title>
</head>
<body>
    <h1>🤖 My Customer Chatbot</h1>

    <form method="POST">
        <input type="text" name="question"
               placeholder="Apna sawal likhein" required>
        <button type="submit">Send</button>
    </form>

    {% if answer %}
        <h3>Bot:</h3>
        <p>{{ answer }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""

    if request.method == "POST":
        question = request.form["question"].lower()

        if "hello" in question or "hi" in question or "namaste" in question:
            answer = "Namaste! 😊 Main aapki madad karne ke liye yahan hoon."

        elif "price" in question or "daam" in question or "paisa" in question:
            answer = "Shoes ₹1499, Jeans ₹999 aur T-Shirt ₹499 ki hai."

        elif "delivery" in question:
            answer = "Normal delivery 3-7 din mein hoti hai."

        elif "order" in question:
            answer = "Order karne ke liye product ka naam aur quantity batayein."

        else:
            answer = "Maaf kijiye, main is sawal ko abhi samajh nahi paaya."

    return render_template_string(HTML, answer=answer)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)