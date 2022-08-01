# from pickle import TRUE
# from flask import Flask
# from flask import send_file
# app = Flask(__name__)
# @app.route("/")
# def mainn():
#     return send_file("index.html")

# @app.route("/page2")
# def page2():
#     return("<h1> hello</h1>")
# app.run(host="localhost", port=80,debug=True)

# import requests
# userdata = {"firstname": "John", "lastname": "Doe", "password": "jdoe123"}
# resp = requests.post('http://localhost/v1/index1.php', params=userdata)
# print(resp)


# from matplotlib.font_manager import json_dump, json_load
# import requests
# import json

# URL = 'http://localhost/v1/index1.php?somekey=ass'
# data = {"somekey": "somevalue"}
# json_data=json.dumps(data)
# # data1=json_load(json_data)
# x= requests.post(url=URL, data=json_data)


# to open/create a new html file in the write mode
f = open('index2.html', 'w')
a="he"
# the html code which will go in the file GFG.html
html_template = f"""<html>
<head>
<title>Title</title>
</head>
<body>
<h2>Welcome To GFG</h2>
  
<p>{a}</p>
  
</body>
</html>
"""
  
# writing the code into the file
f.write(html_template)
  
# close the file
f.close()