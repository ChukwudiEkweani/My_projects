# ISS_overhead

In this project, I wrote a program that keeps watch over the International Space Station with the coordinates of its current location every 60 seconds. 
It is able to do this by communicating with the API of the website that shows the current coordinates of the International Space Station (ISS) in latitude and longitude.
The website renders the coordinates in JSON data format.

This program also informs the user whenever the ISS is over head their location by sending an email notification to the user.

The program is written in such a way that it checks whether the environment is dark (because the ISS can only be seen at night) before sending the notification.
The ISS is not visible in the sky unless the sky is dark.

This is possible by the use of another API that gets the current time of a certain place (your coordinate in this case).

The aim of this mini project is to demonstrate the use of APIs to collect data and use the data collected to create valuable bots and models.





