Create a resource `/items` that allows for basic CRUD operations (Create, Read, Update, Delete).
Items can be stored in memory, no need to use a database.

## Requirements
- A POST request to `/items` should create a new item.
- A GET request to `/items` should return a list of all items.
- A GET request to `/items/:id` should return the item with the specified ID.
- A PUT request to `/items/:id` should update the item with the specified ID.
- A DELETE request to `/items/:id` should delete the item with the specified ID.

Items should have the following properties:
- id: string
- name: string
- created_at: datetime
- updated_at: datetime

Endpoints should return appropriate status codes:
- 200 for POST
- 200 for GET/PUT/DELETE
- 404 for not found