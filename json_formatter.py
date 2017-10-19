
############# COPY TO JUPYTER NOTEBOOK INSTALL DIR ########################


# cp   ../json_formatter.py   ~/.ipython/profile_default/startup/json_formatter.py


## PRINT PRETTY JSON X DEMO

import uuid
from IPython.display import display_javascript, display_html, display
import json

class RenderJSON(object):
    def __init__(self, json_data):
        if isinstance(json_data, dict):
            self.json_str = json.dumps(json_data)
        else:
            self.json_str = json
        self.uuid = str(uuid.uuid4())

    def _ipython_display_(self):
        display_html('<head><link rel="stylesheet" type="text/css" href="json_formatter.css"></head><body><div id="{}" style="background-color: black;"></div></body>'.format(self.uuid),
            raw=True
        )
        display_javascript("""
        require(["https://rawgit.com/caldwell/renderjson/master/renderjson.js"], function() {
          document.getElementById('%s').appendChild(renderjson(%s))
        });
        """ % (self.uuid, self.json_str), raw=True)
