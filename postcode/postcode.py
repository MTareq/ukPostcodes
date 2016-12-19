import os
import requests
from  validator import validate

API_URL = "http://api.postcodes.io/"

def generate_from_file(file_path):
    """Read a text file for each line represents a postal code 
       and returns a generator of PostCode objects from each valid code"""

    if os.path.exists(file_path):
        with open(file_path, 'r') as codes:
            for code in codes:
                try:
                    new_code  = PostCode(code.strip())
                except Exception:
                    pass
                else:
                    yield new_code
    else:
        raise Exception("File does not exist")


class PostCode():


    def valid(self, code):
        """validate initial code to the uk postal code format."""

        return validate(str(code).upper())

    def get_from_api(self, query):
        try:
            resp = requests.get(API_URL + query)
        except (requests.ConnectionError, requests.Timeout) as e:
            raise e
        else:
            return resp

    def lookup(self):
        """Querys using the provided code against an online database to check if it actually exists.
           if exists return the response as dict containing information about the post code."""

        res = self.get_from_api('postcodes/' + self.code)
        if res.ok:
            info = res.json()['result']
            return info
        else:
           res.raise_for_status()

    def lookup_out(self):
        """Query using the outward code against an online database to check if it actually exists.
           if exists return the response as dict containing information about the out code."""

        res = self.get_from_api('outcodes/' + self.outcode)
        if res.ok:
            outward_info = res.json()['result']
            return outward_info
        else:
           res.raise_for_status()

    def nearest(self):
        """Querys using the provided code against an online database to check if it actually exists.
           if exists return the response as an array of the nearest post codes to the provided code."""

        res = self.get_from_api('postcodes/' + self.code + '/nearest')
        if res.ok:
            nearest_info = res.json()['result']
            return nearest_info
        else:
           res.raise_for_status()

    def nearest_out(self):
        """Query using the outward code against an online database to check if it actually exists.
           if exists return the response as an array of the availabe out codes near to that outward code."""

        res = self.get_from_api('outcodes/' + self.outcode + '/nearest')
        if res.ok:
            nearest_out_info = res.json()['result']
            return nearest_out_info
        else:
           res.raise_for_status()

    def __init__(self, code):
        if not self.valid(code):
            raise Exception("Postal Code is not valid")
        self.code = code
        self.outcode = self.code.split(' ', 1)[0]
        self.info = self.lookup()
        self.outward_info = self.lookup_out()
        self.nearest_info = self.nearest()
        self.nearest_out_info = self.nearest_out()




