import csv

#This script analyses some of my downloaded youtube daily data over the last 8 or so years

class videoTypeObject:
    def __init__(self, date, videoType, views, subscribersGained):
        self.date = date
        self.videoType = videoType
        self.views = views
        self.subscibersGained = subscribersGained


def readInAnalyticsData():
    
  entries = []

  with open ('Chart data.csv', newline = "") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar="|")
    next(reader, None)
    for row in reader:
        entries.append(videoTypeObject(row[0], row[1], row[2], row[3]))

  return entries



if __name__ == "__main__":
   print(readInAnalyticsData()[0].date)
