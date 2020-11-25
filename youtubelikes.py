from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from apikey import apikey


class YoutubeBot:

    CLIENT_SECRET_FILE = 'client_secret.json'
    SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_console()
    youtube = build('youtube', 'v3', credentials=credentials)

    def getVids(self):
        searchString = "kagaya john"  # search paramter
        numOfResults = 100
        ids = [] #stores the video ids
        
        youtube = build('youtube', 'v3', developerKey=apikey)
        req = youtube.search().list(q=searchString, part='snippet', type='video', maxResults=numOfResults)
        res = req.execute()
        print("You will be like/commenting on the following videos: ")
        for item in res['items']:
            print(item['snippet']['title'])
            ids.append((item['id']['videoId'], item['snippet']['channelId']))

        
        return ids

    def likeVids(self):
        ids = self.getVids()
        for videoId in ids:
            self.youtube.videos().rate(rating='like', id=videoId[0]).execute()




bot = YoutubeBot()
bot.likeVids()