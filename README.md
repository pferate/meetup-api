#API Client for Meetup
A Python API client for [Meetup](http://meetup.com).

The official [Meetup REST API documentation](http://www.meetup.com/meetup_api/docs/) has a complete list of available API methods and their descriptions.  A brief listing of available API endpoints is located [here](API_METHODS.md).

#Interpreter

The package has been developed and tested with Python 2.6, 2.7, 3.4, and 3.5 under Linux (Ubuntu) and Microsoft Windows

#Authentication

The Meetup API has a four different methods of [authentication](http://www.meetup.com/meetup_api/auth/): OAuth2, OAuth 1.0a, API keys, and API key signatures.

This library currently only works with API keys.  Go to [this page](https://secure.meetup.com/meetup_api/key/) to get your API key (you will need a Meetup account).


#Installing

```bash
$ python setup.py install
```
	
#Usage

##Initialize Client

To initialize your Meetup API Client, you will need to import the Client class and create a Client object.  Before making and API requests, you will need to assign your API key to the object.

Three ways to assign your API key (in order of precedence):

###Initialization Method #1 (Assign to attribute)
```python
import meetup.api
client = meetup.api.Client()
client.api_key = 'my_special_api_key_value'
```

###Initialization Method #2 (Assign at initialization)
```python
import meetup.api
client = meetup.api.Client('my_special_api_key_value')
```

###Initialization Method #3 (Retrieved from environment variable)
```bash
$ export MEETUP_API_KEY=my_special_api_key_value
```
```python
import meetup.api
client = meetup.api.Client()
```


##Execute API Calls

#Testing

Testing is done using [tox](http://testrun.org/tox/latest/) to provide various environments and [pytest](http://pytest.org) is used as the test runner.

To run tests with all environments (interpreters):

    $ tox

To run tests in specific environments:

    $ tox -e <ENV_NAME>
    
Available tox environments:

* py26
* py27
* py34
* py35
* coverage (for code coverage)
* flake8 (for PEP8 checking)
* docs (for generating documentation)


License
=======

The MIT License (MIT)

Copyright (c) 2016 Pat Ferate

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
