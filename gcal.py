from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
#SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SCOPES = ['https://www.googleapis.com/auth/calendar']



eventMatin = {
    'summary': 'W',
  'location': '',
  'description': '',
  'start': {
      'dateTime': '2019-12-03T07:30:00+01:00',
    'timeZone': 'Europe/Paris',
    },
  'end': {
      'dateTime': '2019-12-03T15:00:00+01:00',
    'timeZone': 'Europe/Paris',
    },
}


class gcal():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    
    def __init__(self):
        self.calID = "1isiolu2mu8962t8svogbcogkc@group.calendar.google.com"
        
        self.get_service_running()
        
    def get_service_running(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
    
        self.service = build('calendar', 'v3', credentials=creds)
    def read(self,date,ID=0):
        events_result = self.service.events().list(calendarId=self.calID, timeMin=date.isoformat()+'T00:00:00.000000Z',
                                                       maxResults=1, singleEvents=True,
                                                orderBy='startTime').execute()
         
        events = events_result.get('items', [])
        if not events:
            res = 0
        else :
            event = events[0]
            start = event['start'].get('dateTime', event['start'].get('date'))
            if start[:10] == date.isoformat():
                if ID ==0:
                    res = event['summary']
                elif ID == 1:
                    res = event["id"]
            else:
                res = 0
        
        return res
    def read_next10events(self):
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        #calID = 'primary'
        events_result = self.service.events().list(calendarId=self.calID, timeMin=now,
                                            maxResults=10, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])
    
        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    def create_event(self,myevent):
        if myevent != 0:
            event = self.service.events().insert(calendarId=self.calID, body=myevent).execute()
            print('Event created: %s' % (event.get('htmlLink')))
    
    def delete_event(self,day):
        eventID = self.read(day,ID=1)
        print(day,eventID)
        if eventID != 0 : 
            self.service.events().delete(calendarId=self.calID, eventId=eventID).execute()
            #pass
        
if __name__ == '__main__':
    Mygcal = gcal()
    Mygcal.read_next10events()


            
        