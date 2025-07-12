from .image_pin import ImagePin

WEB_DIRECTORY = "js"

NODE_CLASS_MAPPINGS = {
    "ImagePin": ImagePin
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImagePin": "Image PinNode (Embed image b64 to workflow)"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']