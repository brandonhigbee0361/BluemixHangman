#PolyBlue

Simple BlueMix application and framework to execute local command line python applications through a web portal.

[![Deploy to Bluemix](https://bluemix.net/deploy/button.png)](https://bluemix.net/deploy?repository=https://github.com/HenChao/PolyBlue)

## Requirements

Your local environment will need the websocket-client module installed in order to run the PolyBlueClient library. See the [package page](https://pypi.python.org/pypi/websocket-client/) for installation instructions.

## How to use
0. Install the websocket-client module
  * Very important step! See the Requirements section above.

1. Deploy the server code onto BlueMix
  * You can either use the Deploy to Bluemix button above, or manually push the code onto Bluemix from your local environment, but the code is ready to go as-is

2. Get a copy of the polyBlueClient.py file to your local directory
  * Simplest way would be to visit [this link](https://raw.githubusercontent.com/HenChao/PolyBlue/master/polyBlueClient.py) and save the page as polyBlueClient.py onto your machine. Be sure to save it in the same directory as your python code!

3. Import the PolyBlueClient class into your code
  * Take a look at the first line in the [example.py](https://github.com/HenChao/PolyBlue/blob/master/example.py) file for the recommended way to import the class

4. Write the code to send messages and receive inputs from the web site!
  * Take a look at the [example.py](https://github.com/HenChao/PolyBlue/blob/master/example.py) file to get an idea of how to use the PolyBlueClient class

## Note: Running your application

When you are ready to run your application, please be sure that everything is ready in the following order:

1. The server code is running on BlueMix
2. You have a web browser open to your BlueMix application

Only after the first two steps are complete, then should you proceed to run your python script from your computer.
