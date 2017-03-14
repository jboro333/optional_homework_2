#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

import sys
import requests
import json
# import xmltodict

api_key = None


class WeatherClient(object):
    """docstring for WeatherClient"""
    url_base = 'http://api.wunderground.com/api/'
    url_service = {"hourly": "/hourly/q/CA/"}

    def __init__(self, api_key):
        super(WeatherClient, self).__init__()
        self.api_key = api_key

    def hourly(self, location):
        """
        Accesses wunderground hourly information for the given location
        """
        resp_format = "json"
        url = WeatherClient.url_base + api_key + \
            WeatherClient.url_service[
                "hourly"] + location + "." + resp_format
        r = requests.get(url)
        jsondata = json.loads(r.text)
        return jsondata["hourly_forecast"]


def print_hourly(hourly):
    """
    Prints an forecast received as a dict
    """
    # print hourly[1]["FCTTIME"]["hour"]
    print "On this date: " + hourly[0]["FCTTIME"]["mday"] + "/" + \
        hourly[0]["FCTTIME"]["mday"] + "/" + \
        hourly[0]["FCTTIME"]["year"]
    print " "
    count = []
    count = list(range(0, 24))
    for x in count:
        print "At this hour: " + hourly[x]["FCTTIME"]["hour"] + ":" + \
            hourly[x]["FCTTIME"]["min"] + ":" + hourly[x]["FCTTIME"]["sec"]
        print "Temperature: " + hourly[x]["temp"]["metric"] + "C"
        print "Humidity: " + hourly[x]["humidity"] + "%"
        print " "
    print "End"


if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "Must provide api key in code or cmdline arg"

    weatherclient = WeatherClient(api_key)
    print_hourly(weatherclient.hourly("Lleida"))
