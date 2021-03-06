from .client import ZengaPayAPI
from .utils import validate_number, validate_phone_number, validate_string


class Collections(ZengaPayAPI):
    def collect(self, payload):
        payload["msisdn"] = validate_phone_number(payload.get("msisdn"))
        payload["amount"] = validate_number(payload.get("amount"))
        payload["external_reference"] = validate_string(
            payload.get("external_reference")
        )
        payload["narration"] = validate_string(payload.get("narration"))

        url = f"{self.config.base_url}/collections"
        res = self.request("POST", url, post_data=payload)

        return res.json()

    def get_all_collections(self, url=None):
        if url is None:
            url = f"{self.config.base_url}/collections"
        res = self.request("GET", url)

        return res.json()

    def get_collection(self, transaction_ref):
        url = f"{self.config.base_url}/collections/{validate_string(transaction_ref)}"
        res = self.request("GET", url)

        return res.json()

    def get_transaction_status(self, transaction_ref):
        url = f"{self.config.base_url}/collections/{validate_string(transaction_ref)}"
        res = self.request("GET", url)

        return res.json()["data"]["transactionStatus"]
