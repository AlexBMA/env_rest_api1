import os

from flask import (
    Flask,
    render_template,
    request
)

import connexion

#from pack1.clasify import ImgClassifier
from clasify import ImgClassifier

# Create the application instance
app = Flask(__name__)
# connexion.App(__name__, specification_dir='./')


UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Read the swagger.yml file to configure the endpoints
# app.add_api('swagger.yml')



# Create the application instance
# app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload():

	file = request.files['image']
	filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

	file.save(filename)
	print(filename)
	#resultClassification = ImgClassifier.classify_img(filename, ImgClassifier.path_model, ImgClassifier.path_pickle)

	#print(resultClassification)
	
	print("done");

	return render_template("done.html")

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)