# FinEd - Financial Education

- Domain: [finanz-bildung.com](https://finanz-bildung.com)
- Status: in development

### About the Product
Neither in school nor in adult life do most people receive a comprehensive financial education. I want to make the subject of finance accessible to people in an entertaining way so that they can make sustainable, independent financial decisions.

The first addressed market is Germany, therefore the content of the site was created in German. 

### Technologies
HTML, CSS, Python, Flask

### Deployment
- Server: Google Cloud Server
- Handling requests: NGINX & Gunicorn

### Connected project
This repository is used, to separately develop the landing page of this project:
Repository: https://github.com/tomerror1/fined_lp

### Get it running locally
Required: 
- Python 3.6 (or higher)
- pip (for specific python)

Install the requirements from requirements.txt with pip.

The file run.py is created for running on a server.
To get it run on a local machine, make sure to adapt run.py:
```
from fined_be import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host="0.0.0.0")
```

Inside repository execute run.py with python.
(Example on Windows: python run.py)
