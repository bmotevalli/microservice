from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI()

@app.get("api/2/healthcheck")
async def healthcheck():
    return {"message": "Hello from API2"}

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",  # Path to the OpenAPI schema
        title="FastAPI - Swagger UI"
    )

@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return JSONResponse(
        get_openapi(
            title="FastAPI - API 2",
            version="1.0.0",
            description="This is a simple 'Test' API. No 2."
        )
    )
