def check_api_key(api_key: str) -> bool:
    """Validate API key (Optional security measure)"""
    VALID_API_KEYS = ["your-secure-api-key"]
    return api_key in VALID_API_KEYS
