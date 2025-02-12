from fastapi import APIRouter
from typing import Union, Optional

job = APIRouter()

@job.get('/job/{language}')
def get_jobs(language, degree: Union[str, None] = None, experience: Optional[str] = None):
    return {"language": language, "degree": degree, "experience": experience}