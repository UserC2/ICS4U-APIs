# Web APIs
## What is a Web API?
An Web API is a way for a computer program to get information from a different computer. Usually, the computer provides information that the program won't be able to access by itself, such as the current weather in a particular city. 

## NextBus API
The [NextBus API](https://gist.github.com/grantland/7cf4097dd9cdf0dfed14) could be used for several different purposes related to public transit:
* Tracking the position of public transit vehicles to determine where they spent the most time at, which could help with:
  * Determining the location of traffic jams
  * Identifying poorly designed intersections, which could be used by city planners to improve infrastructure or by the public transit service to plan routes that bypass them to save time
* Getting the routes for a given transit agency, which could be used by a navigation app to plan a route using public transit
* Getting the schedule or stop predictions to determine when the customer should arrive at a stop with minimal wait time
* Getting any messages published by a transit agency to determine whether there are problems at a current stop or disruptions to regular service

The NextBus API is a REST API, providing both JSON and XML files.

The NextBus API is described [here](https://gist.github.com/grantland/7cf4097dd9cdf0dfed14).
* To specify the data you want, add a `command=dataRequested` argument to the URL.

Base URL:
* JSON: `http://webservices.nextbus.com/service/publicJSONFeed`
* XML: `http://webservices.nextbus.com/service/publicXMLFeed`

## WhatTheCommit API
The WhatTheCommit API could be used to retrieve humourous commit messages instead of writing them normally. It isn't particularily useful for making commits on an actual repository, but it could be used as a teaching tool to show why descriptive commit messages are useful by filling a repository with its commit messages and then asking a student to find when a particular change occurred. Once the student realizes how difficult this is, they could be encouraged to improve their own commit messages so they don't encounter this problem.

The WhatTheCommit API is a REST API, providing a random commit message whenever the base URL is accessed.

URL: `https://whatthecommit.com/index.txt`

## Weather API
The [Weather API](https://www.weatherapi.com) can be used for any purpose requiring weather data, such as:
* Get weather predictions and display them to the user so they can dress appropriately
* Get current wind conditions at a particular location to calculate the trajectory of a flying disk
* Get historical weather data to visualize weather trends (e.g. showing the average temperature of each region in Canada overlaid on a map)

The Weather API is a REST API, requiring an API key to connect.
* To specify the type of service, append `/service_name.extension` to the URL.
  * `extension` may be `json` or `xml`.
* Specify your key with a `key` argument after the URL.

Base URL: `https://api.weatherapi.com/v1`

## GitHub
GitHub's API can be used to automate project-tracking tasks. For example, it could be used to automatically file issues from a Google Form for product users that are not familiar with GitHub's user interface.

### Usage
GitHub has a REST and GraphQL API.

REST:
* Change `www` to `api` in the URL for the item you want to access. For example:
* `https://api.github.com/UserC2/ICS4U-APIs/issues`

GraphQL:
* The same URL is used for all GraphQL requests:
* `https://api.github.com/graphql`

# URL Tips
A `?` is used after a URL to specify arguments to pass to an API
* e.g. `https://api.weatherapi.com/v1/current.json?key=12345678`

A `&` is used to seperate each argument
* e.g. `https://api.weatherapi.com/v1/current.json?key=12345678&q=New York&aqi=no`