import os
from app import create_app

config_name = os.getenv('APP_SETTINGS')
app = create_app('config_name')

if __name__ == '__main__':
    # app.run(debug=True) #Could this line be causing issues in Heroku? Lets see if running in production mode resolves it
    app.run()