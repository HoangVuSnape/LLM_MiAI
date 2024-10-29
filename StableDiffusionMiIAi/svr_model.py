from flask import Flask, request, render_template
from text2img_model import create_pipeline, text2img

# Init Flask app
app = Flask(__name__)

# Define parameters
IMAGE_PATH = "static/output.jpg"

# Init pipline
pipline = create_pipeline()

@app.route("/", methods = ['GET', 'POST'])

def index():
    # Check the user view the Web
    if request.method == "GET":
        # Return to web display
        return render_template("index.html")
    else:
        # Solve the user to submit prompt -> Gen image -> return
        user_input = request.form["prompt"]

        print("Start gen...")
        im = text2img(user_input, pipeline=pipline)
        print("Finish gen....")

        im.save(IMAGE_PATH)

        return render_template("index.html", image_url = IMAGE_PATH)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8888, use_reloader= False)
