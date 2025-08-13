import json
import os
from config import DATA_FILE

def initialize_data_file():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def catat_batch(transaksi_list):
    data = load_data()
    data.extend(transaksi_list)
    save_data(data)

def hitung_saldo():
    data = load_data()
    pemasukan = sum(x["jumlah"] for x in data if x["jenis"] == "pemasukan")
    pengeluaran = sum(x["jumlah"] for x in data if x["jenis"] == "pengeluaran")
    return pemasukan - pengeluaran

def laporan():
    data = load_data()
    teks = "Laporan Keuangan\n"
    for idx, x in enumerate(data, 1):
        teks += f"{idx}. [{x['tanggal']}] {x['jenis']} Rp{x['jumlah']:,} - {x['keterangan']}\n"
    teks += f"\nSaldo saat ini: Rp{hitung_saldo():,}"
    return teks

initialize_data_file()

