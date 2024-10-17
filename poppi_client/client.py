from pymongo import MongoClient
import gridfs
import base64 
import pickle
from retriever import VectorStoreRetriever

class PoppiClient:
    def __init__(self, mongo_uri="mongodb://localhost:27017/poppi-db"):
        #self.api_key = api_key
        self.mongo_client = MongoClient(mongo_uri)
        #self.api_key_manager = APIKeyManager(mongo_uri, "poppi_db")
        self.vectorstore = self.mongo_client['poppi_vectordb'] 
        self.fs = gridfs.GridFSBucket(self.vectorstore, bucket_name="vector-stores")

    def get_vectorstore(self, name):
        # if not self.api_key_manager.validate_api_key(self.api_key):
        #     raise ValueError("Invalid or expired API key")

        vector_store = self.vectorstore['vector-stores.files'].find_one(
            {
                "filename": name
            }
        )

        print('vs ', vector_store)

        if not vector_store:
            raise ValueError(f"Vectorstore with id {name} not found")
        
        try:
            file = self.fs.open_download_stream(vector_store["_id"])
            print('file: ', file)
            data = file.read()
            print('data: ', data)
            decoded_data = base64.b64decode(data)
            #vectorstore_binary = pickle.loads(decoded_data)

            vectorstore = VectorStoreRetriever(decoded_data)
        except Exception as e:
            print(f"Error loading vectorstore: {e}")
            return None  # Return None if the vectorstore cannot be loaded for some reason  # Adjust as necessary  # Replace with appropriate error handling mechanism (e.g., logging)  # Return None for now to avoid breaking the client code  # Add error handling mechanism to handle specific exceptions, such as connection errors or decoding errors, and provide appropriate error messages to the user  # Consider implementing retry logic
    

        if vectorstore:
            return vectorstore
        else:
            raise ValueError(f"Vectorstore with id {name} not found")
        

{
  "files_id": {
    "$oid": "66fc0fe960d6d6c02c23f609"
  },
  "n": 0,
  "data": {
    "$binary": {
      "base64": "U1hoR01vQUJBQUFCQUFBQUFBQUFBQUFBRUFBQUFBQUFBQUFRQUFBQUFBQUJBUUFBQUlBQkFBQUFBQUFBaVVUZXZGbWJ4anlHTy9DOURRK092WkdCVTczTndHSzk5ZDEyUFkvUHVUeE9hQjA5R2JFS3ZieUFrYjNSMElHOTdpNlZQUURtSXJ3MlUwZzlCbVNPdlpDdDdidi9qRUE3SGtrcXZHZXByenZiSWI0OWg0bW52TkQzSmI1N3l0UTgyU3dMdlNTNEpiMkRBZzY2Y29ZcHZNdXcvVDJudHBLOVBVbU92TjlONWowOXJjYzlKN1EvUEFvUkhUMVVnOHM4N3czK1BMTGs5THBLeHdhOVBmMmtQQXNXZ3IzMGRGQzhyNjRnUFdUbHpUeUs3NU04WnVxbE8vbURwcnduaktBOElLZTR2VkVuZkRtWnhoUzlJblo0UGJ0RS96dWlRbUU5V20rRXZmRGlMTDBKZGFJOHpOOTlQRndWK2J4Qy9CKzhPZ29mdlRwbHV6ckc1Tm84VHRpUnZYUFg5THdhcGxBOSttT0J2UjIzcUwyWk01ODh2K3l1UE9rYU1yMWQ4VDY5RUI0N3ZkUlloRDM1cGZjN01LODlPVi9GNDd4YTNnKzlna3NJUFVVMlNqeVM4MVc5WnNrYXZRbU0xanl4amprOXNMWmVQUGJjZXIxbmNCVzlxQzhHUFRMNHh6eTNnR0M4My9pWlBNTk1CajBkcTVFOWthaVlQRktDRlQ0Y3V0bThZdFFXUGFUT01UMitFMFE5L3IvWE81YUhqVHY1aW8wOGdXd3R1MlR3Q0wya1ZCQzl2UjJBdlpHTnB6eG5UbXc5UGFOd1BCUlVwcjFocm5DOFdjR052VFVLdXIyQTg5dTlHT3N4dkNMYzdyMGYyb0c5OEswTnZlY1ZvcnViUWM2OU9RNVZPNnlIQmp3OU4wdTdYVDRRUFRpTU1EMVFaL0M4U2p1ZHZLNXAwQW9uM082OW1TVldQYlVseUx6alZTWThVdERoUEdHSlVMeVAvanU5QjhtZVBHL1l4RHora2JnN1IvTFJPMlcvaHoyYmJRazkwL0RGTzkzbDRUMXRMcVM5R2RUbFBNV0k3N3N1UlhLOFIwSjV2WFJBZFQyeGc4WThESytYdkQ3akRyMG5udlk5V2loTVBCekJMYjM3RDBLOUNtWUl2WDZ4VFR3aTVKTTVUV0hudkNHZmhMeTczZGE5T2pOWVBTWmlrYnhYb3Y4ODAvUUx2Y2hIY0QwR2E4Szk0Z3FKdS9YMmlEME9HSm04YlZVRU9uS3Fwam8zTkt1MkgzTXBQVk82NXoxQ2pCdzkxTTQ3dlkxSEFqM1VvS2M5RUdmYnZHZGYrTHpRamhJOWR2U1d2RzJNU2pzeTJaUThoRlRCdTAvWDhUM2pyMDI5aXFKQlBlSFplajI0RTY2OUVad2x2Y3VsMUx4ejVXczlRK0Izdkp0TTBEd2hVYk05aFphN3ZZZjFSajBXWEwyOFg3bVBQWXcxODczZStaYzg0MTNyUExPS29iellPQlc5ZE1xSVBMbXJpNzExYXdtOHMxdnlQQUNLcDd6SkhrTTh0WlVRdmNPNjk3dFJQVUc5Q1NVYnZURFp6cjBPQSs4OGZBN1R2RXp6blR6VU45RThVVjFWdlV5YTA0cll0dzYrUkFwRFBJZDBNcjJHbjlZOUszZUF2WFh5L0x4Nmg0dzhJL25ydlhHUk16MHFJRGE5YlowZnZhUjhqajB2SzFxNlpreGpQSXhnZTcyaGEvbThaeExEdlFjZjhEeDhOT0E4Z0pQRlBOOFdmandGQlRrOTdpdU52YTIwaGJ5SVhoMDl1MGpHUGVnMWlyMTVBMlU2dS9TWlBaalVOajNIaFlTOUt0UXl2VFlGREQwaWxZKzlVL0YzdklZcTRyMDBqV0k5bSs2RFBTRmIyanpwL0dtODl2NHNQWFovaGIxdGVINDlzVGIyTzd0LytqdHN2Yk04SzIyUHZPY2xHejFMcDRnOG1pcGF2U2VQZ1R6L1NEQTlyVFJUdkU2WHVqd3pTbG84K2p6bHUvcjdoTDI5N3hzOUcvUThQYk1EWDcydlRzNjg3MDkzdlFGWm1EMlRYL2c4RFVrZVBaVnpDYjJhNmRPOWN6ZXd2YjZwL3IyODZQUzg5b2Jadk5jY09Ud2lpQSs4ZHoxRHZKZWlzTDFYeS9PODVUZWlQT1JCN0R1L0pkZzhkcVFuUGI5QWxidUdGTm85dHlyQk85S09rcnpXRzZhOXVTdVdQUTJDSFQyUnorKzgrVklBdldPYmpyelBDb2k5d3gwUlBWMm9pN3lTdDQ0ODBWQ2N2V1g0aGJORS9JTzhibFZZdldwbFFUMnRpM0c5Nk1ERFBEQlE2N3ZrUDZpOXVoNVp2TjkyRFQxK2RITzlGTWs5dkp1alQ3MmdhOUs4T1FDRHZVQ0U4ajBQblNrOXNEc3ZQUStuOUwwRG15SzltdVVNdmVJdlpyMXhjS3E2cGpGQU8vYlpsVHNDUHh5ODNkcEp2SGVGQVR1eGhOYzlOcEJ6UFh4UFZ6M0JZZWM4eGF3YlBWdmNGVDJHdU1JNzBSMkxQYU5HS0R6OGJyVzYrL3ZHUFFrZEF6M1hzeVc5ekRhYXZURmwrcnc2K09lODUrc29QZXRkaUQzTjhzRzhSTTB3dlRtT1NqMmdkSHE5dUJFQ08xTkFCYjM4UWNvODhCdkh1MHMzbmozWURsVzgvYkJuUEFKSnRiMGF5aU85M0dTU1BkbVVuejBoMFRpNzFIVmF2RGRzK0xzTm41WTc=",
      "subType": "00"
    }
  }
}