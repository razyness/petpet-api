# petpet-api
A FastAPI app that makes silly petpet gifs

## Install
1. Install the dependencies:
   ```python
   pip install pet-pet-gif fastapi "uvicorn[standard]"
   ```
## Usage
1. RUN `uvicorn main:app --reload`
2. GET `/petpet?image={image url}`

Returns the gif's bytes.
You may also check `/redoc`
