from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the URL submitted by the user
        user_url = request.form.get('url')
        
        # Do some processing with the URL (or pass it to another function)
        # For now, we'll just pretend it takes some time using `sleep`
        from time import sleep
        sleep(5)  # Simulate some processing time
        
        # Redirect to the done page after processing
        return redirect(url_for('done'))
    
    # Render the submission form
    return render_template('index.html')

@app.route("/help")
def help():
    return render_template("help.html")

@app.route('/processing')
def processing():
    # This will show the processing screen while the URL is being processed
    return "Processing... Please wait."

@app.route('/transcribe')
def transcribe():
    return "Transcribing..."

@app.route("/done")
def done():
    return f"done"
    # return render_template("done.html")

app.run(debug=True)