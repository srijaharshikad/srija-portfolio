"""
Google Sheets Service for Portfolio Analytics
Handles data collection and storage in Google Sheets
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Optional

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

class GoogleSheetsService:
    """Service for interacting with Google Sheets API"""
    
    def __init__(self, spreadsheet_id: str, sheet_name: str = 'Portfolio Analytics'):
        self.spreadsheet_id = spreadsheet_id
        self.sheet_name = sheet_name
        self.service = None
        self._authenticate()
    
    def _authenticate(self):
        """Authenticate with Google Sheets API"""
        creds = None
        # The file token.json stores the user's access and refresh tokens.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        
        self.service = build('sheets', 'v4', credentials=creds)
    
    def create_sheet(self) -> bool:
        """Create the portfolio analytics sheet with headers"""
        try:
            # Check if sheet exists
            spreadsheet = self.service.spreadsheets().get(
                spreadsheetId=self.spreadsheet_id
            ).execute()
            
            sheet_exists = any(
                sheet['properties']['title'] == self.sheet_name 
                for sheet in spreadsheet['sheets']
            )
            
            if not sheet_exists:
                # Create new sheet
                request_body = {
                    'requests': [{
                        'addSheet': {
                            'properties': {
                                'title': self.sheet_name
                            }
                        }
                    }]
                }
                
                self.service.spreadsheets().batchUpdate(
                    spreadsheetId=self.spreadsheet_id,
                    body=request_body
                ).execute()
            
            # Set up headers
            headers = [
                'Timestamp',
                'Event Type', 
                'Player Name',
                'Score',
                'Views',
                'Achievements',
                'Interactions',
                'User Agent',
                'URL',
                'Additional Data'
            ]
            
            # Write headers to the sheet
            self.service.spreadsheets().values().update(
                spreadsheetId=self.spreadsheet_id,
                range=f'{self.sheet_name}!A1:J1',
                valueInputOption='RAW',
                body={'values': [headers]}
            ).execute()
            
            print(f"✅ Sheet '{self.sheet_name}' is ready!")
            return True
            
        except HttpError as error:
            print(f"❌ Error creating sheet: {error}")
            return False
    
    def add_data(self, data: Dict) -> bool:
        """Add a new row of data to the sheet"""
        try:
            # Prepare the row data
            row_data = [
                datetime.now().isoformat(),
                data.get('type', 'unknown'),
                data.get('playerName', 'anonymous'),
                data.get('score', 0),
                data.get('views', 0),
                data.get('achievements', 0),
                data.get('interactions', 0),
                data.get('userAgent', ''),
                data.get('url', ''),
                json.dumps(data.get('additionalData', {}))
            ]
            
            # Append the row
            self.service.spreadsheets().values().append(
                spreadsheetId=self.spreadsheet_id,
                range=f'{self.sheet_name}!A:J',
                valueInputOption='RAW',
                insertDataOption='INSERT_ROWS',
                body={'values': [row_data]}
            ).execute()
            
            print(f"✅ Data added: {data.get('type', 'unknown')} - {data.get('playerName', 'anonymous')}")
            return True
            
        except HttpError as error:
            print(f"❌ Error adding data: {error}")
            return False
    
    def get_analytics_summary(self) -> Dict:
        """Get a summary of portfolio analytics"""
        try:
            # Get all data from the sheet
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=f'{self.sheet_name}!A:J'
            ).execute()
            
            values = result.get('values', [])
            if len(values) <= 1:  # Only headers
                return {
                    'total_views': 0,
                    'total_players': 0,
                    'total_quiz_completions': 0,
                    'average_score': 0,
                    'top_players': []
                }
            
            # Process data (skip header row)
            data_rows = values[1:]
            
            total_views = 0
            players = set()
            quiz_completions = 0
            scores = []
            player_scores = {}
            
            for row in data_rows:
                if len(row) >= 4:
                    event_type = row[1] if len(row) > 1 else 'unknown'
                    player_name = row[2] if len(row) > 2 else 'anonymous'
                    score = int(row[3]) if len(row) > 3 and row[3].isdigit() else 0
                    views = int(row[4]) if len(row) > 4 and row[4].isdigit() else 0
                    
                    if event_type == 'portfolio_view':
                        total_views = max(total_views, views)
                    elif event_type == 'player_registration':
                        players.add(player_name)
                    elif event_type == 'quiz_completion':
                        quiz_completions += 1
                        scores.append(score)
                        if player_name not in player_scores:
                            player_scores[player_name] = []
                        player_scores[player_name].append(score)
            
            # Calculate top players
            top_players = []
            for player, player_score_list in player_scores.items():
                if player_score_list:
                    top_players.append({
                        'name': player,
                        'best_score': max(player_score_list),
                        'total_plays': len(player_score_list)
                    })
            
            top_players.sort(key=lambda x: x['best_score'], reverse=True)
            
            return {
                'total_views': total_views,
                'total_players': len(players),
                'total_quiz_completions': quiz_completions,
                'average_score': sum(scores) / len(scores) if scores else 0,
                'top_players': top_players[:5]  # Top 5 players only
            }
            
        except HttpError as error:
            print(f"❌ Error getting analytics: {error}")
            return {}

# Example usage and testing
if __name__ == "__main__":
    # You'll need to set these environment variables or replace with your values
    SPREADSHEET_ID = os.getenv('GOOGLE_SPREADSHEET_ID', 'your-spreadsheet-id-here')
    
    if SPREADSHEET_ID == 'your-spreadsheet-id-here':
        print("⚠️  Please set your GOOGLE_SPREADSHEET_ID environment variable")
        print("   Or replace the SPREADSHEET_ID in this file")
        exit(1)
    
    # Initialize the service
    sheets_service = GoogleSheetsService(SPREADSHEET_ID)
    
    # Create the sheet with headers
    if sheets_service.create_sheet():
        print("🎉 Sheet setup complete!")
        
        # Test with sample data
        test_data = {
            'type': 'portfolio_view',
            'playerName': 'Test User',
            'views': 1,
            'interactions': 5,
            'userAgent': 'Mozilla/5.0 (Test Browser)',
            'url': 'https://example.com'
        }
        
        sheets_service.add_data(test_data)
        
        # Get analytics summary
        summary = sheets_service.get_analytics_summary()
        print(f"📊 Analytics Summary: {summary}")
    else:
        print("❌ Failed to setup sheet")
