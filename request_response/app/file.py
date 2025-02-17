from fastapi import APIRouter, File, UploadFile
import os

file = APIRouter()

@file.post('/file')
async def get_file(file: bytes = File()):
    return {"file_length": len(file)}

@file.post('/files')
async def get_files(files: list[bytes] = File()):
    return {"files_number": len(files)}

@file.post('/upload_file')
async def upload_file(file: UploadFile):
    outfile_path = os.path.join('upload_files', file.filename)

    with open(outfile_path, 'wb') as outfile:
        outfile.write(file.file.read())

    return {"file_name": file.filename}

@file.post('/upload_files')
async def upload_files(files: list[UploadFile]):
    names_of_files = [file.filename for file in files]

    return {"names_of_files": names_of_files}