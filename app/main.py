from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from app.services.color_model import predict_personal_color
import logging

# Setup basic logging for MLOps tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Personal Color Recommender API",
    description="MLOps friendly API for personal color recommendation using a lightweight model.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"status": "healthy", "service": "Personal Color API"}

@app.get("/health")
def health_check():
    """Health check endpoint for container orchestration (K8s/Docker)"""
    return {"status": "ok"}

@app.post("/predict")
async def predict_color(file: UploadFile = File(...)):
    """
    Upload an image to get a personal color recommendation.
    """
    if not file.content_type.startswith("image/"):
        logger.warning(f"Invalid file type uploaded: {file.content_type}")
        raise HTTPException(status_code=400, detail="File must be an image.")
    
    try:
        contents = await file.read()
        logger.info(f"Received image for prediction. Size: {len(contents)} bytes")
        
        # Call the inference logic
        result = predict_personal_color(contents)
        
        logger.info(f"Prediction successful: {result['season']}")
        return JSONResponse(content={"success": True, "data": result})
        
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error during prediction.")
