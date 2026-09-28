# A simple project of books using crud operations
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
books=[]

class  Book(BaseModel):
    id:int
    price:int
    author:str
@app.post("/books")
def book_entry(book:Book):#creating an entry
    books.append(book)
    return{
        "message":"new book added ",
        "new book":book
    }
@app.get("/books") #to take all data into once 
def books_data():
    return books

@app.get("/books/{book_id}") #to find a specific book's data by entering id
def specific_book(book_id:int):
    for kitaab in books:
        if kitaab.id==book_id:
            return kitaab
    return{
        "not found"
    }   
@app.put("/books/{book_id}")#to update a specific book's data by entering id
def update_book_data(book_id:int,updated:Book):
    for index,kitaab in enumerate(books):
        if kitaab.id==book_id:
            books[index]=updated
            return{
                "message":"data updated",
                "updated":updated
            }
    return{
        "message":"not found"
    }

@app.delete("/books/{book_id}")#to delete a specific book  by entering id
def Delete_book(book_id:int):
    for idx,gyaan in enumerate(books):
        if gyaan.id==book_id:
            books.pop(idx)
            return {
                "mesagae":"book deleted"
            }
    return{
        "not found"
    }
        
