# Admin Panel Troubleshooting Guide

## "Connect to GitHub" Button Not Working

### Step 1: Open Browser Console
1. Go to https://srijaharshikad.github.io/srija-portfolio/admin-github.html
2. Press **F12** (or right-click → Inspect)
3. Click the **Console** tab
4. You should see debug messages when the page loads:
   ```
   Admin panel loaded!
   Connect button found: true
   Loaded stored credentials (if you had saved them before)
   ```

### Step 2: Try Connecting Again
1. Enter your GitHub token: `ghp_xxxxxxxxxxxxxxxxxxxx` (your personal access token)
2. Enter your repository: `srijaharshikad/srija-portfolio`
3. Click "Connect to GitHub"
4. Watch the console - you should see:
   ```
   Connect button clicked!
   Token length: 40
   Repo: srijaharshikad/srija-portfolio
   Testing GitHub API connection...
   Response status: 200
   Connected successfully!
   ```

### Step 3: Check for Errors

#### Error: "Network error" or "Failed to fetch"
**Cause**: CORS issue or network problem
**Solution**: 
- Make sure you're accessing the page via HTTPS (GitHub Pages URL)
- Check your internet connection
- Try a different browser

#### Error: "401 Unauthorized"
**Cause**: Invalid GitHub token
**Solution**:
1. Go to https://github.com/settings/tokens
2. Create a new token with **repo** permissions
3. Copy the new token and try again

#### Error: "404 Not Found"
**Cause**: Repository name is incorrect
**Solution**:
- Make sure repository is: `srijaharshikad/srija-portfolio` (exact spelling, lowercase)
- Check that the repository exists on GitHub

#### Error: "Token expired"
**Cause**: Your Personal Access Token has expired
**Solution**:
1. Go to https://github.com/settings/tokens
2. Generate a new token
3. Make sure to check "repo" permissions
4. Copy and use the new token

### Step 4: Clear Cached Credentials
If you had previously entered wrong credentials:
1. Open browser console (F12)
2. Type: `localStorage.clear()`
3. Press Enter
4. Refresh the page
5. Try entering credentials again

### Step 5: Force Reload
The GitHub Pages cache might be serving an old version:
1. Press **Ctrl+Shift+R** (Windows/Linux) or **Cmd+Shift+R** (Mac)
2. This forces a fresh download of the page
3. Try connecting again

## Still Not Working?

### Test Your Token Manually
1. Open a new browser tab
2. Open Console (F12 → Console)
3. Paste this code (replace YOUR_TOKEN with your actual token):
   ```javascript
   fetch('https://api.github.com/repos/srijaharshikad/srija-portfolio', {
     headers: {
       'Authorization': 'token YOUR_TOKEN',
       'Accept': 'application/vnd.github.v3+json'
     }
   }).then(r => r.json()).then(d => console.log(d));
   ```
4. If this works, you should see your repository data
5. If this fails, the problem is with your token

### Common Issues and Quick Fixes

| Issue | Solution |
|-------|----------|
| Button doesn't respond at all | Hard refresh the page (Ctrl+Shift+R) |
| "Token is invalid" | Create a new token with 'repo' permissions |
| "Repository not found" | Check spelling: srijaharshikad/srija-portfolio |
| Page shows 404 | Wait 1-2 minutes for GitHub Pages to deploy |
| Button shows "Connecting..." forever | Check browser console for errors |

## What the Fixed Version Does

The updated admin panel now:
1. ✅ Shows **loading spinner** when connecting
2. ✅ Logs debug messages to console
3. ✅ Displays specific error messages
4. ✅ Disables button while connecting
5. ✅ Supports **Enter key** to submit
6. ✅ Better error handling

## Need More Help?

If you see any errors in the console, copy them and we can investigate further!

