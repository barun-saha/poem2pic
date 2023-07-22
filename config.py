from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass(frozen=True)
class Config:
    HUGGINGFACEHUB_API_TOKEN: str = os.getenv('HUGGINGFACEHUB_API_TOKEN')

    # Flan-T5
    LLM_MODEL_NAME: str = 'google/flan-t5-xxl'
    LLM_TEMPERATURE: float = 0.5
    LLM_MAX_OUTPUT_LENGTH: int = 100
    LLM_MAX_INPUT_LENGTH: int = 512

    # Stable Diffusion
    DIFFUSION_MODEL_NAME: str = 'stabilityai/stable-diffusion-2-1'
    DIFFUSION_NUM_INFERENCE_STEPS: int = 3
