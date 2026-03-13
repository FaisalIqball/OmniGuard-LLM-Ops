from fastapi import FastAPI, HTTPException
from .omniguard.guard import OmniGuard

app = FastAPI(title="OmniGuard API")
guard = OmniGuard()

@app.post("/protect")
async def protect(prompt: str):
    clean_prompt = guard.protect_input(prompt)
    return {"clean_prompt": clean_prompt}

@app.post("/validate")
async def validate(prompt: str, response: str):
    is_valid = guard.validate_output(prompt, response)
    if not is_valid:
        raise HTTPException(status_code=400, detail="Potential hallucination detected")
    return {"status": "valid"}
