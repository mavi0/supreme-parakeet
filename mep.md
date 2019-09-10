# ONOS Intent RestAPI Demo

In this document we're going to use the ONOS RestAPI to get intent statistics data and then change the route an intent uses. 
To use the RestAPI, there are three urls which we need to look at: 

1. [/onos/v1/imr/imr/monitoredIntents](http://51.15.59.76:8181/onos/v1/imr/imr/monitoredIntents) - This lists the intents registered on the network in json format. [Here's](https://github.com/mavi0/supreme-parakeet/blob/master/monitoredIntents.json) an example file.

2. [/onos/v1/imr/imr/intentStats](http://51.15.59.76:8181/onos/v1/imr/imr/intentStats) - This prints the realtime statistics data about all the intents on the network in JSON format. [Here's](https://github.com/mavi0/supreme-parakeet/blob/master/intentStats.json) an example file.

3. [/onos/v1/imr/imr/reRouteIntents](http://51.15.59.76:8181/onos/v1/imr/imr/reRouteIntents) - This is where, in JSON format, a request is made to change intents on the network. Here's](https://github.com/mavi0/supreme-parakeet/blob/master/reroute.json) an example file.