
import streamlit as st
st.title("welcome to kids story teller")
st.header("Hi")
st.subheader("we generate interactive and intresting stories from the image provided")
# Display Images

# import Image from pillow to open images
from PIL import Image
img = Image.open("C:\\Users\\vyshn\OneDrive\\Desktop\\download2.jpg")

# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)
st.file_uploader('upload your image')
st.balloons()
