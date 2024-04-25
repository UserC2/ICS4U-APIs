# Frisbee Wind Compensator
Imagine you want to throw a frisbee to your friend, but it's an annoyingly windy day. You try multiple times, yet you are incapable of throwing the frisbee towards your friend with any consistency. If only you had a way of calculating the correct angle to throw the frisbee!

Well, worry not! This program will calculate the angle offset necessary for you to throw the frisbee to your friend! Since you want to spend the most time possible using your frisbee, the program finds the wind speed at your location automatically, and "only" requires you to enter the speed and compass heading that you will throw the frisbee at.

## Process
* Get speed and heading of frisbee from the user
* Get location, then weather, then wind speed and heading using location & weather APIs
* Calculate angle offset necessary for frisbee to go to target

## Assumptions
* The user actually knows how fast the frisbee is travelling
* The frisbee travels at a constant speed
* The velocity of the wind will affect the velocity of the frisbee by the same amount (i.e. if the wind is 5 km/h east, your frisbee will move 5 km/h eastward)

(As a result of these assumptions, UserC2™ is not responsible if you throw the frisbee and it hits a random passer-by instead of going to your friend.)

## Notes
*I do not actually have a trademark on my username, sorry.*