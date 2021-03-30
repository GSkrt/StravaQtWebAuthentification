# Strava Qt Web Authentification

This is a simple script that will help you simplyfy authentification with Strava API using stravalib library. 
Check https://github.com/hozn/stravalib for further information how to get data to python from Strava servers.

This script helps you manage your access token and refresh of access token. It stores information in a access_token.acs 
file using pickle. 

Stravalib client is generated upon calling refresh_access_token method of LogInStravaWindow class. 


Basic example: 

<pre><code>
import StravaLibQt_Authentification as sa


# go to https://www.strava.com/settings/api and generate new Application  to get strava client id and secret

client_strava_id = 12343425234 <- put your own key
client_secret = 'asdfasgsdfhgpo345928345asdfv234dfsay'

#use client as stravalib client...
client = sa.refresh_access_token(client_strava_id, client_secret)
</code> </pre>

Strava API limits 30000 daily requests, so it's practically useless for some major APP development apart from personal activity analysis.
If you are like me, and you like to analyse time series this will help you get going without reinventing the wheel. 


Happy data analysis and add me on Strava :D   
