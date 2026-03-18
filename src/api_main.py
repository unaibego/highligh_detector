from fastapi import FastAPI
import uvicorn

import api.endpoints


app = FastAPI()


app.include_router(api.endpoints.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0", port=8000)