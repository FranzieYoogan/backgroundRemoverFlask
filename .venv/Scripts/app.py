from flask import render_template, request
from flask import Flask
import os
from rembg import remove 
from PIL import Image 
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/bgRemoverPython/bg/.venv/Scripts/static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        
     fileInput = request.files['fileInput'] 

     filename = secure_filename(fileInput.filename)

     fileInput.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
     
     if(filename):
     # Store path of the image in the variable input_path   
        input_path =  f'/bgRemoverPython/bg/.venv/Scripts/static/uploads/{filename}'
            
            # Store path of the output image in the variable output_path 
        output_path = '/bgRemoverPython/bg/.venv/Scripts/static/uploads/bgChanged.png' 
            
            # Processing the image 
        input = Image.open(input_path) 
        

            # Removing the background from the given Image 
        output = remove(input) 
            
            #Saving the image in the given path 
        output.save(output_path) 
        output.show()
        

        return render_template('index.htm',output_path = output_path, filename = filename)
    
    else:
    
    
     return render_template('index.htm')

app.run(debug=True, host="0.0.0.0", port=8000)