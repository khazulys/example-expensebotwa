import re
import json
from google import genai
from config import GEMINI_API_KEY, PROMPT_AI

client = genai.Client(api_key=GEMINI_API_KEY)

def extract_transaksi(pesan):
    prompt = f"{PROMPT_AI}\n\nUser: {pesan}\nJSON:"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    output = response.text.strip()
    output = re.sub(r"^```json", "", output, flags=re.IGNORECASE).strip()
    output = re.sub(r"^```|```$", "", output).strip()
    try:
        transaksi = json.loads(output)
        if isinstance(transaksi, list) and len(transaksi) > 0:
            return transaksi
    except Exception as e:
        print("Parsing JSON gagal:", e)
        print("Output mentah:", output)
    return None

def get_confirmation_message(user_message, transaksi):
    prompt_konfirmasi = f"""
    Kamu adalah Nekkopoi Asisten, AI yang ramah dan membantu.
    Kamu baru saja berhasil mencatat transaksi keuangan dari user berdasarkan pesan mereka.
    Tugasmu sekarang adalah memberikan respon konfirmasi yang singkat, natural, dan ramah.
    Sebutkan detail transaksi yang kamu catat (misal: jumlah dan keterangan) agar user yakin datanya sudah benar.

    Pesan Asli dari User: "{user_message}"
    Data Transaksi yang Berhasil Dicatat: {json.dumps(transaksi, indent=2, ensure_ascii=False)}

    Berikan respon konfirmasi yang sesuai dengan gaya santaimu:
    """
    
    response_konfirmasi = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_konfirmasi
    )
    return response_konfirmasi.text.strip()

def get_general_response(user_message):
    ai_prompt = f"Nekkopoi Asisten, jawab dengan santai:\nUser: {user_message}\nAI:"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=ai_prompt
    )
    return response.text

