import requests

class Model(object):
    """
    Model part of the MVC pattern, handles the Google Maps Direction API communication.
    """
    def requestNavigation(self, origin, destination, file_format):
        """
        Calls the Google Maps Directions API and returns a formatted string of the route description abd a status message

        :param origin: The origin of the navigation route
        :param destination: The destintion of the nagivation route
        :param file_format: Format of the API return, "json" or "xml"
        :return: Tuple of status message and formatted string of the route navigation description
        """


        # these will cause an HTTP 4xx error and are therefore handled
        # for more datailed error messages
        if origin == "" and destination == "":
            return "", "Error: start and destination missing"
        elif origin == "":
            return "", "Error: start missing"
        elif destination == "":
            return "", "Error: destination missing"

        url = "https://maps.googleapis.com/maps/api/directions/%s" % file_format
        params = {
            "origin": origin,
            "destination": destination,
            "language": "en",
            # INSERT YOUR OWN KEY HERE, DELETE WHEN PUBLISHING
            "key": "API_KEY"
        }

        try:
            # get response with url and data from above
            response = requests.get(url, params)
        except requests.exceptions.RequestException:
            return "", "Error: request error"

        # error handling
        # if response is 'OK' do response parsing and formatting
        if str(response.status_code)[0] == "2":
            if file_format == "json":
                return self.parseJSON(response.json())
            if file_format == "xml":
                return self.parseXML(response.content)

        # if response is HTTP 4xx/client error
        elif str(response.status_code)[0] == "4":
            return "", "Error: client error"

        # if response is HTTP 5xx/server error
        elif str(response.status_code)[0] == "5":
            return "", "Error: Google Maps Directions API unavailable"

        return "", "Error: general error"

    def parseJSON(self, json_data):
        """
        Parses the JSON response into an html formatted string and returns it with a status.

        :param json_data: the requests JSON response
        :return: tuple with the html formatted string and a status
        """
        # get status
        status = json_data["status"]

        # route_description = str(json_data)

        if status == "OK":
            route_description = "Total duration of %s. Distance of %s.<br><br>" % \
                                (json_data["routes"][0]["legs"][0]["duration"]["text"],
                                 json_data["routes"][0]["legs"][0]["distance"]["text"])

            for i in range(1, len(json_data["routes"][0]["legs"][0]["steps"])):
                route_description += "%i. %s. Duration %s, distance %s.<br>" % \
                                     (i,
                                      json_data["routes"][0]["legs"][0]["steps"][i]["html_instructions"],
                                      json_data["routes"][0]["legs"][0]["steps"][i]["duration"]["text"],
                                      json_data["routes"][0]["legs"][0]["steps"][i]["distance"]["text"])

            return route_description, status
        else:
            return "", status


    # todo: XML parsing
    def parseXML(self, xml_data):
        return str(xml_data), "XML not supported"
