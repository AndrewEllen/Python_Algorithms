import csv

#This script analyses some of my downloaded youtube daily data over the last 8 or so years

class videoTypeObject:
    def __init__(self, date, videoType, views, subscribersGained):
        self.date = date
        self.videoType = videoType
        self.views = views
        self.subscribersGained = subscribersGained


def readInAnalyticsData():
    
  entries = []

  with open ('Chart data.csv', newline = "") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar="|")
    next(reader, None)
    for row in reader:
        entries.append(videoTypeObject(row[0], row[1], row[2], row[3]))

  return entries


def analyseSubscriberGainPerType(entries):
   
  numberOfShorts = 0
  numberOfVideos = 0
  totalSubscribersShorts = 0
  totalSubscribersVideos = 0

  for entry in entries:
    if entry.videoType == "Shorts":
      numberOfShorts += 1
      totalSubscribersShorts += int(entry.subscribersGained)

    elif entry.videoType =="Videos":#
       numberOfVideos += 1
       totalSubscribersVideos += int(entry.subscribersGained)


  print("The total subscribers gained from the shorts page is", totalSubscribersShorts)
  print("The total subscribers gained from the videos page is", totalSubscribersVideos)

  print("On average a short gets", totalSubscribersShorts/numberOfShorts, "Subscribers")
  print("On average a video gets", totalSubscribersVideos/numberOfVideos, "Subscribers")

  print("The difference between videos subscribers and shorts subsribers gain is", totalSubscribersShorts/totalSubscribersVideos, "times the amount")




if __name__ == "__main__":
  entries = readInAnalyticsData()

  analyseSubscriberGainPerType(entries)
