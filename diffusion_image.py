import PIL.Image
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch

from config import Config


torch.set_grad_enabled(False)

dpm = DPMSolverMultistepScheduler.from_pretrained(Config.DIFFUSION_MODEL_NAME, subfolder='scheduler')
pipeline = StableDiffusionPipeline.from_pretrained(Config.DIFFUSION_MODEL_NAME, scheduler=dpm)
# pipeline.enable_xformers_memory_efficient_attention()


def generate_image_from_text(text: str) -> PIL.Image.Image:
    """
    Generate an image based on the input text.

    :param text: The text
    :return: An image instance
    """

    with torch.inference_mode():
        output_img = pipeline(
            text,
            num_inference_steps=Config.DIFFUSION_NUM_INFERENCE_STEPS).images[0]
        print(output_img)

        return output_img
