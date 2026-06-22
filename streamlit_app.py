import os
import streamlit as st
from streamlit_image_comparison import image_comparison
import cv2

AZURE_SAS_URI = os.environ.get("BLOB_SAS_TOKEN")

base_uri, token = AZURE_SAS_URI.split("?", 1)

st.set_page_config("Webb Space Telescope vs Hubble Telescope", "🔭")

st.header("J. Webb Space Telescope vs Hubble Telescope")

st.write("")
"This is a reproduction of the fantastic [WebbCompare](https://www.webbcompare.com/index.html) app by [John Christensen](https://twitter.com/JohnnyC1423). It's built in Streamlit and takes only 10 lines of Python code. If you like this app, please star [John's original repo](https://github.com/JohnEdChristensen/WebbCompare)!"
st.write("")

st.markdown("### Southern Nebula")
image_comparison(
    img1=f"{base_uri}/hubble/southern_nebula_700.jpg?{token}",
    img2=f"{base_uri}/webb/southern_nebula_700.jpg?{token}",
    label1="Hubble",
    label2="Webb",
)


st.markdown("### Galaxy Cluster SMACS 0723")
image_comparison(
    img1=f"{base_uri}/hubble/deep_field_700.jpg?{token}",
    img2=f"{base_uri}/webb/deep_field_700.jpg?{token}",
    label1="Hubble",
    label2="Webb",
)

st.markdown("### Carina Nebula")
image_comparison(
    img1=f"{base_uri}/hubble/carina_2800.png?{token}",
    img2=f"{base_uri}/webb/carina_2800.jpg?{token}",
    label1="Hubble",
    label2="Webb",
)

st.markdown("### Stephan's Quintet")
image_comparison(
    img1=f"{base_uri}/hubble/stephans_quintet_2800.png?{token}",
    img2=f"{base_uri}/webb/stephans_quintet_2800.jpg?{token}",
    label1="Hubble",
    label2="Webb",
)


