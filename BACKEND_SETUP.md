# Python Backend Setup Guide

This guide will help you set up the Python backend service that connects your portfolio to Google Sheets for analytics data collection.

## 🏗️ Architecture Overview

```
Portfolio Frontend (index.html)
    ↓ (HTTP requests)
Python Flask API (app.py)
    ↓ (Google Sheets API)
Google Sheets (Analytics Data)
```

## 📋 Prerequisites

- Python 3.8 or higher
- Google Cloud Platform account
- Google Sheets API enabled
- A Google Sheet for storing data

## 🚀 Quick Setup

### Step 1: Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### Step 2: Google Cloud Setup

1. **Create a Google Cloud Project:**
   - Go to [Google Cloud Console](https://console.cloud.google.com)
   - Create a new project or select existing one

2. **Enable Google Sheets API:**
   - Go to "APIs & Services" > "Library"
   - Search for "Google Sheets API"
   - Click "Enable"

3. **Create Credentials:**
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"
   - Choose "Desktop application"
   - Download the credentials file as `credentials.json`
   - Place it in the `backend/` directory

### Step 3: Create Google Sheet

1. Go to [Google Sheets](https://sheets.google.com)
2. Create a new spreadsheet
3. Name it "Portfolio Analytics"
4. Copy the spreadsheet ID from the URL:
   ```
   https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit
   ```

### Step 4: Configure Environment

1. Copy the example environment file:
   ```bash
   cp env_example.txt .env
   ```

2. Edit `.env` with your values:
   ```env
   GOOGLE_SPREADSHEET_ID=your-actual-spreadsheet-id-here
   FLASK_ENV=development
   PORT=5000
   ```

### Step 5: Run the Backend

```bash
python app.py
```

You should see:
```
🚀 Starting Portfolio Analytics API...
📊 Spreadsheet ID: your-spreadsheet-id
✅ Google Sheet is ready!
🌐 Server starting on port 5000
```

### Step 6: Test the Setup

1. **Test the API:**
   ```bash
   curl http://localhost:5000/health
   ```

2. **Setup the sheet:**
   ```bash
   curl -X POST http://localhost:5000/api/setup
   ```

3. **Test data collection:**
   ```bash
   curl -X POST http://localhost:5000/api/analytics \
     -H "Content-Type: application/json" \
     -d '{"type":"test","playerName":"Test User","score":100}'
   ```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `GOOGLE_SPREADSHEET_ID` | Your Google Sheet ID | `1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms` |
| `FLASK_ENV` | Flask environment | `development` or `production` |
| `PORT` | Server port | `5000` |

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/api/analytics` | POST | Collect analytics data |
| `/api/analytics/summary` | GET | Get analytics summary |
| `/api/leaderboard` | GET | Get quiz leaderboard |
| `/api/setup` | POST | Setup Google Sheet |

## 📊 Data Structure

The backend collects and stores the following data:

```json
{
  "type": "portfolio_view|player_registration|quiz_completion",
  "playerName": "John Doe",
  "score": 85,
  "views": 42,
  "achievements": 3,
  "interactions": 15,
  "userAgent": "Mozilla/5.0...",
  "url": "https://srijaharshikad.github.io/srija-portfolio/",
  "additionalData": {}
}
```

## 🚀 Deployment Options

### Option 1: Heroku

1. **Install Heroku CLI**
2. **Create Heroku app:**
   ```bash
   heroku create your-portfolio-analytics
   ```

3. **Set environment variables:**
   ```bash
   heroku config:set GOOGLE_SPREADSHEET_ID=your-spreadsheet-id
   heroku config:set FLASK_ENV=production
   ```

4. **Deploy:**
   ```bash
   git add .
   git commit -m "Deploy backend"
   git push heroku main
   ```

### Option 2: Railway

1. **Connect your GitHub repository**
2. **Set environment variables in Railway dashboard**
3. **Deploy automatically**

### Option 3: Google Cloud Run

1. **Create Dockerfile:**
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["python", "app.py"]
   ```

2. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy --source .
   ```

## 🔒 Security Considerations

1. **Credentials:**
   - Never commit `credentials.json` or `token.json` to version control
   - Use environment variables for sensitive data
   - Rotate credentials regularly

2. **API Security:**
   - Add rate limiting for production
   - Implement CORS properly
   - Add authentication if needed

3. **Data Privacy:**
   - Consider GDPR compliance
   - Add data retention policies
   - Implement data anonymization

## 🐛 Troubleshooting

### Common Issues:

1. **"Credentials not found"**
   - Make sure `credentials.json` is in the backend directory
   - Check file permissions

2. **"Spreadsheet not found"**
   - Verify the spreadsheet ID is correct
   - Check if the sheet exists and is accessible

3. **"Permission denied"**
   - Make sure Google Sheets API is enabled
   - Check OAuth consent screen configuration

4. **"Port already in use"**
   - Change the PORT in your `.env` file
   - Kill existing processes on that port

### Debug Mode:

Run with debug logging:
```bash
FLASK_ENV=development python app.py
```

Check logs for detailed error messages.

## 📈 Monitoring

### Health Checks:
```bash
curl http://localhost:5000/health
```

### Analytics Summary:
```bash
curl http://localhost:5000/api/analytics/summary
```

### Leaderboard:
```bash
curl http://localhost:5000/api/leaderboard
```

## 🔄 Frontend Integration

Update your portfolio's `index.html` to point to your deployed backend:

```javascript
const API_CONFIG = {
  BASE_URL: 'https://your-backend-url.herokuapp.com', // Your deployed URL
  ENDPOINTS: {
    ANALYTICS: '/api/analytics',
    SUMMARY: '/api/analytics/summary',
    LEADERBOARD: '/api/leaderboard',
    SETUP: '/api/setup'
  }
};
```

## 📊 Google Sheets Structure

Your Google Sheet will have these columns:

| A | B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|---|
| Timestamp | Event Type | Player Name | Score | Views | Achievements | Interactions | User Agent | URL | Additional Data |

## 🎯 Next Steps

1. **Deploy the backend** to your preferred platform
2. **Update the frontend** with your backend URL
3. **Test the integration** with real data
4. **Monitor analytics** in your Google Sheet
5. **Set up alerts** for high engagement

---

**Need Help?** Check the console logs and Google Cloud Console for detailed error messages.
