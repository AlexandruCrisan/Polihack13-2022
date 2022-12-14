import datetime
import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import geopy.distance
from dotenv import load_dotenv
from flask import Blueprint, request
from geopy.geocoders import Nominatim
from googleplaces import GooglePlaces, types
from newsapi import NewsApiClient

import utils as ut
from database_ops.db_cash_bank import DB_CASH_BANK
from database_ops.db_homes import DB_HOMES
from database_ops.db_jobs import DB_JOBS
from database_ops.db_users import DB_USERS

urlFuncs = Blueprint('views', __name__)

load_dotenv()

MAPS_API_KEY = os.getenv("MAPS_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

google_places = GooglePlaces(MAPS_API_KEY)

homes_table = DB_HOMES()
bank_table = DB_CASH_BANK()
users_table = DB_USERS()
jobs_table = DB_JOBS()

newsApi = NewsApiClient(api_key=NEWS_API_KEY)

contact_mail = 'calex2005cj@gmail.com'
contact_mail2 = 'adrian.iurian1@gmail.com'
# contact_mail2 = 'calex2005cj@gmail.com'
contact_password = 'vgvtmmgaafazrnfn'

def respects_filters(home, filters):
  try:
    home_JSON = homes_table.get_home(home["id"])
    if filters["max_residents"] < home_JSON["max_residents"]:
      return False
  except Exception:
    return True

  return True



########################################################## Nearby Hospitals
@urlFuncs.route('/nearby_hospitals', methods=['GET'])
def getHospitals():
  lat = request.args.get("lat")
  lng = request.args.get("lng")
  radius = int(request.args.get("radius"))

  query_result = google_places.nearby_search(
        # lat_lng ={'lat': 46.1667, 'lng': -1.15},
        lat_lng ={'lat': lat, 'lng': lng},
        radius = radius,
        types =[types.TYPE_HOSPITAL])

  response = []
  for place in query_result.places:
    response.append( {"name": place.name, "coords":{"lat":float(place.geo_location['lat']), "lng": float(place.geo_location['lng'])}} )
  return response

########################################################## Nearby Homes

@urlFuncs.route('/nearby_homes', methods=['GET'])
def getHomes():
  lat = request.args.get("lat")
  lng = request.args.get("lng")
  radius = int(request.args.get("radius"))
  
  min_residents = request.args.get("min_residents")

  all_homes = homes_table.get_all_homes()
  response = []
  for home in all_homes:
    print(home)
    c1 = (float(lat), float(lng))
    c2 = (float(home["location"]["lat"]), float(home["location"]["lng"]))

    distance = geopy.distance.geodesic(c1, c2).km 
    print(f"{home['id']} -> {distance}")
    if distance <= radius and int(min_residents) <= int(home["max_residents"]):
      home["distance"] = float(int(distance*100) / 100)

      without_comma = home["street_name"].replace(',', '')
      home["google_maps"] = f"https://www.google.com/maps/place/{without_comma.replace(' ', '+')}/@{str(home['location']['lat'])},{str(home['location']['lng'])}"

      response.append(home)

  return response

########################################################## Request Donations
@urlFuncs.route('/donations/money', methods=['GET'])
def getDonationMoney():
  refugee_username = request.args.get("username")
  cash_sum = request.args.get("sum")
  
  return bank_table.extract_funds(refugee_username, cash_sum)

@urlFuncs.route('/donations/money', methods=['POST'])
def sendDonationMoney():
  donation = request.args.get("donation")
  
  return bank_table.add_funds(int(donation))
  

@urlFuncs.route('/donations/food', methods=['GET'])
def getDonationFood():
  refugee_username = request.args.get("username")
  return refugee_username

@urlFuncs.route('/donations/clothes', methods=['GET'])
def getDonationClothes():
  refugee_username = request.args.get("username")
  return refugee_username


########################################################## Scrape News

@urlFuncs.route('/war_news', methods=['GET'])
def getWarNews():
  previous_date = datetime.date.today() - datetime.timedelta(days=7)

  news_dict = newsApi.get_everything(language='en', q="ukraine", from_param=previous_date, page_size=100)

  nonYouTubeArticles = ut.getNonYouTube(news_dict)
  # ut.removeSourceFromName(nonYouTubeArticles)
  ut.removeCharsNumber(nonYouTubeArticles)
  ut.removeUnicodeChars(nonYouTubeArticles)

  return nonYouTubeArticles

########################################################## SOS Email

@urlFuncs.route('/sos', methods=['POST'])
def sendSOS():
  email_type = request.args.get("type")
  lat = request.args.get("lat")
  lng = request.args.get("lng")

  username = request.args.get("username")

  geoLoc = Nominatim(user_agent="GetLoc")
  locname = geoLoc.reverse(f"{lat}, {lng}")

  # print(locname.address)

  if email_type == 1:
    user_json = users_table.get_user(username)

    mail = MIMEMultipart("alternative")
    mail['Subject'] = f"{user_json['name']} ({username}) issued SOS feature"
    mail['From'] = contact_mail
    mail['To'] = contact_mail2

    message = f"Last known location: {locname}"
#   Category: {dataJSON["category"]}

    mail.attach(MIMEText(message))

    mailer = smtplib.SMTP('smtp.gmail.com',587)
    mailer.starttls()
    mailer.login(contact_mail, contact_password)
    mailer.sendmail(contact_mail, contact_mail2, mail.as_string())
    mailer.quit()
    return ('ok', 200)

  user_json = users_table.get_user(username)
  message = request.args.get("message")

  mail = MIMEMultipart("alternative")
  mail['Subject'] = f"{user_json['name']} ({username}) information follow up"
  mail['From'] = contact_mail
  mail['To'] = contact_mail2

  # message = f"Last known location: {locname}"

  mail.attach(MIMEText(message))

  mailer = smtplib.SMTP('smtp.gmail.com',587)
  mailer.starttls()
  mailer.login(contact_mail, contact_password)
  mailer.sendmail(contact_mail, contact_mail2, mail.as_string())
  mailer.quit()
  return ('ok', 200)  

##########################################################  See Jobs

@urlFuncs.route('/all_jobs', methods=['GET'])
def getJobs():
  return jobs_table.get_all_jobs()

  
  



  