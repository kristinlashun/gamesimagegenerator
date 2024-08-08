# Random Game Image Generator Microservice

## Overview
This microservice generates a random game image and displays it using a simple GUI.

## How to Request Data
To request a random game image, send an HTTP GET request to the endpoint:

Use URL: http://127.0.0.1:5001/ 

Clear instructions for how to programmatically REQUEST data from the microservice you implemented.

For the web-based version (web folder): The program will request data from the user via an HTTP GET request to the /api/generate endpoint. The user will interact with the UI to trigger this request.

For the local file version (local folder): The program will read a request from a text file (request.txt), process the request to generate an image path, and write the result to another text file (response.txt).

Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.

For the web-based version: The program will receive the JSON response containing the image path and display the image in the GUI.

For the local file version: The program will read the response from the response.txt file, which contains the path to the generated image, and then display the image.

UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your teammate (and your grader) will understand.

Here is the UML sequence diagram that shows how requesting and receiving data works:

![image](https://github.com/user-attachments/assets/d71d2d1c-1ad0-4318-ba00-b131d8288220)

