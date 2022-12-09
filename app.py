import flask
from flask_cors import CORS

from views.view_users import urlUser

app = flask.Flask(__name__)
CORS(app)


app.register_blueprint(urlUser, name='Proj')




if __name__ == "__main__":
    app.run(debug=True)

# from geopy.geocoders import Nominatim

# geoLoc = Nominatim(user_agent="GetLoc")
 
# # passing the coordinates
# locname = geoLoc.reverse("46.782818, 23.607418")

# print(locname.address)
# print(type(locname))
