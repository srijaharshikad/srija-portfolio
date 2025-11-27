# 🚀 Quick Start Guide - Edit Your Portfolio

## 📍 Your Admin Panel URL
**https://srijaharshikad.github.io/srija-portfolio/admin-github.html**

⚠️ **Important**: Use `srijaharshikad` (with 'd' at the end) - not `srijaharshika`!

---

## 🎯 What You Asked For - Now Available!

### ✅ 1. **Replace Hero Image** (Your Photo)
1. Go to admin panel → **"Hero / About Me"**
2. Click **"Load Current Data"** button
3. Scroll to **"📸 Hero Image"** section
4. First, upload your new image:
   - Go to **"File Manager"** tab
   - Upload your new photo (e.g., `new-headshot.jpg`)
5. Come back to **"Hero / About Me"**
6. Enter the image path: `./new-headshot.jpg`
7. **Preview updates instantly** in the left panel!
8. Click **"Save Hero Section"**

### ✅ 2. **Change Links in Buttons** (Contact, LinkedIn, Topmate)
1. Go to admin panel → **"Hero / About Me"**
2. Click **"Load Current Data"**
3. Scroll to **"🔗 Action Buttons"** section
4. Edit any button:
   - **Button 1** (Contact): Text + Link
   - **Button 2** (LinkedIn): Text + Link
   - **Button 3** (Topmate): Text + Link
5. Want to add more buttons? Use the **"Advanced Editor"** section
6. Click **"Save Hero Section"**

**Example - Change Button 3 to GitHub**:
- Button 3 Text: `GitHub`
- Button 3 Link: `https://github.com/yourusername`

### ✅ 3. **Update Tags/Pills** (GenAI · Agents, RAG, etc.)
1. Go to admin panel → **"Hero / About Me"**
2. Click **"Load Current Data"**
3. Scroll to **"🏷️ Skills Tags (Pills)"** section
4. Edit all 4 tags:
   - Tag 1: `GenAI · Agents` → Change to anything!
   - Tag 2: `RAG · Gemini · LangChain` → Your choice
   - Tag 3: `Evaluation & Guardrails` → Customize
   - Tag 4: `0→1 Delivery` → Your skill
5. Click **"Save Hero Section"**

**Tip**: Use ` · ` (space-dot-space) to separate multiple items in one tag

### ✅ 4. **Update Resume Link**
1. Go to admin panel → **"Resume Link"**
2. Upload your new resume in **"File Manager"** first
3. Enter the file path: `./resume.pdf`
4. (Optional) Change button text
5. Click **"Test Link"** to verify
6. Click **"Save Resume Link"**

---

## 🤖 Chatbot & Game Content

### Chatbot (AI Assistant) 💬
The chatbot at the bottom right of your portfolio can be edited:

**What to Edit**:
- Greeting message
- Knowledge base (responses about you)
- Quick reply buttons
- Personality/tone

**How to Edit**:
1. Go to **"Advanced Editor"**
2. Click **"Load index.html"**
3. Search for: `chatResponses` (Ctrl+F)
4. You'll find all the chatbot content
5. Edit the responses and follow-up questions
6. Save changes

**Example Chatbot Response to Edit**:
```javascript
'jia': {
  response: "Your custom response here about JIA...",
  followUps: ["Question 1?", "Question 2?", "Question 3?"]
}
```

### Game (AI Quiz) 🎮
The game button at the bottom left can be customized:

**What to Edit**:
- Quiz questions
- Answer options
- Correct answers
- Game title
- Achievement text

**How to Edit**:
1. Go to **"Advanced Editor"**
2. Click **"Load index.html"**
3. Search for: `const questions = [` (Ctrl+F)
4. Edit the questions array
5. Save changes

**Example Question to Edit**:
```javascript
{
  question: "Your question here?",
  options: ["Option A", "Option B", "Option C", "Option D"],
  correct: 0 // Index of correct answer (0 = first option)
}
```

---

## 🎨 Complete List of What You Can Edit

| Section | What You Can Change | Where to Edit |
|---------|-------------------|---------------|
| **Hero Image** | Your photo/headshot | Hero / About Me → Image URL |
| **Education Badge** | The graduation badge text | Hero / About Me → Education Badge |
| **Main Title** | "Senior Product Manager · AI/ML" | Hero / About Me → Main Title |
| **Description** | Your intro paragraph | Hero / About Me → Description |
| **Tags/Pills** | GenAI, RAG, etc. (all 4 tags) | Hero / About Me → Skills Tags |
| **Buttons** | Contact, LinkedIn, Topmate links | Hero / About Me → Action Buttons |
| **Work Experience** | All job entries | Work Experience → Load & Edit |
| **Projects** | Project showcase | Projects → Load & Edit |
| **Education** | Schools and degrees | Education → Load & Edit |
| **Blog Posts** | Create new articles | Blog Posts → New Post |
| **Resume Link** | PDF download button | Resume Link → URL |
| **Chatbot** | AI assistant responses | Advanced Editor → Search `chatResponses` |
| **Game** | Quiz questions & answers | Advanced Editor → Search `questions` |
| **Navigation** | Header menu tabs | Advanced Editor → Search `<nav>` |
| **Footer** | Bottom section | Advanced Editor → Search `<footer>` |

---

## 💡 Pro Tips

### Tip 1: Always Load First
Before editing any section, click the **"Load Current Data"** or **"Load..."** button to see what's there now.

### Tip 2: Use File Manager for Images
**Workflow for adding any image**:
1. Go to **"File Manager"**
2. Upload your image file
3. Copy the filename (e.g., `my-image.jpg`)
4. Use it as: `./my-image.jpg` in your editors

### Tip 3: Preview Before Saving
- Hero section has **live preview** of your image
- Use **"Test Link"** buttons when available
- Check your changes in a new tab after saving

### Tip 4: Complex Edits? Use Advanced Editor
For anything not covered by the simple editors:
1. Go to **"Advanced Editor"**
2. Click **"Load index.html"**
3. Use Ctrl+F (Find) to search for the text you want to change
4. Edit directly in HTML
5. Save

### Tip 5: Changes Take Time
After clicking save:
- Wait **1-2 minutes** for GitHub Pages to rebuild
- **Hard refresh** your portfolio: **Ctrl+Shift+R** (or Cmd+Shift+R on Mac)

---

## 🔧 Common Tasks

### Change Your LinkedIn URL
```
1. Hero / About Me → Load Current Data
2. Action Buttons → Button 2 Link
3. Replace with your LinkedIn URL
4. Save Hero Section
```

### Update All Your Tags at Once
```
1. Hero / About Me → Load Current Data
2. Skills Tags section
3. Edit Tag 1, 2, 3, 4
4. Save Hero Section
```

### Add a New Photo
```
1. File Manager → Upload new-photo.jpg
2. Hero / About Me → Image URL
3. Type: ./new-photo.jpg
4. See preview update immediately
5. Save Hero Section
```

### Change Resume Button Text
```
1. Resume Link
2. Resume File URL: ./resume.pdf
3. Button Text: "Download CV" (or anything!)
4. Test Link
5. Save Resume Link
```

---

## 🆘 Troubleshooting

### Changes not showing?
- **Wait 2 minutes** for deployment
- **Hard refresh**: Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac)
- Check browser console (F12) for errors

### Can't connect to admin panel?
- Use `srijaharshikad/srija-portfolio` (with the **'d'**!)
- Check your GitHub token hasn't expired
- Try clearing browser cache

### Image not showing?
- Make sure you uploaded the file to File Manager first
- Use the correct path: `./filename.jpg` (with the dot-slash)
- Check the file extension matches (jpg vs jpeg vs png)

### Button link not working?
- External links need `https://` at the start
- Internal links use `#section-name` format
- Use **"Test Link"** button to verify

---

## 📚 Full Documentation

For more details, see:
- **ADMIN-GUIDE.md** - Complete feature guide
- **ADMIN-TROUBLESHOOTING.md** - Detailed troubleshooting
- **GITHUB-SETUP.md** - Initial setup info

---

## ✨ You're All Set!

**Your portfolio is now fully editable!** 🎉

Everything you asked for:
- ✅ Replace image (your photo)
- ✅ Change links (Contact, LinkedIn, Topmate)
- ✅ Update tags (GenAI, RAG, etc.)
- ✅ Edit chatbot responses
- ✅ Customize game content
- ✅ Update resume link
- ✅ And much more!

**Bookmark your admin panel**: https://srijaharshikad.github.io/srija-portfolio/admin-github.html

Happy editing! 🚀

