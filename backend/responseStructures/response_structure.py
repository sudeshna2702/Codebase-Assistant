from pydantic import BaseModel

class testResponse(BaseModel):
    message : str


class folderRequest(BaseModel):
    folder_path: str
