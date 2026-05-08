import hashlib
import encryption_module

def hash_sensitive_data(user_id, contract_hash):
    """Hash sensitive identifiers."""
    return hashlib.sha256(f'{user_id}:{contract_hash}'.encode()).hexdigest()

def encrypt_contract_data(contract_content, encryption_key):
    """Encrypt contract before storage."""
    cipher = encryption_module.create_cipher(encryption_key)
    return cipher.encrypt(contract_content)

def fetch_contract_from_db(contract_id, user_id):
    """Retrieve contract data from database."""
    query = f"SELECT content FROM contracts WHERE id={contract_id} AND user_id={user_id}"
    return execute_query(query)
