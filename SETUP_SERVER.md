## Install and setup nginx

sudo apt update

sudo apt install nginx -y

sudo vi /etc/nginx/sites-available/cprof_flask

```
server {
    listen 80;
    server_name cprofiler.org www.cprofiler.org 35.224.246.109;
 
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

sudo ln -s /etc/nginx/sites-available/cprof_flask /etc/nginx/sites-enabled/

sudo nginx -t

sudo systemctl restart nginx


## Install python and flask

sudo apt install python3 python3-pip python3-pipx -y

sudo apt install python3-flask python3-gunicorn -y   

sudo apt install python3-numpy python3-pandas python3-matplotlib -y


### Setup flask app

mkdir ~/cprof_flask

cd ~/cprof_flask

vi cprof_flask.py

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Testing, testing, 1, 2, 3."

if __name__ == "__main__":
    app.run()
```

### Test flask app

python3 cprof_flask.py


## Install and run gunicorn

sudo apt install gunicorn -y

gunicorn -w 4 -b 127.0.0.1:8000 cprof_flask:app
