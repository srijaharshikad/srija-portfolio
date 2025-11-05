# Srija's Portfolio - Admin Panel

A user-friendly admin interface for managing portfolio content with direct Git integration.

## Features

✅ **Content Management**
- Edit hero section (title, description, tags)
- Create, edit, and delete blog posts
- Manage work experience, projects, and education
- Update contact information

✅ **Blog Management**
- Rich text editor for blog content
- Automatic HTML file generation
- SEO-friendly blog post structure
- Tag and category management

✅ **Git Integration**
- Commit and push changes directly from the admin panel
- Pull latest changes from repository
- View repository status
- Automatic deployment triggers

✅ **File Management**
- Upload images and documents
- Manage portfolio assets
- File organization tools

✅ **Security**
- Password-protected admin access
- Secure API endpoints
- Local-only administration

## Setup Instructions

### Prerequisites
- Node.js (v14 or higher)
- Git repository set up for your portfolio
- Basic knowledge of HTML/CSS (for content editing)

### Installation

1. **Install Dependencies**
   ```bash
   npm install
   ```

2. **Configure Admin Password**
   Edit `admin.html` and change the admin password:
   ```javascript
   const ADMIN_PASSWORD = 'your-secure-password-here';
   ```

3. **Start the Admin Server**
   ```bash
   npm start
   ```
   
   For development with auto-restart:
   ```bash
   npm run dev
   ```

4. **Access Admin Panel**
   Open your browser and go to:
   ```
   http://localhost:3001/admin.html
   ```

### First Time Setup

1. **Login** with your admin password
2. **Update Hero Section** with your information
3. **Create your first blog post** using the blog management interface
4. **Commit changes** using the Git & Deploy section
5. **Verify** your changes on the live site

## Usage Guide

### Managing Content

#### Hero Section
- Update your main title and description
- Add/edit skill tags and specializations
- Changes are immediately reflected on the homepage

#### Blog Management
- **Create New Post**: Click "New Blog Post" button
- **Edit Existing**: Click on any blog post in the list
- **Rich Content**: Use HTML for formatting, links, and media
- **SEO**: Each post gets its own optimized HTML file

#### Git Operations
- **Commit**: Add a descriptive message and commit all changes
- **Push**: Automatically pushes to your main branch
- **Pull**: Get latest changes from remote repository
- **Status**: View current repository state

### Content Structure

#### Blog Posts
Blog posts are stored as individual HTML files with the naming convention:
```
blog-{slug}.html
```

Each blog post includes:
- SEO-optimized meta tags
- Reading progress indicator
- Responsive design
- Back navigation to portfolio

#### File Organization
```
portfolio/
├── index.html          # Main portfolio page
├── admin.html          # Admin interface
├── admin-server.js     # Backend API
├── blog-*.html         # Individual blog posts
├── style.css           # Styles
├── script.js           # Frontend scripts
└── assets/             # Images, documents, etc.
```

## Customization

### Styling
- Edit `admin.html` CSS section for admin panel styling
- Modify blog post template in `admin-server.js`
- Update main site styles in `style.css`

### Functionality
- Add new content sections in `admin.html`
- Extend API endpoints in `admin-server.js`
- Customize Git workflows as needed

### Security
- Change default admin password
- Consider adding HTTPS for production
- Implement session management for enhanced security

## Deployment

### GitHub Pages
1. Ensure your repository is connected to GitHub Pages
2. Use the admin panel to commit and push changes
3. Changes will automatically deploy via GitHub Pages

### Custom Hosting
1. Upload files to your web server
2. Ensure Node.js is available for the admin server
3. Configure domain and SSL as needed

## Troubleshooting

### Common Issues

**Admin panel won't load**
- Check if Node.js server is running on port 3001
- Verify no other services are using the port
- Check browser console for errors

**Git operations fail**
- Ensure Git is properly configured with credentials
- Check repository permissions
- Verify remote repository URL

**Blog posts not appearing**
- Check if HTML files are being generated
- Verify index.html is being updated
- Check for JavaScript errors in browser console

**File uploads fail**
- Check file permissions in portfolio directory
- Verify multer configuration
- Ensure sufficient disk space

### Getting Help

1. Check browser developer console for errors
2. Review server logs in terminal
3. Verify file permissions and Git configuration
4. Test with a simple blog post first

## Security Notes

- The admin panel is designed for local use
- Change the default password immediately
- Don't expose the admin server to public internet without proper security
- Regularly backup your content and repository

## Future Enhancements

- [ ] Rich text editor (WYSIWYG)
- [ ] Image optimization and resizing
- [ ] Content scheduling
- [ ] Analytics integration
- [ ] Multi-user support
- [ ] Content versioning
- [ ] Automated backups

---

**Happy content management!** 🚀

For questions or issues, refer to the troubleshooting section above or check the code comments for implementation details.
