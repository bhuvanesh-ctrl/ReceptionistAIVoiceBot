import httpx

try:
    client = httpx.Client(base_url="http://localhost:9090")
    response = client.get("/")
    if response.status_code == 200:
        print("Connection successful! Server is responding.")
    else:
        print(f"Unexpected response status: {response.status_code}")
except httpx.RequestError as e:
    print(f"Connection error: {e}")
