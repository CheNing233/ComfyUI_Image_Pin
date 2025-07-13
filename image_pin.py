import torch
import numpy as np
from PIL import Image, ImageOps
import base64
from io import BytesIO
import folder_paths
import os


class ImagePin:
    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [
            f
            for f in os.listdir(input_dir)
            if os.path.isfile(os.path.join(input_dir, f))
        ]
        return {
            "required": {
                "image": (sorted(files) + ["#DECODE_FROM_BASE64"], {"image_upload": True}),
                "image_data": ("STRING", {"multiline": False}),
            },
        }

    CATEGORY = "utils"

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "load_image"

    def load_image(self, image, image_data):
        if image_data.startswith('data:image/webp;base64,'):
            image_data = base64.b64decode(image_data.split(",")[1])
        else:
            image_data = base64.b64decode(image_data.split(",")[1])

        i = Image.open(BytesIO(image_data))
        i = ImageOps.exif_transpose(i)
        image = i.convert("RGB")
        image = np.array(image).astype(np.float32) / 255.0
        image = torch.from_numpy(image)[None,]
        return (image,)

    @classmethod
    def VALIDATE_INPUTS(cls, image, image_data):
        if image_data is None:
            return "image_data is required"

        return True
