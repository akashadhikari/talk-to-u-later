# Talk to u later
<p>Imagine its your girlfriend's birthday tomorrow. (No offense if you're single. You can still imagine. :p )</p>
<p>You had a very long day at work and thus, all you wanna do is go to bed once you reach home. But you know you have to wish her exactly at 00:00 because idk, its like the <b>golden rule</b> of relationship. </p>
<p>What do you do? You'll probably be a good lad and stay up all night just to wish her a happy birthday on Facebook and make her feel "special" (lol).</p>
<p>Or, may be, you can become a smart lad and try this dope thing. <b>Talk to u later (ttyl)</b> is for people like you. Its also for people like me. Its for everyone who are busy in their lives. Its for everyone who would love to send <b>scheduled Facebook messages.</b></p>

# Requirements
I assume you have following things installed already:
- git
- python
- virtualenv
- a girlfriend (optionally :p )

# Installation

`git clone https://github.com/akashadhikari/talk-to-u-later.git`

`cd talk-to-u-later`

`python3 -m venv .venv`

`source .venv/bin/activate`

`pip3 install -r requirements.txt`

`python3 manage.py migrate`

`python3 manage.py runserver`

### In the next terminal window

### Install Redis
`sudo apt install redis-server` if you are on linux.
Check out [Redis Website](https://redis.io/download) for more details.

### Check if Redis is up!

`redis-cli ping`

### This should show you the result `PONG`

### In the same terminal

`source .venv/bin/activate`

`celery -A ttyl worker -l info`

### In yet another terminal window, run

`source .venv/bin/activate`

`celery -A ttyl beat -l info`

### Open your browser and go to
`http://localhost:8000/`

### That's it. Now you can send delayed Facebook messages!
<b>WARNING!!!</b>: If you schedule the time to the past, the application will cause distortion in time and space which might ultimately lead you to an alternate universe. :p

# Screenshot

![alt text](https://raw.githubusercontent.com/akashadhikari/talk-to-u-later/master/screenshots/schedule.png "Home page screenshot.")
