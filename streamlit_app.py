import os
import streamlit as st
from streamlit_image_comparison import image_comparison
from translations import get_text

AZURE_SAS_TOKEN = os.environ.get("BLOB_SAS_TOKEN") # e.g. ?sv=<token>
AZURE_SAS_URI = os.environ.get("BLOB_ACCOUNT_URL") # e.g. https://<account_name>.blob.core.windows.net

try:
    if not AZURE_SAS_URI or not AZURE_SAS_TOKEN:
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
        img1=f"{AZURE_SAS_URI}/datahub/hubble/southern_nebula_700.jpg{AZURE_SAS_TOKEN}",
        img2=f"{AZURE_SAS_URI}/datahub/webb/southern_nebula_700.jpg{AZURE_SAS_TOKEN}",
        label1="Hubble",
        label2="Webb",
    )
except Exception as e:
    st.error(t("error_image_load"))

st.markdown(f"### {t('galaxy_cluster')}")
try:
    image_comparison(
        img1=f"{AZURE_SAS_URI}/datahub/hubble/deep_field_700.jpg{AZURE_SAS_TOKEN}",
        img2=f"{AZURE_SAS_URI}/datahub/webb/deep_field_700.jpg{AZURE_SAS_TOKEN}",
        label1="Hubble",
        label2="Webb",
    )
except Exception as e:
    st.error(t("error_image_load"))

st.markdown(f"### {t('carina_nebula')}")
try:
    image_comparison(
        img1=f"{AZURE_SAS_URI}/datahub/hubble/carina_2800.png{AZURE_SAS_TOKEN}",
        img2=f"{AZURE_SAS_URI}/datahub/webb/carina_2800.jpg{AZURE_SAS_TOKEN}",
        label1="Hubble",
        label2="Webb",
    )
except Exception as e:
    st.error(t("error_image_load"))

st.markdown(f"### {t('stephans_quintet')}")
try:
    image_comparison(
        img1=f"{AZURE_SAS_URI}/datahub/hubble/stephans_quintet_2800.jpg{AZURE_SAS_TOKEN}",
        img2=f"{AZURE_SAS_URI}/datahub/webb/stephans_quintet_2800.jpg{AZURE_SAS_TOKEN}",
        label1="Hubble",
        label2="Webb",
    )
except Exception as e:
    st.error(t("error_image_load"))
