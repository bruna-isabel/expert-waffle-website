from waffle import app
#Allows to run module directly instead of using flask run
#Whenever we shut down terminal, we don't have to set
# environment variables again 
if __name__ == '__main__':
    app.run(debug=True)