import uvicorn

if __name__ == "__main__":
    pass
    uvicorn.run("api.api:app", host="0.0.0.0", port=5000, reload=True)
