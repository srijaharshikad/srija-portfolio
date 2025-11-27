# Portfolio Admin Panel Guide

## 🎯 How to Edit Your Portfolio Sections

Your admin panel now has editors for **every section** of your portfolio!

### 📍 Access Your Admin Panel

**URL**: https://srijaharshikad.github.io/srija-portfolio/admin-github.html

**Login**:
- Token: `ghp_xxxxxxxxxxxxxxxxxxxx` (your GitHub token)
- Repository: `srijaharshikad/srija-portfolio` (note the 'd' at the end!)

---

## 📝 Available Editors

### 1. **Hero / About Me** 🎭
Edit your main introduction section:
- Education badge (e.g., "ISB MBA — Strategy & Leadership, Marketing")
- Main title line 1 (e.g., "Senior Product")
- Main title line 2 - highlighted (e.g., "Manager · AI/ML")
- Description paragraph

**How to use**:
1. Click "Hero / About Me" in the sidebar
2. Fill in the fields
3. Click "Save Hero Section"
4. Changes go live immediately!

---

### 2. **Work Experience** 💼
Manage your job history:
- Click "Work Experience" in sidebar
- Click "Load Current Work Experience" to see what's there now
- Edit the HTML directly
- Click "Save Work Experience"

**Tip**: For complex formatting, use the "Advanced Editor" section to get the full HTML and make detailed changes.

---

### 3. **Projects** 📂
Showcase your project portfolio:
- Click "Projects" in sidebar
- Click "Load Current Projects"
- Edit the project HTML
- Click "Save Projects"

---

### 4. **Education** 🎓
Update your educational background:
- Click "Education" in sidebar
- Click "Load Current Education"
- Edit the education HTML
- Click "Save Education"

---

### 5. **Resume Link** 📄
**This is what you asked about!** Update your resume button:

**Steps**:
1. Click "Resume Link" in the sidebar
2. First, upload your new resume PDF:
   - Go to "File Manager"
   - Upload your `resume.pdf` file
3. Come back to "Resume Link"
4. Enter the file path: `./resume.pdf`
5. (Optional) Change the button text
6. Click "Save Resume Link"
7. Click "Test Link" to verify it works!

**Example Resume URLs**:
- Local file: `./resume.pdf`
- Google Drive: `https://drive.google.com/file/d/YOUR_FILE_ID/view`
- Dropbox: `https://www.dropbox.com/s/YOUR_FILE/resume.pdf`

---

### 6. **Blog Posts** ✍️
Create and publish blog articles:
- Click "Blog Posts" in sidebar
- Fill in title, date, tags, content
- Click "Publish Blog Post"
- It creates a new blog page and adds it to your portfolio!

---

### 7. **Advanced Editor** 🔧
For power users:
- Direct access to your `index.html` file
- Make any changes to any part of your portfolio
- Full HTML editing capability

**How to use**:
1. Click "Advanced Editor"
2. Click "Load index.html"
3. Edit the HTML code
4. Click "Save Changes"

---

### 8. **File Manager** 📁
Upload and manage files:
- Upload images, PDFs, documents
- Get file URLs for use in your portfolio
- Delete old files
- Upload new resume versions here!

---

## 🚀 Quick Workflow Examples

### Example 1: Update Resume
```
1. Go to admin panel
2. Click "File Manager" → Upload your new resume.pdf
3. Click "Resume Link"
4. Enter: ./resume.pdf
5. Click "Save Resume Link"
6. Done! Resume button now points to new file
```

### Example 2: Add New Job
```
1. Click "Work Experience"
2. Click "Load Current Work Experience"
3. Copy the HTML format of an existing job entry
4. Paste and edit with your new job details
5. Click "Save Work Experience"
```

### Example 3: Update Hero Section
```
1. Click "Hero / About Me"
2. Change your title or description
3. Click "Save Hero Section"
4. Refresh your portfolio to see changes
```

---

## ⚡ Tips & Best Practices

### Tip 1: Always Load First
Before editing Work/Projects/Education, always click the "Load" button to see the current content.

### Tip 2: Test Changes
After saving, open your portfolio in a new tab to verify changes look good.

### Tip 3: Use Advanced Editor for Complex Changes
If you need to change multiple sections at once or make complex formatting changes, use the "Advanced Editor".

### Tip 4: Keep Backups
Before making major changes, you can:
1. Go to Advanced Editor
2. Load index.html
3. Copy the entire content
4. Save it locally as a backup

### Tip 5: Resume Best Practices
- Name your file clearly: `resume.pdf` or `srija-harshika-resume.pdf`
- Keep it under 5MB for fast loading
- Always test the link after updating!

---

## 🎨 Editing Navigation Tabs

Your portfolio has these tabs in the header:
- Work
- Projects  
- Blog
- Education
- In Their Words
- Contact
- Resume (button)

**To change tab text/links**:
1. Go to "Advanced Editor"
2. Click "Load index.html"
3. Find the `<nav>` section (usually near the top)
4. Edit the link text or hrefs
5. Save changes

**Example nav structure to look for**:
```html
<nav>
  <a href="#work">Work</a>
  <a href="#projects">Projects</a>
  <a href="#blog">Blog</a>
  ...
</nav>
```

---

## 🔄 How Changes Work

1. **You edit** → Admin panel
2. **Changes saved** → GitHub repository
3. **Automatically deployed** → GitHub Pages (takes 1-2 minutes)
4. **Live on your site** → Portfolio updates

**Wait time**: 1-2 minutes for changes to appear live.

---

## ❓ Troubleshooting

### Changes not showing?
- Wait 2 minutes for GitHub Pages to rebuild
- Hard refresh your portfolio: Ctrl+Shift+R (or Cmd+Shift+R on Mac)

### Can't connect?
- Check your repository name: `srijaharshikad/srija-portfolio` (with the 'd'!)
- Verify your GitHub token hasn't expired

### Error saving?
- Check browser console (F12) for specific errors
- Make sure your HTML is valid (no unclosed tags)

---

## 🎉 You're All Set!

You now have complete control over your portfolio without touching code! 

**Bookmark this**: https://srijaharshikad.github.io/srija-portfolio/admin-github.html

