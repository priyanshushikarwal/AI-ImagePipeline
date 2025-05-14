from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
).to("cuda")

prompt =     """A sleek black Ford Endeavour SUV, highly detailed, glossy finish, parked on a scenic mountain road "
    "during golden hour, ultra-realistic, 8k, volumetric lighting, professional DSLR photo style, "
    "reflections, rich contrast, vibrant colors"""
image = pipe(prompt).images[0]

image.save("ford_scenic.jpg")
