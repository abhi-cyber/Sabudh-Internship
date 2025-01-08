from fastapi import FastAPI, HTTPException  # Import FastAPI for creating the app and HTTPException for error handling
from pydantic import BaseModel  # Import BaseModel from Pydantic to define data models with validation

# Initialize the FastAPI app
app = FastAPI()

# Define the TodoItem model
class TodoItem(BaseModel):
    id: int  # Use an integer ID for the todo item
    title: str  # Title of the todo item, must be a string
    description: str  # Description of the todo item, must be a string and is required
    completed: bool = False  # Completed status of the todo item, defaults to False

# In-memory storage for the todo items
todo_items = []  # List to hold all todo items

# API endpoint to create a new todo item
@app.post("/todos/")
async def create_todo_item(todo_item: TodoItem):
    """
    Create a new todo item.

    Parameters:
    - todo_item: The TodoItem object containing title, description, and completed status.

    Returns:
    - The created TodoItem object with an assigned ID.
    """
    todo_items.append(todo_item)  # Add the new todo item to the list
    return todo_item  # Return the created todo item

# API endpoint to retrieve all todo items
@app.get("/todos/")
async def get_todo_items():
    """
    Retrieve all todo items.

    Returns:
    - A list of all TodoItem objects.
    """
    return todo_items  # Return the list of all todo items

# API endpoint to retrieve a single todo item by ID
@app.get("/todos/{todo_id}")
async def get_todo_item(todo_id: int):
    """
    Retrieve a single todo item by its ID.

    Parameters:
    - todo_id: The ID of the todo item to retrieve.

    Returns:
    - The TodoItem object with the specified ID.
    
    Raises:
    - HTTPException: If the todo item is not found (404).
    """
    # Find the todo item by its ID
    for item in todo_items:
        if item.id == todo_id:
            return item  # Return the found todo item
    raise HTTPException(status_code=404, detail="Todo item not found")  # Raise a 404 error if not found

# API endpoint to update a todo item by ID
@app.put("/todos/{todo_id}")
async def update_todo_item(todo_id: int, updated_item: TodoItem):
    """
    Update an existing todo item by its ID.

    Parameters:
    - todo_id: The ID of the todo item to update.
    - updated_item: The updated TodoItem object containing title, description, and completed status.

    Returns:
    - The updated TodoItem object.
    
    Raises:
    - HTTPException: If the todo item is not found (404).
    """
    # Find the todo item by its ID
    for index, item in enumerate(todo_items):
        if item.id == todo_id:
            updated_item.id = todo_id  # Keep the original ID for the updated item
            todo_items[index] = updated_item  # Update the item in the list
            return updated_item  # Return the updated todo item
    raise HTTPException(status_code=404, detail="Todo item not found")  # Raise a 404 error if not found

# API endpoint to delete a todo item by ID
@app.delete("/todos/{todo_id}")
async def delete_todo_item(todo_id: int):
    """
    Delete a todo item by its ID.

    Parameters:
    - todo_id: The ID of the todo item to delete.

    Returns:
    - The deleted TodoItem object.
    
    Raises:
    - HTTPException: If the todo item is not found (404).
    """
    # Find the todo item by its ID
    for index, item in enumerate(todo_items):
        if item.id == todo_id:
            return todo_items.pop(index)  # Remove and return the deleted todo item
    raise HTTPException(status_code=404, detail="Todo item not found")  # Raise a 404 error if not found

# Entry point to run the application
if __name__ == "__main__":
    import uvicorn  # Import uvicorn for running the FastAPI app
    uvicorn.run(app, host="127.0.0.1", port=8000)  # Run the app on localhost at port 8000

# You can see all the endpoints by visiting: http://127.0.0.1:8000/docs



'''
uvicorn main:app --reload

uvicorn: This is the ASGI server that will run your FastAPI application.
main:app: This tells Uvicorn to look for the app instance in the main module (the main.py file).
--reload: This enables auto-reload, meaning the server will automatically restart whenever you make changes to your code. This is very useful during development.
'''
