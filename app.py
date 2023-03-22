import streamlit as st
from util import *
from PIL import Image

st.set_page_config(page_title='Cat Breed Classifier', layout='centered')

st.title("Cat Breed Classifier")
st.subheader("Upload your cat image or be doomed")

cat = st.sidebar.file_uploader("Upload yo cat")

if cat:
    st.image(cat)
    image = Image.open(cat)
    img_array = np.array(image)
    st.subheader("your cat is "+ get_prediction(img_array)[0])

    


