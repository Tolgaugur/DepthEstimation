import torch
from misc import colorize
from PIL import Image


class DepthEstimationModel:
    def __init__(self) -> None:
        self.device = self._get_device()
        self.model = self._init_model(
            model_repo="isl-org/ZoeDepth", model_name="ZoeD_N"
        ).to(self.device)

    def _get_device(self):
        return "cuda" if torch.cuda.is_available() else "cpu"

    def _init_model(self, model_repo="isl-org/ZoeDepth", model_name="ZoeD_N"):
        torch.hub.help("intel-isl/MiDaS", "DPT_BEiT_L_384", force_reload=True)
        model = torch.hub.load(
            model_repo, model_name, pretrained=True, skip_validation=False
        )
        model.eval()
        print("Model initialized")
        return model

    def save_colored_depth(self, depth_numpy, output_path):
        colorized_depth = colorize(depth_numpy)
        Image.fromarray(colorized_depth).save(output_path)
        print(f"Colorized depth map saved at {output_path}")

    def calculate_depth_map(self, image_path, output_path):
        image = Image.open(image_path).convert("RGB")
        print(f"Image loaded from {image_path}")
        depth_numpy = self.model.infer_pil(image)
        self.save_colored_depth(depth_numpy, output_path)
        return f"Colorized depth map saved at {output_path}"


model = DepthEstimationModel()
model.calculate_depth_map("image.png", "output.png")
