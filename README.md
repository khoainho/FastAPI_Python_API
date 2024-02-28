# NewJeans API 
## Description

This is a Python API with full CRUD routes for NewJeans member's data.

<img src="images/newjeans.png">

### Technologies 
* Python
* FastAPI
* Uvicorn
* UUID
* Pydantic

## Setup Instructions
1. Clone the repository to your local machine
2. CD into the project folder and run the command to install all of the necessary packages
```python
pip3 install fastapi "uvicorn[standard]"
```
4. Run the command to run the API on your local machine
```python
uvicorn main:app --reload
```
6. Open Postman or the browser of your choice and go to to get started
```python
http://localhost:8000/members
```
