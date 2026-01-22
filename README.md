# Z-Angel Generator for ComfyUI
### Absolute Control over Anatomy & Atmosphere

**Z-Angel** is a custom node for ComfyUI designed to act as the "brain" of your prompt engineering. It layers anatomy, skin texture, lighting, and atmospheric physics logic *before* your main prompt, solving the struggle of controlling body types and scene details.

## Features (God Mode)

* **Anatomy Control:** From natural bodies to "Nuclear" high-fashion slender figures (`Slender Force`).
* **Age Engine:** Hard-codes age characteristics from 18 to 90+ years old.
* **Eye Contact:** Control whether the subject ignores the camera or stares into your soul.
* **Wind Physics:** Simulate breeze to hurricane levels directly in the prompt.
* **Atmosphere:** Add dust, leaves, fog, smoke, or sparks with density control.
* **Skin Fidelity:** Choose between "Standard", "Enhanced", or "Extreme" (pores, peach fuzz).

## Installation

### Method 1: Manual
1.  Navigate to your ComfyUI `custom_nodes` folder.
2.  Run `git clone https://github.com/[TUO_USERNAME]/ComfyUI-Z-Angel.git`
    * *Or download the zip, extract it, and rename the folder to `Z-Angel_Node`.*
3.  Restart ComfyUI.

### Method 2: ComfyUI Manager
(Coming soon if you submit it to the registry)

## Usage

1.  **Add Node:** Right-click -> Z-Angel -> `Z-Angel Generator vFinal`.
2.  **Connect:** * Connect your CLIP inputs/outputs.
    * **CRITICAL:** Connect the `negative_prompt` output to your Sampler. The node calculates negative weights automatically based on your slider settings.
3.  **Settings:**
    * Use `Slender Force` carefully. Level 10 is extreme.
    * Use `Seed` to vary micro-details (pores, light direction) while keeping the subject same.

## License
MIT License
