from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Initialize the FastAPI app
app = FastAPI()

# Configuration settings
class Config:
    PROJECT_NAME = "Deepfake Video Detection"
    VERSION = "1.0"

# Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Adjust this to your allowed origins
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/")
async def root():
    return {"message": "Welcome to the Deepfake Video Detection API!"}