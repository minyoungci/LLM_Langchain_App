# Flask 사용

from ice_breaker import ice_break
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["post"])
def process():
    name = request.form["name"]
    summary_and_facts, interests, ice_breakers, profile_pic_url = ice_break(
        name=name
    )
    return jsonify(
        {
            "summary_and_facts": summary_and_facts.to_dict(),
            "interests": interests.to_dict(),
            "ice_breakers": ice_breakers.to_dict(),
            "picture_url": profile_pic_url,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
