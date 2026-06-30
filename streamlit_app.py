import os
import streamlit as st
from streamlit_image_comparison import image_comparison
import cv2
from translations import get_text

AZURE_SAS_URI = os.environ.get("SAS_TOKEN")

try:
    base_uri, token = AZURE_SAS_URI.split("?", 1)
    if not base_uri or not token:
        raise ValueError
except Exception as e:
    st.error(get_text("error_sas_token", st.session_state.get("language", "en")))
    st.stop()

# Initialize language in session state
if "language" not in st.session_state:
    st.session_state.language = "en"
    
def toggleLanguage():
    if st.session_state.language == "en":
        st.session_state.language = "fr"
    else:
        st.session_state.language = "en"
        
st.button(get_text("language", st.session_state.language), on_click=toggleLanguage, type="primary")

# Set page config with translated title
st.set_page_config(get_text("page_title", st.session_state.language), "🔭")

# Get translation function for current language
def t(key: str) -> str:
    return get_text(key, st.session_state.language)

st.header(t("header"))

st.write(t("intro_line1"))
st.write(t("intro_line2"))

st.markdown(f"### {t('southern_nebula')}")
try:
    image_comparison(
        img1=f"{base_uri}/hubble/southern_nebula_700.jpg?{token}",
        img2=f"{base_uri}/webb/southern_nebula_700.jpg?{token}",
        label1="Hubble",
        label2="Webb",
    )
except Exception as e:
    st.error(t("error_image_load"))

st.markdown(f"### {t('galaxy_cluster')}")
try:
    image_comparison(
        img1=f"{base_uri}/hubble/deep_field_700.jpg?{token}",
        img2=f"{base_uri}/webb/deep_field_700.jpg?{token}",
        label1="Hubble",
        label2="Webb",
    )
except Exception as e:
    st.error(t("error_image_load"))

st.markdown(f"### {t('carina_nebula')}")
try:
    image_comparison(
        img1=f"{base_uri}/hubble/carina_2800.png?{token}",
        img2=f"{base_uri}/webb/carina_2800.jpg?{token}",
        label1="Hubble",
        label2="Webb",
    )
except Exception as e:
    st.error(t("error_image_load"))

st.markdown(f"### {t('stephans_quintet')}")
try:
    image_comparison(
        img1=f"{base_uri}/hubble/stephans_quintet_2800.jpg?{token}",
        img2=f"{base_uri}/webb/stephans_quintet_2800.jpg?{token}",
        label1="Hubble",
        label2="Webb",
    )
except Exception as e:
    st.error(t("error_image_load"))
