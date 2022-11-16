



#from config import FIREBASE_API_KEY, FIREBASE_AUTH_DOMAIN, FIREBASE_DATABASE_URL, FIREBASE_STORAGE_BUCKET
from config import FIREBASE_CERTIFICATE
import firebase_admin



from firebase_admin import credentials

cred = credentials.Certificate(FIREBASE_CERTIFICATE)

firebase_admin.initialize_app(cred)


from firebase_admin import firestore

db = firestore.client()



class FirebaseService:


    @staticmethod
    def discord_conf():
        """Return the first element of the DISCORD_CONF collection"""
        coll = db.collection('DISCORD_CONF')
        docs = coll.stream()
        for doc in docs:
            return doc.to_dict()
    

    