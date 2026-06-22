"""
Translation module for i18n support (English and French)
"""

TRANSLATIONS = {
    "en": {
        "page_title": "Webb Space Telescope vs Hubble Telescope",
        "header": "J. Webb Space Telescope vs Hubble Telescope",
        "intro_line1": "This is the [Streamlit example application](https://github.com/streamlit/example-app-image-comparison) refactored to run on the Federal Science DataHub using images in the FSDH Azure Blob Storage.",
        "intro_line2": "The code for this version can be found on [GitHub](https://github.com/Sean-Stilwell/example-app-image-comparison).",
        "southern_nebula": "Southern Nebula",
        "galaxy_cluster": "Galaxy Cluster SMACS 0723",
        "carina_nebula": "Carina Nebula",
        "stephans_quintet": "Stephan's Quintet",
        "hubble": "Hubble",
        "webb": "Webb",
        "error_sas_token": "Invalid SAS_TOKEN format. Please ensure it is in the format 'https://<storage_account>.blob.core.windows.net/<container>?<sas_token>'.",
        "error_image_load": "This image failed to load. Verify the file exists in the Azure Blob Storage",
        "language": "Français",
    },
    "fr": {
        "page_title": "Télescope Spatial Webb vs Télescope Hubble",
        "header": "Télescope Spatial J. Webb vs Télescope Hubble",
        "intro_line1": "Ceci est l'[application exemple Streamlit](https://github.com/streamlit/example-app-image-comparison) refactorisée pour s'exécuter sur le Federal Science DataHub en utilisant des images du Azure Blob Storage du FSDH.",
        "intro_line2": "Le code de cette version se trouve sur [GitHub](https://github.com/Sean-Stilwell/example-app-image-comparison).",
        "southern_nebula": "Nébuleuse australe",
        "galaxy_cluster": "Amas de galaxies SMACS 0723",
        "carina_nebula": "Nébuleuse de la Carène",
        "stephans_quintet": "Quintette de Stephan",
        "hubble": "Hubble",
        "webb": "Webb",
        "error_sas_token": "Format SAS_TOKEN invalide. Veuillez vous assurer qu'il est au format 'https://<storage_account>.blob.core.windows.net/<container>?<sas_token>'.",
        "error_image_load": "Cette image n'a pas pu être chargée. Vérifiez que le fichier existe dans le Azure Blob Storage",
        "language": "English",
    }
}


def get_text(key: str, language: str = "en") -> str:
    """
    Get translated text for a given key and language.
    
    Args:
        key: Translation key
        language: Language code ("en" or "fr")
    
    Returns:
        Translated text, or the key itself if not found
    """
    if language not in TRANSLATIONS:
        language = "en"
    
    return TRANSLATIONS[language].get(key, key)
