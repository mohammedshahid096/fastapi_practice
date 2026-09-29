from fastapi import FastAPI,Request
from mockData import products
from dtos import ProductDTO


app = FastAPI()


@app.get("/")
def home():
    return "hello world"

@app.get("/products")
def get_products():
    return products

# path params
@app.get("/products/{product_id}")
def get_one_product(product_id:int):
    for oneProduct in products:
        if(oneProduct.get("id") == product_id):
            return oneProduct
        
    return{
        "message" :"product not found"
    }


# query params
@app.get("/greet")
def greet_user(name:str,age:int):
    return{
        "greet" :f"hello {name}, how are you??",
        "age" : age
    }


# Request
@app.get("/request")
def request_data(req:Request):
    print(req.query_params)
    query_params = dict(req.query_params)
    print(query_params)
    return{
            "greet" :f"hello {query_params.get("name")}, how are you??",
            "age" : query_params.get("age")
        }

## body, headers- request headers, query params,

#pydentic - it helps for for data validation

## different types of HTTP Methods
@app.post("/create_product")
def create_product(body:ProductDTO): ## how to validate data - DTO's (Data Transfer Objects)
    product_data = body.model_dump()
    products.append(product_data)
    return{
        "status" :"Product Created Successfully"
    }


@app.put("/update_product/{product_id}")
def update_product(product_id:int,data:ProductDTO):
    product_data = data.model_dump()
    for index,oneProduct in enumerate(products):
        if(oneProduct.get("id") == product_id):
            products[index] = product_data
            return {
            "stauts" : "product updaed successfully"
           }

    return {
            "message" :"product not found"
        }
    

@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
      for index,oneProduct in enumerate(products):
            if(oneProduct.get("id") == product_id):
                delete_data = products.pop(index)
                return {
                "stauts" : "product delete successfully",
                "data":delete_data
               }
    
      return {
                "message" :"product not found"
            }
    
    
