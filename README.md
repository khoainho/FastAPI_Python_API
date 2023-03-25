# NewJeans API 
## Description
This is a Python API with full CRUD routes for storing NewJeans members' information.

<img src="images/newjeans.png">

### Technologies 
* Python
* FastAPI
* Uvicorn
* UUID
* Pydantic

## Setup Instructions
1. Clone repository to your local machine using SSH key
2. CD into project folder and run the command ```pip3 install fastapi "uvicorn[standard]"``` to isntall all of the necessary packages
3. Run the command ```uvicorn main:app --reload``` to run the API on your local machine
4. Open Postman or browser of your choice and go to ```http://localhost:8000/members``` to get started
