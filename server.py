"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page. <a href="/hello">Hello page</a></html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method="GET">
          What's your name? <input type="text" name="person">
          <p></p>
          <label for="compliment-select">Please choose your compliment that you'll see in a moment after you hit the Submit button.</label>
          <select name="compliment" id="compliment">
            <option value="passionate">Passionate</option>
            <option value="brilliant">Brilliant</option>
            <option value="brave">Brave</option>
          </select>
          <input type="submit" value="Submit">
        </form>
        <p></p>
        <form action="/diss" method="GET">
          What's your name? <input type="text" name="person">
          <p></p>
          <label for="diss-select">Please choose your diss that you'll see in a moment after you hit the Submit button.</label>
          <select name="diss" id="diss">
            <option value="disrespectful">Disrespectful</option>
            <option value="lazy">Lazy</option>
            <option value="stupid">Stupid</option>
          </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""
    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss')
def diss_person():
    """Get user by name."""
    player = request.args.get("person")

    diss = request.args.get("diss")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
