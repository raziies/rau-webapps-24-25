from flask import Flask, json, request, Response
from datetime import datetime

app = Flask("app")

@app.route("/", methods=["GET"])
def home():
    print("Heloo")
    return "<h1>Welcome to my page</h1>"

@app.route("/version", methods=["GET"])
def version():
    return{
    "version": "1.0.0",
    "requested_at": str(datetime.now())
    }
    
@app.route("/signin", methods=["GET, POST"])
def signin():
    #1. recive data
    print(request)
    body = request.json
    
    #2. validate data
    keys = list(body.keys())
    if not "email" in keys:
        return Response(json.dumps({"error": "Invalid request. Email not sent."}), status=400, headers={"Content-type": "application/json"})
    
    if not "password" in keys:
        return Response (json.dumps({"error": "Invalid request. Email not sent."}), status=400, headers={"Content-type": "application/json"})
        
    #3. check against the stored data
    #4. return response based on the result obtained at 3.
    return Response({}, status=200, headers={"Content-type": "application/json"})


if __name__ == "__main__":
    app.run(debug= True, port = 5001)


