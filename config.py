import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PYWABOT_API_KEY = os.getenv("PYWABOT_API_KEY")
SESSION_NAME = "whatsapp_sessions"
DATA_FILE = "data/data.json"

PROMPT_AI = """
Kamu adalah Nekkopoi Asisten, AI yang membantu mencatat keuangan user.
Jika pesan user mengandung pemasukan atau pengeluaran, ekstrak semua data dalam bentuk JSON dengan format:
[
  {"tanggal": "YYYY-MM-DD", "jenis": "pemasukan/pengeluaran", "jumlah": <angka dalam rupiah>, "keterangan": "string"}
]
Gunakan tanggal hari ini jika tidak disebutkan.
Jangan tambahkan teks lain selain JSON valid. Jangan gunakan markdown atau tanda ``` .
"""
