import uuid 

class generete_ID ():
    @classmethod
    def genID(cls) -> str:
        return str(uuid.uuid4())
