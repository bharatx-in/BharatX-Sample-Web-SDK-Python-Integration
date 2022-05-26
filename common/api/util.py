import hashlib
import base64

def generate_signature(payload: str, endpoint: str, private_api_key: str) -> str:
    signature_input = payload + endpoint +  private_api_key
    signature_hash = hashlib.sha256(signature_input.encode("utf-8")).digest()
    return base64.encodebytes(signature_hash).decode("utf-8")


if __name__  == "__main__":
    print("testing signature generation")
    import json

    data = {
        "transactionId": "1234",
        "amount": 1000,
        "userPhoneNumber": "+919840013290"
    }
    endpoint = "/api/transaction"
    private_api_key = "testPrivateKey"

    json_data = json.dumps(data)
    generated_signature = generate_signature(json_data, endpoint, private_api_key)
    print("for payload:")
    print(json_data)
    print("signature: " + generated_signature)
