from datetime import datetime
from uuid import uuid4


def place_image_upload_path(instance, filename):
    ext = filename.split(".")[-1]
    # Genera nombre único
    new_filename = f"{uuid4().hex}.{ext}"
    # Organiza por fecha actual: YYYY/MM/DD
    today = datetime.now()
    return f"places/covers/{today.strftime('%Y/%m/%d')}/{new_filename}"
