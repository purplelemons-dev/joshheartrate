import mimetypes

def ext_to_mime(ext):
    """Convert file extension to MIME type."""
    return mimetypes.types_map.get(ext, "application/octet-stream")
