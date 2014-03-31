from flask import Flask
from flask import jsonify
import threading
from lxml import html
import requests
import json
class chart:
	def __init__(self,songlis,artlist,urllist):
		self.songs=songlist
		self.artists=artlist
		self.urls=urllist

	def __init__(self):
		self.songs=[]
		self.artists=[]
		self.urls=[]
	def setSongs(self,songlist):
		self.songs=songlist
	def setArtists(self,artlist):
		self.artists=artlist
	def setUrls(self,urllist):
		self.urls=urllist


hot100=chart();
rockHot100=chart();
popHot100=chart();
rnbHot100=chart();
danceHot100=chart();
latinHot100=chart();

app = Flask(__name__)

@app.route('/BillBoard/api/v1.0/getBillBoardHot100',methods=['GET'])
def getBillBoardHot100():
	
	print hot100.songs
	#temp= jsonify(hot100.songs)
	
	return json.dumps(hot100.__dict__)

@app.route('/BillBoard/api/v1.0/getRockHot100',methods=['GET'])
def getRockHot100():
	return json.dumps(rockHot100.__dict__)

@app.route('/BillBoard/api/v1.0/getPopHot100',methods=['GET'])
def getPopHot100():
	return json.dumps(popHot100.__dict__)

@app.route('/BillBoard/api/v1.0/getRnbHot100',methods=['GET'])
def getRnbHot100():
	return json.dumps(rnbHot100.__dict__)

@app.route('/BillBoard/api/v1.0/getDanceHot100',methods=['GET'])
def getDanceHot100():
	return json.dumps(danceHot100.__dict__)

@app.route('/BillBoard/api/v1.0/getLatinHot100',methods=['GET'])
def getLatin100():
	return json.dumps(latinHot100.__dict__)





def updateCharts():


	global hot100;
	global rockHot100;
	global popHot100;
	global rnbHot100;
	global danceHot100;
	global latinHot100;

	hot100=chart();
	rockHot100=chart();
	popHot100=chart();
	rnbHot100=chart();
	danceHot100=chart();
	latinHot100=chart();
	
	hotSongs=[]
	hotArtists=[]
	hotUrls=[]

	rockSongs=[]
	rockArtists=[]
	rockUrls=[]

	popSongs=[]
	popArtists=[]
	popUrls=[]

	rnbSongs=[]
	rnbArtists=[]
	rnbUrls=[]

	danceSongs=[]
	danceArtists=[]
	danceUrls=[]

	latinSongs=[]
	latinArtists=[]
	latinUrls=[]

	for i in range(10):
		if(i==0):
			hotUrl="http://www.billboard.com/charts/hot-100"
			rockUrl="http://www.billboard.com/charts/rock-songs"
			popUrl="http://www.billboard.com/charts/pop-songs"
			rnbUrl="http://www.billboard.com/charts/r-b-hip-hop-songs"
			danceUrl="http://www.billboard.com/charts/dance-electronic-songs"
			latinUrl="http://www.billboard.com/charts/latin-songs"
		else:	
			hotUrl="http://www.billboard.com/charts/hot-100?page="+str(i)
			rockUrl="http://www.billboard.com/charts/rock-songs?page="+str(i)
			popUrl="http://www.billboard.com/charts/pop-songs?page="+str(i)
			rnbUrl="http://www.billboard.com/charts/r-b-hip-hop-songs?page="+str(i)
			danceUrl="http://www.billboard.com/charts/dance-electronic-songs?page="+str(i)
			latinUrl="http://www.billboard.com/charts/latin-songs?page="+str(i)


		hotPage=requests.get(hotUrl)
		hotHtml_tree=html.fromstring(hotPage.content)
		hotSongs=hotSongs+hotHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/h1/text()')
		hotArtists=hotArtists+hotHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/p[@class="chart_info"]/a/text()')
		hotUrls=hotUrls+hotHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/p[@class="chart_info"]/a/@href')

		rockPage=requests.get(rockUrl)
		rockHtml_tree=html.fromstring(rockPage.content)
		rockSongs=rockSongs+rockHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/h1/text()')
		rockArtists=rockArtists+rockHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/p[@class="chart_info"]/a/text()')
		rockUrls=rockUrls+rockHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/p[@class="chart_info"]/a/@href')
			
		popPage=requests.get(popUrl)
		popHtml_tree=html.fromstring(popPage.content)
		popSongs=popSongs+popHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/h1/text()')
		popArtists=popArtists+popHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/p[@class="chart_info"]/a/text()')
		popUrls=popUrls+popHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/p[@class="chart_info"]/a/@href')

		rnbPage=requests.get(rnbUrl)
		rnbHtml_tree=html.fromstring(rnbPage.content)
		rnbSongs=rnbSongs+rnbHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/h1/text()')
		rnbArtists=rnbArtists+rnbHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/p[@class="chart_info"]/a/text()')
		rnbUrls=rnbUrls+rnbHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/p[@class="chart_info"]/a/@href')	

		dancePage=requests.get(danceUrl)
		danceHtml_tree=html.fromstring(dancePage.content)
		danceSongs=danceSongs+danceHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/h1/text()')
		danceArtists=danceArtists+danceHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/p[@class="chart_info"]/a/text()')
		danceUrls=danceUrls+danceHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/p[@class="chart_info"]/a/@href')

		latinPage=requests.get(latinUrl)
		latinHtml_tree=html.fromstring(latinPage.content)
		latinSongs=latinSongs+ latinHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/h1/text()')
		latinArtists=latinArtists+latinHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/p[@class="chart_info"]/a/text()')
		latinUrls=latinUrls+latinHtml_tree.xpath('//div[@class="listing chart_listing"]/article/header/p[@class="chart_info"]/a/@href')
		
	print hotSongs


	hot100.setSongs(hotSongs)
	hot100.setArtists(hotArtists)
	hot100.setUrls(hotUrls)


	rockHot100.setSongs(rockSongs)
	rockHot100.setArtists(rockArtists)
	rockHot100.setUrls(rockUrls)


	popHot100.setSongs(popSongs)
	popHot100.setArtists(popArtists)
	popHot100.setUrls(popUrls)

	rnbHot100.setSongs(rnbSongs)
	rnbHot100.setArtists(rnbArtists)
	rnbHot100.setUrls(rnbUrls)

	danceHot100.setSongs(danceSongs)
	danceHot100.setArtists(danceArtists)
	danceHot100.setUrls(danceUrls)

	latinHot100.setSongs(latinSongs)
	latinHot100.setArtists(latinArtists)
	latinHot100.setUrls(latinUrls)

	



if __name__=='__main__':
	updateCharts()
	app.run(host="0.0.0.0",debug=True)
