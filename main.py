from contextlib import contextmanager
import json

#Constants
FILENAME = 'contacts.json'
FILEPATH = '/'

@contextmanager
def file_open(path, mode):
    try:
        f = open(path, mode)
        print("Working with file started")
        try:
            yield f
        finally:
            print("Closing file in progress")
            f.close()
        print("File closed")
    except Exception as e:
        print(f"Error while openning file '{path}: '{e}'")
        raise


def get_data_from_file(path):
    try:
        with file_open(path, 'r') as f:
            data = json.load(f)
            contact_id = data.get('contact_id', {})
            contacts = data.get('contacts', {})
            last_id = data.get('last_id', 0)
            return contact_id, contacts, last_id
    except json.JSONDecodeError:
        print("File json incorrect")
        return {}, {}, 0
    except Exception as e:
        print(f"Pls check error: '{e}'")
        return {}, {}, 0



def find_by_phone(phone, contacts_id, contacts):
    if not (contact_key := contacts_id.get(phone)):
        print("Contact not found")
        return
    
    contact_letter = contact_key[0]

    if contact := contacts.get(contact_letter, {}).get(contact_key):
        print(contact)


def find_by_field(field, contacts):
    