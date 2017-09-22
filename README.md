# pyjamendo
A Python module to access the Jamendo API v3.0. Until now, only a small subset of functionality provided by the Jamendo 
API is supported. A detailed description of the API can be found at https://developer.jamendo.com/v3.0.

Until now, only the search for *tracks* is supported. 

## Installation
pyjamendo can be installed from the source code via setuptools:

```
python setup.py install
```

## Usage
To use the Jamendo API, a client ID is required. It can be obtained from [the Jamendo developer portal](https://devportal.jamendo.com/).
 
The interface to the API is the ```Connector``` class:

```
c = Connector(client_id)
```

Searches are started with the ```Connector.search()``` method that until now requires "tracks" as the first argument
and a ```dict``` that contains items describing the query parameters as a second argument. The supported query parameters
are listed at https://developer.jamendo.com/v3.0/tracks.

The ```Connector.search()``` method returns a ```dict``` with two items: *headers*, and *results*. The *headers* item
contains information about whether the query was successful and the number of returned query results. The *results* item
contains a list of ```dict```s containing information regarding the found tracks.