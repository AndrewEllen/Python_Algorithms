import csv
import matplotlib.pyplot as plot

#This script analyses some of my downloaded youtube daily data over the last 8 or so years

class videoTypeObject:
    def __init__(self, date, videoType, views, subscribersGained):
        self.date = date
        self.videoType = videoType
        self.views = views
        self.subscribersGained = subscribersGained

class analysedStats:
   def __init__(self, numberOfShortsViewDays, numberOfVideosViewDays, totalShortsSubscribersGained, totalVideosSubscribersGained, totalShortsViews, totalVideosViews):
      self.numberOfShortsViewDays = numberOfShortsViewDays
      self.numberOfVideosViewDays = numberOfVideosViewDays
      self.totalShortsSubscribersGained = totalShortsSubscribersGained
      self.totalVideosSubscribersGained = totalVideosSubscribersGained
      self.totalShortsViews = totalShortsViews
      self.totalVideosViews = totalVideosViews


def readInAnalyticsData():
    
  entries = []

  with open ('Chart data.csv', newline = "") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar="|")
    next(reader, None)
    for row in reader:
        if int(row[2]) != 0 or int(row[3]) != 0:
          entries.append(videoTypeObject(row[0], row[1], row[2], row[3]))

  return entries


def analyseSubscriberGainPerType(entries):
   
  numberOfShortsViewDays = 0
  numberOfVideosViewDays = 0
  totalSubscribersShorts = 0
  totalSubscribersVideos = 0
  totalViewsShorts = 0
  totalViewsVideos = 0

  for entry in entries:
    if entry.videoType == "Shorts":
      numberOfShortsViewDays += 1
      totalSubscribersShorts += int(entry.subscribersGained)
      totalViewsShorts += int(entry.views)

    elif entry.videoType =="Videos":
       numberOfVideosViewDays += 1
       totalSubscribersVideos += int(entry.subscribersGained)
       totalViewsVideos += int(entry.views)

  return analysedStats(numberOfShortsViewDays, numberOfVideosViewDays, totalSubscribersShorts, totalSubscribersVideos, totalViewsShorts, totalViewsVideos)


def displayGraphs(analysedData, entries):
   
  x = [1,2]
  y = [analysedData.totalShortsSubscribersGained, analysedData.totalVideosSubscribersGained]

  labels = ["Shorts", "Videos"]
  
  plot.bar(x, y, tick_label = labels, width = 1, color = ["red","purple"])

  plot.xlabel("Video Type")
  plot.ylabel("Subscribers Gained")

  plot.title("Subscribers Gained vs video type")

  plot.show()


    




if __name__ == "__main__":

  entries = readInAnalyticsData()
  analysedData = analyseSubscriberGainPerType(entries)

  displayGraphs(analysedData, entries)

