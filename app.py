from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def index():
	video_source = "https://gcloud.live/v/rywg2hed--yjmd2?jwsource=cl";
	return render_template("index.html", video_source = video_source )

@app.route('/about')

def about():
	return render_template("about.html", video_source = video_source)

@app.route('/collection')

def collection():
	title = "Mirzapur season 2";
	return render_template("collection.html", title=title, video_source = video_source)

@app.route('/episode2')
def episode2():
	sno = "TWO";
	return render_template("episode2.html", sno=sno, video_source = video_source)


@app.route('/episode3')
def episode3():
	sno = "THREE";
	return render_template("episode3.html", sno=sno, video_source = video_source)

@app.route('/episode4')
def episode4():
	sno = "FOUR";
	return render_template("episode4.html", sno=sno, video_source = video_source)

@app.route('/episode5')
def episode5():
	sno = "FIVE";
	return render_template("episode5.html", sno=sno, video_source = video_source)

@app.route('/episode6')
def episode6():
	sno = "SIX";
	return render_template("episode6.html", sno=sno, video_source = video_source)

@app.route('/episode7')
def episode7():
	sno = "SEVEN";
	return render_template("episode7.html", sno=sno, video_source = video_source)

@app.route('/episode8')
def episode8():
	sno = "EIGHT";
	return render_template("episode8.html", sno=sno, video_source = video_source)

@app.route('/episode9')
def episode9():
	sno = "NINE";
	return render_template("episode9.html", sno=sno, video_source = video_source)

@app.route('/episode10')
def episode10():
	sno = "TEN";
	return render_template("episode10.html", sno=sno, video_source = video_source)
