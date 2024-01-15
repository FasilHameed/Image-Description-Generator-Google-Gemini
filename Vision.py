# Import necessary libraries
import os
from dotenv import load_dotenv
import streamlit as st
from PIL import Image

# Import the Generative AI library
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Generative AI API with the provided key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the Generative AI model and get responses
def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input_prompt != "":
        response = model.generate_content([input_prompt, image])
    else:
        response = model.generate_content(image)
    return response.text

# Customizing Streamlit UI
st.set_page_config(
    page_title="Image Captioning AI",
    page_icon="🖼️",
    layout="wide",  # Change layout to wide
)

# Customizing UI elements
st.title("🌟 Creative Image Captioning AI 🌟")
st.markdown(
    """
    Welcome to the Creative Image Captioning AI Application! Upload an image,
    and let the AI generate a unique and artistic caption for you!
    """
)

# User input for image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image_placeholder_url = "https://via.placeholder.com/500"  # Placeholder image URL

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", width=500)
else:
    # Adjust the width of the placeholder image
    st.image(image_placeholder_url, caption="No Image Uploaded.", width=200, output_format='auto')

# Optional prompt below the image
input_prompt = st.text_input("Optional Prompt:")

# Button to trigger the API call
if st.button("Generate Creative Description 🚀"):
    try:
        response = get_gemini_response(input_prompt, image)
        st.subheader("Generated Creative Description:")
        st.write(response)
    except Exception as e:
        st.error("An error occurred during the API call. Please try again.")
        # Optionally, you can print or log the error for further investigation
        print(f"Error: {e}")
