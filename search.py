from encrypt import decrypt
from keyword_index import hash_keyword
from access_control import check_access
from database import retrieve_data

def search_keyword(user, keyword):
    if check_access(user, keyword):
        keyword_hash = hash_keyword(keyword)
        encrypted_data = retrieve_data(keyword_hash)
        return decrypt(encrypted_data) if encrypted_data else "No data found."
    return "Access denied."
