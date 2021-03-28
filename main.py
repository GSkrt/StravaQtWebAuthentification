#!/usr/bin/env python
""" QT GUI Strava authentification using PySide2

 Simple example of usage, just replace client strava ID and secret with your own api

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.

"""

import StravaLibQt_Authentification as sa


client_strava_id = 12343425234 # <put your strava ID here>
client_secret = 'asdfasgsdfhgpo345928345asdfv234dfsay' #<put your strava api secret here>'

# Class returns client and you can use stravalib methods
# Project abandoned due to restrictions from strava API

client = sa.refresh_access_token(client_strava_id, client_secret)

activities = client.get_activities(limit=10)

for activity in activities:
    print(activity.name)
    print(activity.id)
    print(str(activity.max_watts) + ' W')
    print(str(activity.average_watts) + ' W')
    print(activity.distance)
    print(activity.elapsed_time)
    print("=================================")

athlete = client.get_athlete()
print(athlete.stats)
print(athlete.id)
print("Hello, {}".format(athlete.firstname))

clubs = client.get_athlete_clubs()
for club in clubs:
    print(club.id)
    print(club.name)