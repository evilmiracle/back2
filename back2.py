#!/usr/bin/python
# -*- coding: UTF-8 -*-

#获取图片地址
#获取价格
#获取商品标题
#获取评论量
#获取评分星级
#函数化
from bs4 import BeautifulSoup

into = []

def geturl():
	soup = BeautifulSoup(open('D:/Plan-for-combating-master/week1/1_2/1_2answer_of_homework/1_2_homework_required/index.html'),'lxml')
	images = soup.select('body > div > div > div.col-md-9 > div > div > div > img')
	prices = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
	titles = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
	#titles = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4:nth-of-type(2) > a')
	reviews = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
	starts = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
	
	for image,price,title,review,start in zip(images,prices,titles,reviews,starts):

		data = {

			'image':image.get('src'),
			'price':price.get_text(),
			'title':title.get_text(),
			'review':review.get_text(),
			'start':len(start.find_all("span",class_="glyphicon glyphicon-star"))

		}
		into.append(data)

		for i in into:
			if i['start']>3:
				print i['image'],
				print i['price'],
				print i['title'],
				print i['review'],
				print i['start']

print geturl()
