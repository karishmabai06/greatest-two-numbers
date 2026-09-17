from flask import Flask, render_template, request

app = Flask(__name__)

def greatest_of_three(a, b, c):
    return max(a, b, c)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    num1 = num2 = num3 = ""
    
    if request.method == "POST":
        try:
            # Get numbers from the HTML form and convert to integers
            num1 = int(request.form["num1"])
            num2 = int(request.form["num2"])
            num3 = int(request.form["num3"])
            
            # Calculate the greatest number
            result = greatest_of_three(num1, num2, num3)
        except ValueError:
            result = "Error: Please enter valid integers."

    return render_template("index.html", result=result, num1=num1, num2=num2, num3=num3)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)