# Google Sheets Integration Setup Guide

This guide will help you connect your portfolio to Google Sheets to store analytics data, quiz scores, and player information.

## 📊 What Data Gets Stored

The integration will automatically collect and store:

- **Portfolio Views**: Every time someone visits your portfolio
- **Player Registrations**: When someone enters their name for the quiz
- **Quiz Completions**: Scores, questions answered, achievements earned
- **User Interactions**: Click counts, engagement metrics
- **Technical Data**: User agent, timestamps, page URLs

## 🚀 Setup Steps

### Step 1: Create a Google Sheet

1. Go to [Google Sheets](https://sheets.google.com)
2. Create a new spreadsheet
3. Name it "Portfolio Analytics" (or any name you prefer)
4. Create a sheet tab called "Portfolio Analytics"
5. Add these headers in row 1:
   ```
   A: Timestamp
   B: Event Type
   C: Player Name
   D: Score
   E: Views
   F: Achievements
   G: Interactions
   H: User Agent
   I: URL
   ```

### Step 2: Get Your Spreadsheet ID

1. Open your Google Sheet
2. Look at the URL: `https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit`
3. Copy the `SPREADSHEET_ID` part (the long string between `/d/` and `/edit`)

### Step 3: Enable Google Sheets API

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project or select existing one
3. Enable the Google Sheets API:
   - Go to "APIs & Services" > "Library"
   - Search for "Google Sheets API"
   - Click "Enable"

### Step 4: Create API Credentials

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "API Key"
3. Copy the generated API key
4. (Optional) Restrict the API key to Google Sheets API for security

### Step 5: Configure Your Portfolio

1. Open `index.html` in your portfolio
2. Find the `GOOGLE_CONFIG` section (around line 1231)
3. Replace the placeholder values:

```javascript
const GOOGLE_CONFIG = {
  API_KEY: 'YOUR_ACTUAL_API_KEY_HERE',
  SPREADSHEET_ID: 'YOUR_ACTUAL_SPREADSHEET_ID_HERE',
  SHEET_NAME: 'Portfolio Analytics',
  CLIENT_ID: 'YOUR_GOOGLE_CLIENT_ID' // Optional for OAuth
};
```

### Step 6: Test the Integration

1. Deploy your updated portfolio
2. Visit your portfolio and play the quiz
3. Check your Google Sheet - you should see data appearing
4. Check browser console for any error messages

## 📈 Data Structure

Each row in your Google Sheet will contain:

| Column | Description | Example |
|--------|-------------|---------|
| A | Timestamp | 2025-01-27T10:30:00.000Z |
| B | Event Type | portfolio_view, player_registration, quiz_completion |
| C | Player Name | John Doe, Player1234, anonymous |
| D | Score | 0, 45, 85 |
| E | Views | 1, 15, 42 |
| F | Achievements | 0, 2, 5 |
| G | Interactions | 3, 12, 28 |
| H | User Agent | Mozilla/5.0 (Windows NT 10.0...) |
| I | URL | https://srijaharshikad.github.io/srija-portfolio/ |

## 🔧 Troubleshooting

### Common Issues:

1. **"Google API not loaded"**
   - Check if the Google API script is loading
   - Verify your internet connection

2. **"API key not configured"**
   - Make sure you've replaced `YOUR_GOOGLE_API_KEY` with your actual key
   - Check that the API key is valid

3. **"Permission denied"**
   - Make sure Google Sheets API is enabled in your project
   - Check that your API key has the right permissions

4. **"Spreadsheet not found"**
   - Verify your spreadsheet ID is correct
   - Make sure the sheet tab name matches `SHEET_NAME`

### Debug Mode:

The integration includes console logging. Open browser developer tools (F12) to see:
- API initialization status
- Data being sent to Google Sheets
- Any error messages
- Pending sync data

## 🔒 Security Notes

- **API Key**: Keep your API key secure. Don't commit it to public repositories
- **Rate Limiting**: The integration includes rate limiting to avoid hitting API quotas
- **Fallback Storage**: If Google Sheets is unavailable, data is stored locally and synced later
- **Privacy**: Consider adding a privacy notice about data collection

## 📊 Analytics Dashboard

Once you have data flowing, you can:

1. **Create Charts**: Use Google Sheets' built-in charting tools
2. **Set up Alerts**: Get notified of high engagement
3. **Export Data**: Download CSV files for further analysis
4. **Share Insights**: Give others view-only access to your analytics

## 🚀 Advanced Features

### Custom Events:
You can add custom data collection by calling:

```javascript
sendToGoogleSheets({
  type: 'custom_event',
  playerName: 'John Doe',
  customData: 'any additional info'
});
```

### Batch Sync:
The system automatically syncs pending data when the connection is restored.

### Real-time Monitoring:
Check your Google Sheet regularly to monitor:
- Daily/weekly view trends
- Quiz completion rates
- Player engagement levels
- Popular achievement unlocks

---

**Need Help?** Check the browser console for detailed error messages and debug information.
