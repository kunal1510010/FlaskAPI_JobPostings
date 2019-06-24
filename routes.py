from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify
import pandas as pd

df=pd.read_csv('data.csv')
app = Flask(__name__)
api = Api(app)


a = df.Title.values.tolist()
b = df.Company.values.tolist()
c = df.Experience.values.tolist()
d = df.Location.values.tolist()
e = df.Link.values.tolist()
f = df.Sno.values.tolist()

dic = []
for i,j,k,l,m,n in zip(f,a,b,c,d,e):
   temp = (i,j,k,l,m,n)
   dic.append(temp)
  
   
class Jobs(Resource):
    def get(self):
        keys=('Sno', 'Title', 'Company', 'Experience', 'Location', 'Link')
        result = {'data': [dict(zip(keys,i) ) for i in dic]}
        return jsonify(result)


api.add_resource(Jobs, '/jobs') # Route



if __name__ == '__main__':
     app.run(port='5002')
     
