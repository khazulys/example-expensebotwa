import asyncio
from pywabot import PyWaBot
import config
import data_manager
import gemini_client

bot = PyWaBot(session_name=config.SESSION_NAME, api_key=config.PYWABOT_API_KEY)

@bot.on_message
async def handle_message(message):
    if message.from_me:
        return
        
    teks = message.text.strip().lower()

    if teks == "/saldo":
        saldo = data_manager.hitung_saldo()
        await bot.send_message(message.chat, f"Saldo saat ini: Rp{saldo:,}", reply_chat=message)
        return
        
    if teks == "/laporan":
        laporan_text = data_manager.laporan()
        await bot.send_message(message.chat, laporan_text, reply_chat=message)
        return

    transaksi = gemini_client.extract_transaksi(message.text)

    if transaksi:
        data_manager.catat_batch(transaksi)
        jawaban_ai = gemini_client.get_confirmation_message(message.text, transaksi)
        await bot.send_message(message.chat, jawaban_ai, reply_chat=message)
        return

    jawaban_ai = gemini_client.get_general_response(message.text)
    await bot.send_message(message.chat, jawaban_ai, reply_chat=message)

async def main():
    try:
        if not await bot.connect():
            phone_number = int(input("Enter your phone number (e.g., 628): "))
            code = await bot.request_pairing_code(phone_number)
            if code:
                print(f"Your pairing code: {code}")
                print("Waiting for connection after pairing...")
                if await bot.wait_for_connection(timeout=120):
                    print("Bot connected successfully!")
                    await bot.start_listening()
                else:
                    print("Connection timeout after pairing.")
            else:
                print("Failed to request pairing code.")
        else:
            print("bot ready to incomming message!")
            await bot.start_listening()
    except KeyboardInterrupt:
        print("Bot stopped by user.")

if __name__=="__main__":
    data_manager.initialize_data_file()
    asyncio.run(main())