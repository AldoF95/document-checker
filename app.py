from flask import Flask, render_template, request
from main import calculate_level

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "/"

@app.route("/")
def root():
    return render_template("upload_form.html")
   

@app.route("/level", methods=['GET', 'POST'])
def get_level():
    if request.method=='POST':
        f = request.files['file']
        f.save(f.filename)
        print("file saved successfuly")
        awl_ratio, lfwl_ratio, scale_level = calculate_level(f.filename)
        if awl_ratio==400: return f"{lfwl_ratio}! Msg:{scale_level}"
        return f"awl ratio {awl_ratio}%; low freq word ratio {lfwl_ratio}%; Complexity level '{scale_level}'"

if __name__=="__main__":
    app.run(port=5000, debug=True)