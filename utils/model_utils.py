import re
import subprocess
import ollama
from typing import Optional

def get_available_models():
    """
    Get a list of available Ollama model names (without version tags).
    Handles several formats:
      - A dict with a "models" key (older style)
      - A list of objects or dicts
      - Any other type, by converting to string and using regex
    """
    try:
        models_response = ollama.list()
        
        # Case 1: If models_response is a dict with a "models" key
        if isinstance(models_response, dict) and "models" in models_response:
            all_models = models_response["models"]
            # If they are objects with a 'model' attribute
            if all(hasattr(m, "model") for m in all_models):
                return list(set(m.model.split(":")[0] for m in all_models))
            # Else if they are dicts with a "name" key
            elif all(isinstance(m, dict) and "name" in m for m in all_models):
                return list(set(m["name"].split(":")[0] for m in all_models))
        
        # Case 2: If models_response is a list
        if isinstance(models_response, list):
            if all(hasattr(m, "model") for m in models_response):
                return list(set(m.model.split(":")[0] for m in models_response))
            elif all(isinstance(m, dict) and "name" in m for m in models_response):
                return list(set(m["name"].split(":")[0] for m in models_response))
        
        # Case 3: Otherwise, try converting to string and parsing with regex
        models_str = str(models_response)
        raw_names = re.findall(r"Model\(model='([^:]+):", models_str)
        if raw_names:
            return list(set(raw_names))
        else:
            print(f"[Model Detection Error] Unexpected format: {models_response}")
            return []
    except Exception as e:
        print(f"[Model Detection Error] {e}")
        return []

def pull_model(model_name: str):
    """
    Download a model from Ollama.
    """
    try:
        ollama.pull(model_name)
        return True
    except Exception as e:
        print(f"[Model Download Error] {e}")
        return False

def clean_code_response(raw: str) -> str:
    """
    Extract executable Python code from an LLM response (Markdown → code).
    Returns one clean line of code.
    """
    try:
        match = re.findall(r"```(?:python)?(.*?)```", raw, re.DOTALL)
        if match:
            raw = match[0]

        lines = [line.strip() for line in raw.splitlines()
                 if line.strip() and not line.lower().startswith(('here', '#'))]

        for line in lines:
            if "result" in line and "=" in line and not line.startswith(('"', "'")):
                return line

        return lines[0] if lines else "result = pd.DataFrame()"
    except Exception as e:
        return f"result = pd.DataFrame()  # [Error cleaning LLM output] {e}"

def ask_llama_custom(model: str, prompt: str, system: str = "You are a helpful data analyst.") -> str:
    """
    Run an Ollama model with a formatted system + user prompt.
    Uses subprocess to call: ollama run <model> <full_prompt>
    """
    try:
        full_prompt = f"<|system|>\n{system}\n<|user|>\n{prompt}\n<|assistant|>"
        result = subprocess.run(
            ["ollama", "run", model, full_prompt],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout.strip()
    except Exception as e:
        return f"[LLM Error] {e}"

def analyze_with_llama(
    model: str,
    prompt: str,
    context: Optional[str] = None,
    image_path: Optional[str] = None,
    temperature: float = 0.7
):
    """
    Analyze either text (with optional context) or image using a local Ollama model.
    If image_path is provided, appends the image reference to the prompt.
    """
    full_prompt = f"{context}\n\n{prompt}" if context else prompt

    if image_path:
        full_prompt += f"\n[Image: {image_path}]"

    return ask_llama_custom(model, full_prompt)
