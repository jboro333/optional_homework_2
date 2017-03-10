#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

import sys
import requests
import json

api_key = None


class WeatherClient(object):
    """docstring for WeatherClient"""
    url_base = "http://api.wunderground.com/api/"
    url_service = {"forecast": "/forecast/q/CA/"}

    def __init__(self, api_key):
        super(WeatherClient, self).__init__()
        self.api_key = api_key

    def forecast(self, location):
        """
        Accesses wunderground forecast information for the given location
        """
        resp_format = "json"
        url = WeatherClient.url_base + api_key + \
            WeatherClient.url_service[
                "forecast"] + location + "." + resp_format
        r = requests.get(url)

        jsondata = json.loads(r.text)
        print url
        print jsondata
        return jsondata["forecast"]


def print_forecast(forecast):
    """
    Prints an forecast received as a dict
    """
    # print "Average on this date", forecast["date.day"]


if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "Must provide api key in code or cmdline arg"

    weatherclient = WeatherClient(api_key)
    print_forecast(weatherclient.forecast("Lleida"))
