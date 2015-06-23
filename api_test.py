from pyjamendo import connector

# to access the JAMENDO_CLIENT_ID environment variable
import os

# the environment variable JAMENDO_CLIENT_ID is expected to be set to the
# jamendo developer account client_id
client_id = os.getenv('JAMENDO_CLIENT_ID')
if client_id == None:
    raise NameError("The JAMENDO_CLIENT_ID environment variable could not be found.")

c = connector(client_id)

result = c.search('tracks', {'tags': 'rock',
                             'limit': 3})

print(result)

#d = c.download(1141572, '.')
#d = c.download(1141571, '.')