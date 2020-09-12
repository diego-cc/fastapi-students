# FastAPI-Students
This is a REST API that can be used to manage student records, implemented using FastAPI and MariaDB

## Instructions
### Clone the project
```bash
git clone https://github.com/diego-cc/fastapi-students.git
```
### Create a database
Run the commands below to create a database and user for this project:
```sql
CREATE DATABASE fastapi_students CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_general_ci';
CREATE USER 'students_admin'@'localhost' IDENTIFIED BY 'Password1';
GRANT ALL PRIVILEGES ON fastapi_students.* TO 'students_admin'@'localhost';
FLUSH PRIVILEGES;
```

### Create a virtual environment
If you are using Anaconda on Windows, open your Anaconda Navigator and create a new virtual environment called __fastapi-students__. 

Then, follow the steps below to install the required packages:
1. Open Anaconda Prompt
2. Navigate to your project folder
3. Switch your virtual environment to __fastapi-students__ by running this command: `conda activate fastapi-students`
4. Install packages:
```
conda install -c conda-forge fastapi
conda install -c conda-forge sqlalchemy
conda install -c conda-forge uvicorn
conda install -c conda-forge pymysql
conda install -c conda-forge pytest
```

### Run the application
From your Anaconda Prompt (with your __fastapi-students__ environment activated), run the command below from the project root directory (one level above the `app` directory):

```bash
uvicorn app.main:app --reload
```

You may now navigate to http://localhost:8000/docs to test the routes available.
