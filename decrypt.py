import sys
import io
import re

ENCRYPTED_CODE = """
"""

def decrypt():
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    local_vars = {}
    
    try:
        exec(ENCRYPTED_CODE, {}, local_vars)
        for key, value in local_vars.items():
            if isinstance(value, str) and len(value) > 100:
                print(f"Decrypted code in variable: {key}")
                print("="*50)
                print(value[:2000])
                print("="*50)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sys.stdout = old_stdout

decrypt()

