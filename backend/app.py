"""
Flask API Server for Portfolio Analytics
Handles data collection from the portfolio frontend
"""

import os
import json
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

from sheets_service import GoogleSheetsService

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

# Initialize Google Sheets service
SPREADSHEET_ID = os.getenv('GOOGLE_SPREADSHEET_ID')
if not SPREADSHEET_ID:
    print("⚠️  GOOGLE_SPREADSHEET_ID not found in environment variables")
    print("   Please create a .env file with your spreadsheet ID")
    exit(1)

sheets_service = GoogleSheetsService(SPREADSHEET_ID)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Portfolio Analytics API'
    })

@app.route('/api/analytics', methods=['POST'])
def collect_analytics():
    """Collect analytics data from the portfolio"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Add additional metadata
        data['userAgent'] = request.headers.get('User-Agent', '')
        data['url'] = request.headers.get('Referer', '')
        data['timestamp'] = datetime.now().isoformat()
        
        # Send to Google Sheets
        success = sheets_service.add_data(data)
        
        if success:
            return jsonify({
                'status': 'success',
                'message': 'Data collected successfully',
                'timestamp': data['timestamp']
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Failed to store data'
            }), 500
            
    except Exception as e:
        print(f"❌ Error in collect_analytics: {e}")
        return jsonify({
            'status': 'error',
            'message': 'Internal server error'
        }), 500

@app.route('/api/analytics/summary', methods=['GET'])
def get_analytics_summary():
    """Get analytics summary from Google Sheets"""
    try:
        summary = sheets_service.get_analytics_summary()
        return jsonify({
            'status': 'success',
            'data': summary,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        print(f"❌ Error getting analytics summary: {e}")
        return jsonify({
            'status': 'error',
            'message': 'Failed to get analytics summary'
        }), 500

@app.route('/api/leaderboard', methods=['GET'])
def get_leaderboard():
    """Get quiz leaderboard data"""
    try:
        summary = sheets_service.get_analytics_summary()
        leaderboard = summary.get('top_players', [])
        
        return jsonify({
            'status': 'success',
            'data': {
                'leaderboard': leaderboard,
                'total_players': summary.get('total_players', 0),
                'total_completions': summary.get('total_quiz_completions', 0)
            },
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        print(f"❌ Error getting leaderboard: {e}")
        return jsonify({
            'status': 'error',
            'message': 'Failed to get leaderboard'
        }), 500

@app.route('/api/setup', methods=['POST'])
def setup_sheet():
    """Setup the Google Sheet with headers"""
    try:
        success = sheets_service.create_sheet()
        
        if success:
            return jsonify({
                'status': 'success',
                'message': 'Sheet setup completed successfully'
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Failed to setup sheet'
            }), 500
            
    except Exception as e:
        print(f"❌ Error setting up sheet: {e}")
        return jsonify({
            'status': 'error',
            'message': 'Failed to setup sheet'
        }), 500

if __name__ == '__main__':
    # Setup the sheet on startup
    print("🚀 Starting Portfolio Analytics API...")
    print(f"📊 Spreadsheet ID: {SPREADSHEET_ID}")
    
    # Create the sheet with headers
    if sheets_service.create_sheet():
        print("✅ Google Sheet is ready!")
    else:
        print("❌ Failed to setup Google Sheet")
    
    # Start the Flask server
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    print(f"🌐 Server starting on port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug)
