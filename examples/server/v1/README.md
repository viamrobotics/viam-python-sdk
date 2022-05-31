# Client and Server Examples

This directory contains everything required to

1. Connect to a remote robot with the python client
2. Create a custom robot server in python with custom python components


## Client

If you would like to test a the client against an running robot, you should open the `client.py` file and update the connection code with the proper endpoint and credentials. Update the code so that you are referencing components that exist on the robot. Then, simply run `make run_client`.


## Server

The `server.py` file shows how to create your own custom Viam server with custom components, all written in python. You can view the example implementations of the custom components in the `compnents.py` file. To start the server, run `make run_server`. If you would then like to connect to the server via a robot client, you can run `make run_client` (with the proper endpoint and credentials, which is the default state of the client).
