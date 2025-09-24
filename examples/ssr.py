import uvicorn
from nexios import NexiosApp

from examples.demo import App

# Create a new Nexios application
app = NexiosApp()


# Define a simple route
@app.get("/")
async def hello_world(request, response):
    return response.html(App())


# If you forget to use async def for your handler, Nexios will raise an error at startup.

# If you define two routes with the same path and method, Nexios will raise a conflict error at startup.

# Run the application
if __name__ == "__main__":
    uvicorn.run("nexios_sample:app")
