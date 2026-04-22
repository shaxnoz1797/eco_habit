import json
from solana.rpc.api import Client
from solders.keypair import Keypair
from solders.pubkey import Pubkey
# Transactionni solders kutubxonasidan olamiz, bu xatolikni oldini oladi
from solders.transaction import Transaction
from solders.system_program import transfer, TransferParams

# Solana Devnet tarmog'iga ulanish
SOLANA_CLIENT = Client("https://api.devnet.solana.com")

def log_habit_on_chain(habit_name):
    try:
        # Demo uchun yangi hamyon
        sender = Keypair()
        receiver = Pubkey.from_string("11111111111111111111111111111111")

        # Blockchain qaydi simulyatsiyasi
        return {
            "status": "Success",
            "transaction_id": "5H6j" + habit_name[:3] + "demo7K2p",
            "network": "Solana Devnet",
            "memo": f"EcoHabit: {habit_name} verified"
        }
    except Exception as e:
        return {"status": "Error", "message": str(e)}