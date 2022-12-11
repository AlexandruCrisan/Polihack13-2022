import flask
from flask_cors import CORS
from geopy.geocoders import Nominatim

from views.view_funcs import urlFuncs
from views.view_homes import urlHomes
from views.view_jobs import urlJobs
from views.view_users import urlUser

app = flask.Flask(__name__)
CORS(app)


app.register_blueprint(urlUser, name='Proj')
app.register_blueprint(urlFuncs, name='Funcs')
app.register_blueprint(urlHomes, name='Homes')
app.register_blueprint(urlJobs, name='Jobs')

print("*****************************************************************************************************************************")

# geolocator = Nominatim(user_agent="geoapiExercises")
# address = geolocator.reverse("46.747350,23.603630")
# address = address.raw["address"]
# print(address)

if __name__ == "__main__":
    app.run(debug=True)

# from geopy.geocoders import Nominatim

# geoLoc = Nominatim(user_agent="GetLoc")
 
# # passing the coordinates
# locname = geoLoc.reverse("46.782818, 23.607418")

# print(locname.address)
# print(type(locname))
