import requests

jamendo_params = {
'entities': ['tracks'],
'tracks': {
'limit': range(10, 200+1),
'type': ['single', 'albumtrack'],
'featured': [0, 1],
'audioformat': ['mp31', 'mp32', 'ogg', 'flac'],
'audiodlformat': ['mp31', 'mp32', 'ogg', 'flac'],
'acousticelectric': ['acoustic', 'electric'],
'vocalinstrumental': ['vocal', 'instrumental'],
'gender': ['male', 'female'],
'speed': ['verylow', 'low', 'medium', 'high', 'veryhigh'],
'include': ['licenses', 'musicinfo', 'stats', 'lyrics'],
'groupby': ['artist_id', 'album_id'],
}
}

# some static functions
def get_durationbetween_string(duration_min_sec, duration_max_sec):
    if not isinstance(duration_min_sec, int) or not isinstance(duration_max_sec, int):
        raise Exception('durations must be integer.')

    return '{}_{}'.format(duration_min_sec, duration_max_sec)

class Connector():
    def __init__(self, client_id):
        self.client_id = client_id
        self.api_url = 'https://api.jamendo.com'
        self.version_string = 'v3.0'

    def get_url(self, entity, subentity=None):
        url = self.api_url + '/' + self.version_string
    
        if entity is not None:
            url += '/' + entity
    
        if subentity is not None:
            url += '/' + subentity
    
        return url + '/'

    def set_client_id(self, client_id):
        self.client_id = client_id

    def get_tag_string(self, tags):
        return '+'.join(tags)

    def search(self, entity, params):
        # expecting params to be a dict
        # no error checking so far (-> jamendo_params etc.)

        # set some default parameters
        # (some may be overridden by the passed params dict)
        params_processed = {}
        params_processed['client_id'] = self.client_id
        params_processed['format'] = 'json'

        # loop through all parameters and process according to the api's format specification
        for key, value in params.items():
            params_processed[key] = value

        url = self.get_url(entity)

        r = requests.get(url, params=params_processed)

        return r.json()

    def download(self, track_id, dir_output):
        # first find the download url
        search_result = self.search('tracks', {'id': track_id,
                                               'limit': 1})

        print(search_result['results'][0]['audiodownload'])

        data = requests.get(search_result['results'][0]['audiodownload'])

        f = open('{0:07}.mp3'.format(int(search_result['results'][0]['id'])), 'wb')
        f.write(data._content)
        f.close()

        return True
        
def search_album(name):
    payload = {'client_id': client_id,
               'format': 'json',
               'name': name}
    r = requests.get(get_url('albums'), params=payload)

    return r.json()
# def set_file_format(