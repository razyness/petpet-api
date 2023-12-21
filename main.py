from fastapi import FastAPI, HTTPException, Query
from io import BytesIO
from PIL import Image
import requests
import tempfile
from petpetgif import petpet
from starlette.responses import StreamingResponse

app = FastAPI()

@app.get("/petpet/")
async def pet(image: str = Query(..., description="URL of the image to petpet")):
    try:
        response = requests.get(image)
        response.raise_for_status()

        image = Image.open(BytesIO(response.content))

        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
            image.save(temp_file.name, format="PNG")

        dest = BytesIO()
        petpet.make(temp_file.name, dest)
        dest.seek(0)

        return StreamingResponse(dest, media_type="image/gif")
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    finally:
        temp_file.close()
