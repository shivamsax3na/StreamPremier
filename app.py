from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def index():
	videoHeight = 500;
	video_source = "https://gcloud.live/v/rywg2hed--yjmd2?jwsource=cl";
	return render_template("index.html", video_source = video_source, videoHeight = videoHeight)

@app.route('/about')

def about():
	return render_template("about.html")

@app.route('/collection')

def collection():
	videoHeight = 500;
	title = "Mirzapur season 2";
	video_source = "https://gcloud.live/v/rywg2hed--yjmd2?jwsource=cl";
	return render_template("collection.html", title=title, video_source = video_source, videoHeight = videoHeight)

@app.route('/episode2')
def episode2():
	title = "Mirzapur season 2";
	sno = "TWO";
	videoHeight = 500;
	video_source = "https://gcloud.live/v/ky5g0h3w44m35nn?jwsource=cl";
	return render_template("episode2.html", sno=sno, video_source = video_source, title=title, videoHeight = videoHeight)


@app.route('/episode3')
def episode3():
	sno = "THREE";
	videoHeight = 500;
	title = "Mirzapur season 2";
	video_source = "https://gcloud.live/v/8p40ni8mllp248-?jwsource=cl";
	return render_template("episode3.html", sno=sno, video_source = video_source, title=title, videoHeight = videoHeight)

@app.route('/episode4')
def episode4():
	sno = "FOUR";
	videoHeight = 500;
	title = "Mirzapur season 2";
	video_source = "https://gcloud.live/v/pyjgzhmk11785y3?jwsource=cl";
	return render_template("episode4.html", sno=sno, video_source = video_source, title=title, videoHeight = videoHeight)

@app.route('/episode5')
def episode5():
	sno = "FIVE";
	videoHeight = 500;
	title = "Mirzapur season 2";
	video_source = "https://gcloud.live/v/w3ygxbnmjjnzm4w?jwsource=cl";
	return render_template("episode5.html", sno=sno, video_source = video_source, title=title, videoHeight = videoHeight)

@app.route('/episode6')
def episode6():
	sno = "SIX";
	videoHeight = 500;
	title = "Mirzapur season 2";
	video_source = "https://gcloud.live/v/36d3ecmreemrmqg?jwsource=cl";
	return render_template("episode6.html", sno=sno, video_source = video_source, title=title, videoHeight = videoHeight)

@app.route('/episode7')
def episode7():
	sno = "SEVEN";
	videoHeight = 500;
	title = "Mirzapur season 2";
	video_source = "https://gcloud.live/v/ky5g0h3w448eg07?jwsource=cl";
	return render_template("episode7.html", sno=sno, video_source = video_source, title=title, videoHeight = videoHeight)

@app.route('/episode8')
def episode8():
	sno = "EIGHT";
	videoHeight = 500;
	title = "Mirzapur season 2";
	video_source = "https://gcloud.live/v/ky5g0h3w44371nd?jwsource=cl";
	return render_template("episode8.html", sno=sno, video_source = video_source, title=title, videoHeight = videoHeight)

@app.route('/episode9')
def episode9():
	sno = "NINE";
	title = "Mirzapur season 2";
	videoHeight = 500;
	video_source = "https://gcloud.live/v/qy5gmhen006g11p?jwsource=cl";
	return render_template("episode9.html", sno=sno, video_source = video_source, title=title, videoHeight = videoHeight)

@app.route('/episode10')
def episode10():
	sno = "TEN";
	title = "Mirzapur season 2";
	videoHeight = 500;
	video_source = "https://gcloud.live/v/7r3dgbgkqqg63jw?jwsource=cl";
	return render_template("episode10.html", sno=sno, video_source = video_source, title=title, videoHeight = videoHeight)
