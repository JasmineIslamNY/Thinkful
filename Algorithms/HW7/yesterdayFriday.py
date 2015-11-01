from datetime import datetime, timedelta
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/MMDD")
def yesterday_friday_mmdd():
    today = datetime.now() 
    day = today.strftime('%a')

    if day == 'Mon':
        yesterday = today - timedelta(days=3)
        yesterday = yesterday.strftime('%m/%d')
    elif day == 'Sun':
        yesterday = today - timedelta(days=2)
        yesterday = yesterday.strftime('%m/%d')
    else:
        yesterday = today - timedelta(days=1)
        yesterday = yesterday.strftime('%m/%d')

    return render_template('yesterday.html', yesterday=yesterday, title='MMDD')



if __name__ == "__main__":
	app.run(debug=True)