import re

def is_valid_uri(uri):
    """
    Validates if the MongoDB URI is in the correct format.
    
    Args:
        uri (str): MongoDB connection URI
        
    Returns:
        bool: True if URI matches the pattern, False otherwise
    """
    pattern = r"^mongodb(\+srv)?:\/\/.*"  # ✅ Aceita mongodb:// ou mongodb+srv://
    return bool(re.match(pattern, uri))