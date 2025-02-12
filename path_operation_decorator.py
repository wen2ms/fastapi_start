from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post('/items',
          tags=['This is the interface of items'],
          summary='Summary',
          description='Description',
          response_description='Response Description')
def items_test():
    return {"items": "data"}

if __name__ == "__main__":
    uvicorn.run('path_operation_decorator:app', reload=True)