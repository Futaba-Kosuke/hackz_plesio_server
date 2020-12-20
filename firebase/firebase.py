import firebase_admin
from firebase_admin import credentials, firestore


class Firebase:
	def __init__(self, cred_path='firebase/cred.json'):
		cred = credentials.Certificate(cred_path)
		firebase_admin.initialize_app(cred)
		self.db = firestore.client()
