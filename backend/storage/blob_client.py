from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

credential = DefaultAzureCredential()

def get_blob_client():
    return BlobServiceClient(
        account_url="https://theoblob.blob.core.windows.net",
        credential=credential
    )
