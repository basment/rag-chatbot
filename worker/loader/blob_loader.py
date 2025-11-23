from backend.storage.blob_client import get_blob_client

def load_blobs_from_container(container_name: str):
    try:
        blob_service = get_blob_client()
        container_client = blob_service.get_container_client(container_name)

        blobs = container_client.list_blobs()

        return blobs
    except Exception as e:
        print(f"ERROR accessing blob storage: {str(e)}")