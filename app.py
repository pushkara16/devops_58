from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "POST":
		name = request.form.get("name", "").strip()
		email = request.form.get("email", "").strip()
		student_id = request.form.get("student_id", "").strip()

		if name == email == student_id:
			return render_template("successful.htm")

	return render_template("registration.html")

if __name__ == "__main__":
	app.run(debug=True)
