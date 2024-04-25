## What is a Web API?
An Web API is a way for a computer program to get information from a different computer. Usually, the computer provides information that the program won't be able to access by itself, such as the current weather in a particular city. 

## NextBus API
The NextBus API could be used for several different purposes related to public transit:
* Tracking the position of public transit vehicles to determine where they spent the most time at, which could help with:
  * Determining the location of traffic jams
  * Identifying poorly designed intersections, which could be used by city planners to improve infrastructure or by the public transit service to plan routes that bypass them to save time
* Getting the routes for a given transit agency, which could be used by a navigation app to plan a route using public transit
* Getting the schedule or stop predictions to determine when the customer should arrive at a stop with minimal wait time
* Getting any messages published by a transit agency to determine whether there are problems at a current stop or disruptions to regular service

The NextBus API is a REST API, providing both JSON and XML files.

The NextBus API is described [here](https://gist.github.com/grantland/7cf4097dd9cdf0dfed14).
* To specify the data you want, add `?command=dataRequested` to the URL.
* Some commands require arguments. To add an argument, add `&argumentName=argumentValue`.

Base URL:
* JSON: `http://webservices.nextbus.com/service/publicJSONFeed`
* XML: `http://webservices.nextbus.com/service/publicXMLFeed`

## WhatTheCommit API
The WhatTheCommit API could be used to retrieve humourous commit messages instead of writing them normally. It isn't particularily useful for making commits on an actual repository, but it could be used as a teaching tool to show why descriptive commit messages are useful by filling a repository with its commit messages and then asking a student to find when a particular change occurred. Once the student realizes how difficult this is, they could be encouraged to improve their own commit messages so they don't encounter this problem.

The WhatTheCommit API is a REST API, providing a random commit message whenever the base URL is accessed.

URL: `https://whatthecommit.com/index.txt`

## GraphQL Weather API
The GraphQL Weather API is a GraphQL wrapper for the [OpenWeather Weather API](https://openweathermap.org/api).

The GraphQL Weather API can be used to make a weather app that get weather for a particular location, which can be used to help plan the user's day.

The GraphQL Weather API is accessible through GraphQL.

yeah but it doesnt work

## GitHub