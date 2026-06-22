import os
import streamlit as st
from streamlit_image_comparison import image_comparison
import cv2

AZURE_SAS_URI = os.environ.get("SAS_TOKEN")

try:
    base_uri, token = AZURE_SAS_URI.split("?", 1)
    if not base_uri or not token:
        raise ValueError
except Exception as e:
    st.error("Invalid SAS_TOKEN format. Please ensure it is in the format 'https://<storage_account>.blob.core.windows.net/<container>?<sas_token>'.")
    st.stop()

st.set_page_config("Webb Space Telescope vs Hubble Telescope", "🔭")

st.header("J. Webb Space Telescope vs Hubble Telescope")

st.write("This is the [Streamlit example application](https://github.com/streamlit/example-app-image-comparison) refactored to run on the Federal Science DataHub using images in the FSDH Azure Blob Storage.")
st.write("The code for this version can be found on [GitHub](https://github.com/Sean-Stilwell/example-app-image-comparison).")

st.markdown("### Southern Nebula")
try:
    image_comparison(
        img1=f"{base_uri}/hubble/southern_nebula_700.jpg?{token}",
        img2=f"{base_uri}/webb/southern_nebula_700.jpg?{token}",
        label1="Hubble",
        label2="Webb",
    )
except Exception as e:
    st.error("This image failed to load. Verify the file exists in the Azure Blob Storage")

st.markdown("### Galaxy Cluster SMACS 0723")
try:
    image_comparison(
        img1=f"{base_uri}/hubble/deep_field_700.jpg?{token}",
        img2=f"{base_uri}/webb/deep_field_700.jpg?{token}",
        label1="Hubble",
        label2="Webb",
    )
except Exception as e:
    st.error("This image failed to load. Verify the file exists in the Azure Blob Storage")

st.markdown("### Carina Nebula")
try:
    image_comparison(
        img1=f"{base_uri}/hubble/carina_2800.png?{token}",
        img2=f"{base_uri}/webb/carina_2800.jpg?{token}",
        label1="Hubble",
        label2="Webb",
    )
except Exception as e:
    st.error("This image failed to load. Verify the file exists in the Azure Blob Storage")

st.markdown("### Stephan's Quintet")
try:
    image_comparison(
        img1=f"{base_uri}/hubble/stephans_quintet_2800.jpg?{token}",
        img2=f"{base_uri}/webb/stephans_quintet_2800.jpg?{token}",
        label1="Hubble",
        label2="Webb",
    )
except Exception as e:
    st.error("This image failed to load. Verify the file exists in the Azure Blob Storage")
