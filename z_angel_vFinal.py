import re
import random

class ZAngel_vFinal:
    """
    Z-ANGEL PROTOCOL vFinal (God Mode Extended)
    Features: Anatomy + Age + Wind + Atmosphere + Eye Contact Control
    Filename: z_angel_vFinal.py
    """
    
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                # --- INPUT BASE ---
                "text_input": ("STRING", {"multiline": True, "default": "portrait of a woman"}),
                "subject": ("STRING", {"multiline": False, "default": "beautiful woman"}),
                
                # --- CHAOS ENGINE ---
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),

                # --- ANATOMY CONTROL (Fianchi/Magrezza) ---
                "slender_force": ("INT", {"default": 0, "min": 0, "max": 10, "step": 1, "display": "slider"}),

                # --- NEW: AGE CONTROL ---
                "age_slider": ("INT", {"default": 25, "min": 18, "max": 90, "step": 1, "display": "slider"}),

                # --- NEW: EYE CONTACT (0=Away, 10=Camera) ---
                "eye_contact_force": ("INT", {"default": 10, "min": 0, "max": 10, "step": 1, "display": "slider"}),

                # --- NEW: WIND FORCE ---
                "wind_force": ("INT", {"default": 0, "min": 0, "max": 10, "step": 1, "display": "slider"}),

                # --- NEW: ATMOSPHERE ---
                "atmosphere_type": ([
                    "Off", 
                    "Dust & Dirt (Polvere/Sporco)", 
                    "Flying Leaves (Foglie)", 
                    "Fog / Mist (Nebbia)", 
                    "Smoke (Fumo)",
                    "Sparks / Embers (Scintille)"
                ],),
                "atmosphere_density": ("INT", {"default": 5, "min": 1, "max": 10, "step": 1, "display": "slider"}),

                # --- CONTROLLI PRECEDENTI ---
                "skin_fidelity": ([
                    "Extreme (Raw / Pores)", 
                    "Enhanced (Natural)", 
                    "Standard (Soft)",
                    "Off"
                ],),
                
                "lighting_setup": ([
                    "Natural / Ambient",
                    "Rembrandt (Moody Side Light)",
                    "Butterfly (Beauty / Frontal)",
                    "Split (Dramatic Side)",
                    "Golden Hour (Warm Backlight)",
                    "Cinematic Teal/Orange",
                    "Studio Flash (Hard)",
                    "Volumetric (God Rays)"
                ],),

                "visual_style": ([
                    "Standard / Natural", "Fashion Editorial", "Cinematic", 
                    "Dark / Moody", "Vintage / Analog", "Minimalist"
                ],),
                
                "shooting_intent": ([
                    "Portrait", "Boudoir", "Playboy", "Porno / Hardcore", 
                    "Alessio Albi", "Candid / Street", "Instagram"
                ],),
                
                "film_stock": ([
                    "Digital Sharp", "Kodak Portra 400", "Fujifilm Pro 400H", 
                    "Cinestill 800T", "Ilford HP5 (B&W)"
                ],),
                
                "pose_override": ([
                    "Auto", "Close-up", "Standing", "Sitting", 
                    "Lying Down", "From Behind", "Dynamic"
                ],),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive_prompt", "negative_prompt")
    FUNCTION = "execute_z_angel"
    CATEGORY = "Z-Angel"

    def execute_z_angel(self, text_input, subject, seed, slender_force, age_slider, eye_contact_force, wind_force, atmosphere_type, atmosphere_density, skin_fidelity, lighting_setup, visual_style, shooting_intent, film_stock, pose_override):
        
        rng = random.Random(seed)
        
        # --- 0. ANATOMY CONTROL (PRIORITÀ 1) ---
        anatomy_prefix = ""
        if slender_force > 0:
            if slender_force <= 3: anatomy_prefix = "fit body, athletic build, "
            elif slender_force <= 6: anatomy_prefix = "very slender woman, narrow hips, small buttocks, straight body shape, flat stomach, "
            elif slender_force <= 8: anatomy_prefix = "(narrow hips:1.3), (small ass:1.2), (slim waist:1.2), straight figure, no curves, petite, "
            else: anatomy_prefix = "((extremely slender)), ((boyish figure)), ((narrow pelvis)), ((flat chest)), ((skinny)), ((no hips)), runway model, "

        # --- 1. AGE CONTROL (Modifica il soggetto) ---
        age_desc = ""
        if age_slider < 25: age_desc = f"({age_slider} years old), young, youthful skin"
        elif age_slider < 35: age_desc = f"({age_slider} years old), prime age, detailed skin"
        elif age_slider < 50: age_desc = f"({age_slider} years old), mature woman, milf, sophisticated"
        else: age_desc = f"({age_slider} years old), elderly, wrinkles, aged skin, authentic"
        
        # Uniamo Soggetto + Età
        full_subject = f"Subject is a {age_desc} {subject}"

        # --- 2. EYE CONTACT (Sguardo) ---
        eye_desc = ""
        if eye_contact_force >= 8: eye_desc = "(looking directly at camera:1.4), (eye contact:1.3), staring at viewer"
        elif eye_contact_force >= 5: eye_desc = "looking at camera, relaxed gaze"
        elif eye_contact_force >= 2: eye_desc = "looking away, candid look"
        else: eye_desc = "looking aside, profile shot, ignoring camera, distracted"

        # --- 3. WIND FORCE (Vento) ---
        wind_desc = ""
        if wind_force > 0:
            if wind_force <= 3: wind_desc = "gentle breeze, hair slightly moving"
            elif wind_force <= 6: wind_desc = "wind blowing, windswept hair, moving clothes"
            elif wind_force <= 9: wind_desc = "(strong wind:1.3), (hair flying), chaotic hair, windy atmosphere"
            else: wind_desc = "((hurricane wind)), ((stormy wind)), clothes flying away, extreme wind"

        # --- 4. ATMOSPHERE & PARTICLES ---
        atmo_desc = ""
        if "Off" not in atmosphere_type:
            # Calcolo intensità
            intensity_weight = 1.0 + (atmosphere_density / 20.0) # da 1.05 a 1.5
            density_str = ""
            if atmosphere_density <= 3: density_str = "subtle"
            elif atmosphere_density <= 7: density_str = "heavy"
            else: density_str = "extreme dense"

            if "Dust" in atmosphere_type:
                atmo_desc = f"({density_str} dust in air:{intensity_weight:.1f}), floating dust particles, dirty air, gritty texture"
            elif "Leaves" in atmosphere_type:
                atmo_desc = f"({density_str} flying leaves:{intensity_weight:.1f}), wind blowing leaves, autumn leaves in air, dynamic debris"
            elif "Fog" in atmosphere_type:
                atmo_desc = f"({density_str} fog:{intensity_weight:.1f}), mist, haze, volumetric fog, atmospheric depth"
            elif "Smoke" in atmosphere_type:
                atmo_desc = f"({density_str} smoke:{intensity_weight:.1f}), smoky atmosphere, smog, haze"
            elif "Sparks" in atmosphere_type:
                atmo_desc = f"({density_str} fire sparks:{intensity_weight:.1f}), floating embers, fire particles, bokeh sparks"

        # --- 5. CHAOS & SKIN ---
        dict_skin_details = ["(visible pores:1.1)", "(skin texture details)", "(natural epidermis)", "(authentic skin finish)"]
        rnd_skin = rng.choice(dict_skin_details)
        rnd_imp = rng.choice(["(skin irregularities)", "(micro-details)", "(slight asymmetrical features)"])
        rnd_light = rng.choice(["(perfectly lit)", "(finely illuminated)", "(light shaping)"])

        skin_tokens = ""
        neg_skin = ""
        if "Extreme" in skin_fidelity:
            skin_tokens = f"(hyper-detailed skin:1.2), {rnd_skin}, (peach fuzz), {rnd_imp}, (moles), (veins), (raw photo:1.2)"
            neg_skin = "airbrushed, smooth skin, plastic skin, blur, denoise, makeup, wax"
        elif "Enhanced" in skin_fidelity:
            skin_tokens = f"(realistic skin texture), {rnd_skin}, (natural finish)"
            neg_skin = "plastic, doll, cartoon, smooth"
        elif "Standard" in skin_fidelity:
            skin_tokens = "(smooth but realistic skin), (fashion photography skin)"
            neg_skin = "bad anatomy, cartoon"

        # --- 6. LIGHTING & STYLE ---
        light_map = {
            "Natural / Ambient": "(natural light), (soft shadows)",
            "Rembrandt (Moody Side Light)": "(rembrandt lighting), (chiaroscuro), (triangle of light on cheek), (shadowy)",
            "Butterfly (Beauty / Frontal)": "(butterfly lighting), (paramount lighting), (shadow under nose), (beauty dish)",
            "Split (Dramatic Side)": "(split lighting), (half face in shadow), (high contrast)",
            "Golden Hour (Warm Backlight)": "(golden hour), (warm sun), (backlighting), (lens flare), (rim light)",
            "Cinematic Teal/Orange": "(teal and orange grading), (cinematic lighting), (complementary colors)",
            "Studio Flash (Hard)": "(hard flash), (direct strobe), (sharp shadows), (high key)",
            "Volumetric (God Rays)": "(volumetric lighting), (god rays), (tyndall effect), (foggy atmosphere)"
        }
        var_light = f"{light_map.get(lighting_setup, '')}, {rnd_light}"

        style_tokens = {
            "Fashion Editorial": "(sharp focus), (vogue style)",
            "Cinematic": "(anamorphic lens), (widescreen)",
            "Vintage / Analog": "(film grain), (retro)",
            "Minimalist": "(clean background), (simple)"
        }
        var_style = style_tokens.get(visual_style, "")

        # --- 7. LOGIC GATES ---
        anatomy_base = ""
        if "Portrait" in shooting_intent: anatomy_base = "(detailed eyes), (iris texture), (skin pores on nose)"
        elif "Boudoir" in shooting_intent: anatomy_base = "(soft body texture), (natural skin folds), (goosebumps)"
        elif "Porno" in shooting_intent: anatomy_base = "(raw skin), (sweat), (imperfections), (uncensored)"
        elif "Playboy" in shooting_intent: anatomy_base = "(oiled skin), (perfect body), (tanned)"
        
        # Vestiti
        var_clothes = ""
        is_nsfw = any(x in shooting_intent for x in ["Porno", "Playboy", "Boudoir"])
        if is_nsfw and not any(x in text_input.lower() for x in ["dress", "bikini", "lingerie"]):
            if "Porno" in shooting_intent: var_clothes = "(nude), (naked)"
            elif "Playboy" in shooting_intent: var_clothes = "(lingerie)"
            elif "Boudoir" in shooting_intent: var_clothes = "(silk robe), (partially dressed)"

        # Posa
        var_pose = ""
        if "Auto" not in pose_override:
            clean_pose = pose_override.split("(")[0].strip().lower()
            var_pose = f"({clean_pose}), {eye_desc}, {wind_desc}"
        else:
            var_pose = f"{eye_desc}, {wind_desc}"

        # --- 8. FINAL ASSEMBLY ---
        components = [anatomy_prefix, full_subject, anatomy_base, skin_tokens, var_pose, var_clothes, var_light, atmo_desc, text_input, var_style, film_stock]
        
        final_positive = ", ".join([c for c in components if c])
        
        base_neg = "cartoon, 3d, render, illustration, painting, drawing, anime, cgi, blender, lowres, bad anatomy, blur"
        extra_neg_anatomy = ""
        if slender_force >= 5:
            extra_neg_anatomy = "wide hips, pear shape, big ass, curvy, thick thighs, fat, volumetric"

        final_negative = f"{base_neg}, {extra_neg_anatomy}, {neg_skin}"

        # --- MONITOR ---
        print(f"\n[Z-ANGEL FINAL] Age: {age_slider} | Wind: {wind_force} | Atmo: {atmosphere_type} ({atmosphere_density})")
        
        return {
            "ui": {"text": [final_positive]},
            "result": (final_positive, final_negative)
        }

# --- MAPPATURE NODI ---
# Tutto allineato a ZAngel_vFinal
NODE_CLASS_MAPPINGS = {
    "ZAngel_vFinal": ZAngel_vFinal
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ZAngel_vFinal": "Z-Angel Generator vFinal (God Mode)"
}