# --- Flask Hello World --- #

# import the flask class from the falsk package 

from flask import Flask 

# create the application object 
app = Flask(__name__)

#error handling 
app.config["DEBUG"] = True 

# use the decorator pattern to 
# link the view function to a url 
@app.route("/")
@app.route("/hello")

# define the view usign a function, which returns a string 
def hello_world():
	return "Hello, World!?!?!"

@app.route("/test/<search_query>")
def search(search_query):
	return search_query

# a dynamic route that only accepts integer value
@app.route("/integer/<int:value>")
def int_type(value):
	print(value + 1)
	return "correct"

# a dynamic route that only accepts float value 
@app.route("/float/<float:value>")
def float_type(value):
	print(value + 1)
	return "correct"

# a dynamic route that accepts slashes 
# You can use both integers and floats as well, but they will be converted to unicode
@app.route("/path/<path:value>")
def path_type(value):
	print(value)
	return "correct"

# Here, the route can take an optional parameter of name, and the response object is
#dependent on the assigned value
@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael" :
		return "Hello, {}".format(name)
	else :
		return "Not Found", 404

# start the development server using the run() method 
if __name__ == "__main__":
	app.run()
