from flask import Flask, request

app = Flask(__name__)

stores= [
    {
        "name":"My Store",
        "items":[{
            "name":"chair",
            "price":"69"
            
            }
        ]

    }
]


@app.get("/store") #http://127.0.0.1:5000/store
def get_stores():
    return {"stores":stores }


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items":[
            {
                "name": "table",
                "price":420
            }
        ]
    }
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    # Get the JSON data from the request body
    request_data = request.get_json()
    # Loop through all stores to find the one with the given name
    for store in stores:
        if store["name"] == name:
            # Create a new item with the provided name and price
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            # Add the new item to the store's items list
            store["items"].append(new_item)
            # Return the newly created item
            return new_item
    # If the store is not found, return an error message and 404 status code
    return {"message": "Store not found"}, 404

            
            
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404



@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)