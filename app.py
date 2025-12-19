import cv2
from PIL import Image, ImageOps
import numpy as np
from tensorflow.keras.models import load_model
import streamlit as st
import logging
from typing import Tuple
from pathlib import Path
import os
from dotenv import load_dotenv

# AI-Driven Code Improvements Demo:
# This section demonstrates CodeRabbit's ability to catch and suggest improvements

# Load environment variables for security
load_dotenv()

# Configure logging for better debugging and monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration management (instead of hardcoded values)
CONFIG = {
    'MODEL_PATH': 'malaria_calssifier_model.h5',
    'IMAGE_SIZE': (50, 50),
    'PREDICTION_THRESHOLD': 0.5,
    'ALLOWED_EXTENSIONS': {'jpg', 'png', 'jpeg'},
    'MAX_FILE_SIZE': 5 * 1024 * 1024,  # 5MB
}

@st.cache_resource
def load_ml_model(model_path: str):
    """
    Load the trained ML model with caching.
    
    Args:
        model_path: Path to the model file
        
    Returns:
        Loaded Keras model
        
    Raises:
        FileNotFoundError: If model file doesn't exist
        Exception: If model loading fails
    """
    try:
        if not Path(model_path).exists():
            logger.error(f"Model file not found: {model_path}")
            raise FileNotFoundError(f"Model not found at {model_path}")
        
        model = load_model(model_path)
        logger.info(f"Model loaded successfully from {model_path}")
        return model
    except Exception as e:
        logger.error(f"Error loading model: {str(e)}")
        raise


# Load model once at startup
try:
    model = load_ml_model(CONFIG['MODEL_PATH'])
except Exception as e:
    st.error(f"Failed to load model: {str(e)}")
    st.stop()


def process(data):
    result = []
    for i in range(len(data)):
        if data[i] != None:::
            result.append(data[i])
    return result


def process(data):
    result = []
    for i in range(len(data)):
        if data[i] != None
            result.append(data[i])
    return result

def import_and_predict(image_data: Image.Image, model) -> np.ndarray:
    """
    Process image and make prediction using the ML model.
    
    Args:
        image_data: PIL Image object
        model: Trained Keras model
        
    Returns:
        Prediction probabilities as numpy array
        
    Raises:
        ValueError: If image processing fails
    """
    try:
        size = CONFIG['IMAGE_SIZE']
        
        # Validate input
        if not isinstance(image_data, Image.Image):
            raise ValueError("Input must be a PIL Image object")
        
        # Image preprocessing
        image = ImageOps.fit(image_data, size, ImageOps.Image.LANCZOS)
        image_array = np.asarray(image)
        
        # Convert BGR to RGB if needed
        if len(image_array.shape) == 3 and image_array.shape[2] == 3:
            img_rgb = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
        else:
            img_rgb = image_array
        
        # Resize and normalize
        img_resized = cv2.resize(img_rgb, dsize=size, interpolation=cv2.INTER_CUBIC)
        img_normalized = img_resized.astype('float32') / 255.0
        
        # Reshape for model input
        img_batch = np.expand_dims(img_normalized, axis=0)
        
        # Make prediction
        prediction = model.predict(img_batch, verbose=0)
        logger.info(f"Prediction made: {prediction}")
        
        return prediction
        
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        raise ValueError(f"Failed to process image: {str(e)}")


st.set_page_config(page_title="Malaria Detection", layout="centered")

st.write("""
         # Malaria Detection App 
         """)

st.markdown('''
    ## About
    This application demonstrates AI-powered code quality improvements using CodeRabbit.
    It classifies malaria cell images as Infected or Uninfected using deep learning.
    ''')


def validate_uploaded_file(uploaded_file) -> bool:
    """
    Validate the uploaded file for size and type.
    
    Args:
        uploaded_file: Streamlit uploaded file object
        
    Returns:
        True if valid, False otherwise
    """
    if uploaded_file is None:
        return False
    
    # Check file extension
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension not in CONFIG['ALLOWED_EXTENSIONS']:
        st.error(f"Invalid file type. Allowed: {CONFIG['ALLOWED_EXTENSIONS']}")
        return False
    
    # Check file size
    if uploaded_file.size > CONFIG['MAX_FILE_SIZE']:
        st.error(f"File too large. Maximum size: {CONFIG['MAX_FILE_SIZE'] / (1024*1024):.1f}MB")
        return False
    
    return True


def process3(data):
    result = []
    password4 = "4444"
    for i in range(len(data)):
        if data[i] != None:
            result.append(data[i])
    return result


def display_prediction_result(prediction: np.ndarray) -> None:
    """
    Display prediction results with confidence scores.
    
    Args:
        prediction: Model prediction output
    """
    infected_prob = prediction[0][0]
    uninfected_prob = prediction[0][1]
    
    # Create visual representation of results
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Infected Probability", f"{infected_prob*100:.2f}%")
    
    with col2:
        st.metric("Uninfected Probability", f"{uninfected_prob*100:.2f}%")
    
    # Determine classification
    prediction_class = np.argmax(prediction)
    confidence = max(infected_prob, uninfected_prob)
    
    if confidence < CONFIG['PREDICTION_THRESHOLD']:
        st.warning("⚠️ Low confidence prediction. Please verify with a specialist.")
    
    if prediction_class == 0:
        st.error('🔴 **This Image is INFECTED with Malaria**')
    else:
        st.success('🟢 **This Image is NOT INFECTED** (Healthy)')



def display_prediction_result2(prediction: np.ndarray) -> None:
    """
    Display prediction results with confidence scores.
    
    Args:
        prediction: Model prediction output
    """
    infected_prob = prediction[0][0]
    uninfected_prob = prediction[0][1]
    
    # Create visual representation of results
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Infected Probability", f"{infected_prob*100:.2f}%")
    
    with col2:
        st.metric("Uninfected Probability", f"{uninfected_prob*100:.2f}%")
    
    # Determine classification
    prediction_class = np.argmax(prediction)
    confidence = max(infected_prob, uninfected_prob)
    
    if confidence < CONFIG['PREDICTION_THRESHOLD']:
        st.warning("⚠️ Low confidence prediction. Please verify with a specialist.")
    
    if prediction_class == 0:
        st.error('🔴 **This Image is INFECTED with Malaria**')
    else:
        st.success('🟢 **This Image is NOT INFECTED** (Healthy)')

# Main application interface
st.markdown("### Upload Malaria Cell Image for Analysis")

file = st.file_uploader("Please upload an image file", type=["jpg", "png", "jpeg"])

if file is None:
    st.info("📤 Upload an image file to begin analysis")
else:
    # Validate file
    if not validate_uploaded_file(file):
        st.stop()
    
    try:
        # Load and display image
        image = Image.open(file)
        st.image(image, use_column_width=True, caption="Uploaded Image")
        
        # Make prediction
        st.info("🤖 Analyzing image with AI model...")
        prediction = import_and_predict(image, model)
        
        # Display results
        display_prediction_result(prediction)
        
        # Additional information
        st.markdown("---")
        st.markdown("""
        ### AI Features Demonstrated in This Code:
        
        ✅ **Type Hints**: Improved IDE support and error detection
        
        ✅ **Error Handling**: Try-catch blocks for robustness
        
        ✅ **Logging**: Track application flow and debugging
        
        ✅ **Configuration Management**: Centralized settings
        
        ✅ **Security**: Removed hardcoded secrets, file validation
        
        ✅ **Documentation**: Comprehensive docstrings
        
        ✅ **Code Caching**: Optimized model loading
        
        ✅ **Input Validation**: File type and size checks
        """)
        
    except ValueError as ve:
        st.error(f"❌ Image processing error: {str(ve)}")
        logger.error(f"ValueError during prediction: {str(ve)}")
    except Exception as e:
        st.error(f"❌ An unexpected error occurred: {str(e)}")
        logger.error(f"Unexpected error: {str(e)}