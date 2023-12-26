# FastAPI-CRUD-PostgreSQL

"FastAPI-CRUD-PostgreSQL with SQLAlchemy is an introduction to building a FastAPI application that performs CRUD operations using the SQLAlchemy ORM with a PostgreSQL database. This project demonstrates the power of FastAPI in combination with the robust data manipulation capabilities provided by SQLAlchemy, offering a seamless and efficient solution for creating, reading, updating, and deleting data in a PostgreSQL database."

## Configurations

- **`Installation FastAPI`**

```
pip install uvicorn fastapi
```

- **`Installation Others`**

```
pip install sqlalchemy 
```
```
pip install pyscopg2
```
```
pip install psycopg2  
```
```
pip install python-dotenv
```

- **`Example`**
  ###### Create a file main.py with:
  
```
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
```

- **`Run it`**

```
uvicorn main:app --reload
```

#  
#### Clone this repository ✅
```md
https://github.com/Pasan-Pahasara/FastAPI-CRUD-PostgreSQL.git
```
###                                              
###### If you think my code is good pleace drop a Star <img src="https://github.com/Pasan-Pahasara/md-alpha/blob/main/star.webp" width="40px">

![GitHub issues](https://img.shields.io/github/issues/Pasan-Pahasara/FastAPI-CRUD-PostgreSQL?&labelColor=black&color=eb3b5a&label=Issues&logo=issues&logoColor=black&style=for-the-badge)
![GitHub Contributions](https://img.shields.io/github/contributors/Pasan-Pahasara/FastAPI-CRUD-PostgreSQL?&labelColor=black&color=8854d0&style=for-the-badge)

### License 📝
[![GitHub license](https://img.shields.io/github/license/Pasan-Pahasara/FastAPI-CRUD-PostgreSQL?&labelColor=black&color=3867d6&style=for-the-badge)](https://github.com/Pasan-Pahasara/FastAPI-CRUD-PostgreSQL/blob/master/LICENSE)

<div align="center">

![repo size](https://img.shields.io/github/repo-size/Pasan-Pahasara/FastAPI-CRUD-PostgreSQL?label=Repo%20Size&style=for-the-badge&labelColor=black&color=20bf6b)
 
![GitHub forks](https://img.shields.io/github/forks/Pasan-Pahasara/FastAPI-CRUD-PostgreSQL?&labelColor=black&color=0fb9b1&style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/Pasan-Pahasara/FastAPI-CRUD-PostgreSQL?&labelColor=black&color=f7b731&style=for-the-badge)
![GitHub LastCommit](https://img.shields.io/github/last-commit/Pasan-Pahasara/FastAPI-CRUD-PostgreSQL?logo=github&labelColor=black&color=d1d8e0&style=for-the-badge)

</div>

<div align="center"> 
If you have any questions or just wanna say hi, <br><b>MAIL ME</b>&nbsp;
  <a href="mailto:pasanpahasara7788@gmail.com">
      <img width="20px" src="https://github.com/Pasan-Pahasara/md-alpha/blob/main/gmail.svg" />
  </a></p>
 
 </div>

