from fastapi import FastAPI, File, UploadFile
from predictor import DepthEstimationModel
import os
import uuid
from upload import upload_image_to_imgbb

app = FastAPI()
depth_estimator = DepthEstimationModel()

ALLOWED_EXTENSIONS = {".jpg", ".png", ".jpeg"}
TEMP_FOLDER = "api_images"
os.makedirs(TEMP_FOLDER, exist_ok=True)


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        file_extension = os.path.splitext(file.filename)[1]
        if file_extension not in ALLOWED_EXTENSIONS:
            return {
                "error": "Uploaded file must be an image with extension .jpg, .jpeg or .png"
            }
        filename_base = str(uuid.uuid4())
        filename = filename_base + file_extension
        destination_path = os.path.join(TEMP_FOLDER, filename)
        output_path = os.path.join(TEMP_FOLDER, "output" + filename_base + ".png")
        with open(destination_path, "wb") as image_data:
            image_data.write(file.file.read())

        depth_estimator.calculate_depth_map(destination_path, output_path)
        response = upload_image_to_imgbb(output_path)
        return response
    except Exception as e:
        return {"error": str(e)}
