# financial_graph
use python3, bokeh and pandas_datareader to create web base Financial Graph and deploy to heroku

![alt text](https://github.com/smalltide/financial_graph/blob/master/screenshot.png "financial_graph")

1. python3
2. bokeh
3. pandas
4. pandas_datareader
5. flask

```
  > git@github.com:smalltide/financial_graph.git
  > cd financial_graph
  > pip3 install bokeh
  > pip3 install pandas
  > pip3 install pandas_datareader
  > python3 app.py
```

if need virtualenv and deploy to Heroku
```
  > cd financial_graph
  > pip3 install virtualenv
  > python3 -m venv venv
  > venv/bin/pip3 install bokeh
  > venv/bin/pip3 install pandas
  > venv/bin/pip3 install pandas_datareader
  > venv/bin/pip3 install flask
  > venv/bin/python3 web.py
```

if deploy to Heroku
```
  > venv/bin/pip3 install gunicorn
  > venv/bin/pip3 freeze > requirements.txt
  > echo "web: gunicorn web:app" > Procfile
  > echo "python-3.6.0" > runtime.txt
  > heroku login
  > heroku create web-financia
  > heroku git:remote -a web-financia
  > git push heroku master
```
