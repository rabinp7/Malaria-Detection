import cv2
from PIL import Image, ImageOps
import numpy as np
from tensorflow.keras.models import load_model
import streamlit as st 



model_path = 'malaria_calssifier_model.h5'
model = load_model(model_path)

def import_and_predict(image_data, model):
        size = (50,50)    
        image = ImageOps.fit(image_data, size, ImageOps.Image.BOX)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        img_resize = (cv2.resize(img, dsize=(50, 50), interpolation=cv2.INTER_CUBIC))/255.
        
        img_reshape = img_resize[np.newaxis,...]
    
        prediction = model.predict(img_reshape)
        
        return prediction

st.write("""
         # Malaria_Detection_App 
         """
         )
st.markdown('''
    ## About
    ''')
st.write("This is a simple Malaria classification web app to predict Parasitisized or Unifected Malaria cell made by [Pritiranjan]")

file = st.file_uploader("Please upload an image file", type=["jpg", "png"])
#k


if file is None:
    st.text("You haven't uploaded an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    if  np.argmax(prediction) == 0:
        st.write('This Image is **Infected** ')
    else:
        st.write('This Image is **Not Infected** ')

    
        
        
        

        
    

