# StravaQtWebAuthentification

This is a simple script for authentification with stravalib library. Check "main.py" for example how to use this module and don't forget to open new application 
"My API Application" on strava API site. 

import StravaLibQt_Authentification as sa


# go to https://www.strava.com/settings/api and generate new Application  to get strava client id and secret

client_strava_id = 12343425234 <- put your own key
client_secret = 'asdfasgsdfhgpo345928345asdfv234dfsay'

client = sa.refresh_access_token(client_strava_id, client_secret)


Since you are limited with 30000 daily requests, strava API its practically useles for some  development apart from some personal activity analysis.
If you are like me and you like to analyse time series this will help you get going. 

Happy data analysis. 
