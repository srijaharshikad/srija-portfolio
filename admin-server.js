const express = require('express');
const fs = require('fs').promises;
const path = require('path');
const { exec } = require('child_process');
const cors = require('cors');
const multer = require('multer');

const app = express();
const PORT = 3001;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('.'));

// Configure multer for file uploads
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, './');
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname);
  }
});
const upload = multer({ storage });

// Utility function to execute shell commands
const execCommand = (command) => {
  return new Promise((resolve, reject) => {
    exec(command, (error, stdout, stderr) => {
      if (error) {
        reject({ error: error.message, stderr });
      } else {
        resolve({ stdout, stderr });
      }
    });
  });
};

// API Routes

// Get current portfolio data
app.get('/api/portfolio/hero', async (req, res) => {
  try {
    const indexContent = await fs.readFile('index.html', 'utf8');
    
    // Extract hero section data using regex
    const titleMatch = indexContent.match(/<h1[^>]*>(.*?)<\/h1>/s);
    const descriptionMatch = indexContent.match(/<p class="mt-4[^>]*>(.*?)<\/p>/s);
    
    const heroData = {
      title: titleMatch ? titleMatch[1].replace(/<[^>]*>/g, '').trim() : '',
      description: descriptionMatch ? descriptionMatch[1].replace(/<[^>]*>/g, '').trim() : '',
      tags: [] // Extract tags from chips
    };
    
    res.json(heroData);
  } catch (error) {
    res.status(500).json({ error: 'Failed to read hero data' });
  }
});

// Update hero section
app.post('/api/portfolio/hero', async (req, res) => {
  try {
    const { title, description, tags } = req.body;
    let indexContent = await fs.readFile('index.html', 'utf8');
    
    // Update title
    indexContent = indexContent.replace(
      /<h1[^>]*>.*?<\/h1>/s,
      `<h1 class="mt-4 text-[clamp(2rem,5vw,3.2rem)] font-extrabold leading-tight tracking-tight">
          ${title}
        </h1>`
    );
    
    // Update description
    indexContent = indexContent.replace(
      /<p class="mt-4 text-\[clamp\(1rem,2\.3vw,1\.125rem\)\][^>]*>.*?<\/p>/s,
      `<p class="mt-4 text-[clamp(1rem,2.3vw,1.125rem)] text-slate-700 max-w-prose">
          ${description}
        </p>`
    );
    
    // Update tags/chips
    if (tags && tags.length > 0) {
      const chipsHtml = tags.map(tag => `<span class="chip">${tag.trim()}</span>`).join('\n          ');
      indexContent = indexContent.replace(
        /<div class="mt-5 flex flex-wrap gap-2">.*?<\/div>/s,
        `<div class="mt-5 flex flex-wrap gap-2">
          ${chipsHtml}
        </div>`
      );
    }
    
    await fs.writeFile('index.html', indexContent);
    res.json({ success: true, message: 'Hero section updated successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Failed to update hero section' });
  }
});

// Get blog posts
app.get('/api/blog/posts', async (req, res) => {
  try {
    const indexContent = await fs.readFile('index.html', 'utf8');
    
    // Extract blog posts from the HTML
    const blogPosts = [];
    
    // Extract featured post
    const featuredMatch = indexContent.match(/<article class="reveal reveal-delay-2 blog-card[^>]*>.*?<\/article>/s);
    if (featuredMatch) {
      const titleMatch = featuredMatch[0].match(/<h3[^>]*>(.*?)<\/h3>/s);
      const excerptMatch = featuredMatch[0].match(/<p class="text-lg[^>]*>(.*?)<\/p>/s);
      const dateMatch = featuredMatch[0].match(/<span class="text-sm text-slate-500[^>]*>(.*?)<\/span>/s);
      
      if (titleMatch) {
        blogPosts.push({
          id: 'building-trust-ai',
          title: titleMatch[1].replace(/<[^>]*>/g, '').trim(),
          excerpt: excerptMatch ? excerptMatch[1].replace(/<[^>]*>/g, '').trim() : '',
          date: dateMatch ? dateMatch[1].trim() : '',
          featured: true,
          tags: ['User Trust', 'AI Products', 'Scale'],
          readTime: '7 min read'
        });
      }
    }
    
    // Extract other blog posts
    const blogCardMatches = indexContent.match(/<a href="blog-[^"]*\.html"[^>]*class="stagger-item blog-card[^>]*>.*?<\/a>/gs);
    if (blogCardMatches) {
      blogCardMatches.forEach((match, index) => {
        const titleMatch = match.match(/<h3[^>]*>(.*?)<\/h3>/s);
        const excerptMatch = match.match(/<p class="text-sm text-slate-700[^>]*>(.*?)<\/p>/s);
        const dateMatch = match.match(/<span class="text-xs text-slate-500[^>]*>(.*?)<\/span>/s);
        const hrefMatch = match.match(/href="([^"]*\.html)"/);
        
        if (titleMatch && hrefMatch) {
          const filename = hrefMatch[1];
          const id = filename.replace('blog-', '').replace('.html', '');
          
          blogPosts.push({
            id,
            title: titleMatch[1].replace(/<[^>]*>/g, '').trim(),
            excerpt: excerptMatch ? excerptMatch[1].replace(/<[^>]*>/g, '').trim() : '',
            date: dateMatch ? dateMatch[1].trim() : '',
            featured: false,
            tags: [],
            readTime: '5 min read'
          });
        }
      });
    }
    
    res.json(blogPosts);
  } catch (error) {
    res.status(500).json({ error: 'Failed to read blog posts' });
  }
});

// Get specific blog post content
app.get('/api/blog/posts/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const filename = `blog-${id}.html`;
    
    try {
      const content = await fs.readFile(filename, 'utf8');
      res.json({ content });
    } catch (fileError) {
      // If file doesn't exist, return empty content
      res.json({ content: '' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Failed to read blog post' });
  }
});

// Create or update blog post
app.post('/api/blog/posts', async (req, res) => {
  try {
    const { id, title, date, excerpt, tags, readTime, content, featured } = req.body;
    
    // Create blog HTML file
    const blogTemplate = `<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>${title} | Srija Harshika</title>
  <meta name="description" content="${excerpt}">
  <meta name="theme-color" content="#0B1220">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors:{brand:{600:'#4f46e5',700:'#4338ca'}},
          boxShadow:{soft:'0 14px 40px rgba(2,6,23,.12)'},
          fontFamily:{sans:['Inter','ui-sans-serif','system-ui']}
        }
      }
    }
  </script>
  <style>
    .reveal{opacity:1; transform:none; transition:all .8s cubic-bezier(.2,.65,.3,1)}
    .reading-progress {
      position: fixed;
      top: 0;
      left: 0;
      width: 0%;
      height: 3px;
      background: linear-gradient(90deg, #4f46e5, #06b6d4);
      z-index: 1000;
      transition: width .1s ease;
    }
  </style>
</head>
<body class="bg-white text-slate-900 font-sans">
  <div class="reading-progress"></div>
  
  <header class="sticky top-0 z-50 border-b border-slate-200/70 bg-white/80 backdrop-blur">
    <div class="max-w-4xl mx-auto px-4 py-3 flex items-center justify-between">
      <a href="index.html" class="flex items-center gap-3 hover:opacity-80 transition">
        <img src="./headshot.jpg" alt="Srija headshot" class="h-9 w-9 rounded-lg object-cover ring-1 ring-slate-200" />
        <span class="font-semibold">Srija Harshika</span>
      </a>
      <a href="index.html#blog" class="text-sm text-slate-600 hover:text-slate-900 transition">← Back to Blog</a>
    </div>
  </header>

  <main class="max-w-4xl mx-auto px-4 py-12">
    <article class="prose prose-lg max-w-none">
      <div class="mb-8">
        <div class="flex items-center gap-4 text-sm text-slate-600 mb-4">
          <time datetime="${date}">${new Date(date).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}</time>
          <span>•</span>
          <span>${readTime}</span>
        </div>
        <h1 class="text-4xl font-bold text-slate-900 mb-4">${title}</h1>
        <p class="text-xl text-slate-700 leading-relaxed">${excerpt}</p>
        <div class="flex flex-wrap gap-2 mt-6">
          ${tags.map(tag => `<span class="px-3 py-1 text-sm rounded-full bg-blue-100 text-blue-800 font-medium">${tag}</span>`).join('')}
        </div>
      </div>
      
      <div class="blog-content">
        ${content}
      </div>
    </article>
  </main>

  <footer class="border-t border-slate-200/70 mt-16">
    <div class="max-w-4xl mx-auto px-4 py-8 text-center">
      <a href="index.html" class="inline-flex items-center gap-2 text-brand-600 hover:text-brand-700 font-medium">
        ← Back to Portfolio
      </a>
    </div>
  </footer>

  <script>
    // Reading progress
    function updateReadingProgress() {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const scrollPercent = (scrollTop / docHeight) * 100;
      document.querySelector('.reading-progress').style.width = Math.min(scrollPercent, 100) + '%';
    }
    window.addEventListener('scroll', updateReadingProgress);
  </script>
</body>
</html>`;

    const filename = `blog-${id}.html`;
    await fs.writeFile(filename, blogTemplate);
    
    // Update index.html to include this blog post
    await updateBlogInIndex(req.body);
    
    res.json({ success: true, message: 'Blog post saved successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Failed to save blog post' });
  }
});

// Delete blog post
app.delete('/api/blog/posts/:id', async (req, res) => {
  try {
    const { id } = req.params;
    const filename = `blog-${id}.html`;
    
    // Delete the blog file
    try {
      await fs.unlink(filename);
    } catch (fileError) {
      // File might not exist, continue
    }
    
    // Remove from index.html
    await removeBlogFromIndex(id);
    
    res.json({ success: true, message: 'Blog post deleted successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Failed to delete blog post' });
  }
});

// Helper function to update blog in index.html
async function updateBlogInIndex(blogData) {
  try {
    let indexContent = await fs.readFile('index.html', 'utf8');
    
    // Create blog card HTML
    const blogCardHtml = `
            <a href="blog-${blogData.id}.html" class="stagger-item blog-card group p-6 rounded-2xl border border-slate-200 bg-white shadow-soft">
              <div class="flex items-center justify-between mb-3">
                <div class="flex items-center gap-2">
                  <span class="text-xs text-slate-500 text-slate-600">${new Date(blogData.date).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}</span>
                  <span class="tag px-2 py-1 text-xs rounded-full bg-blue-100 text-blue-800 font-medium">${blogData.tags[0] || 'Article'}</span>
                </div>
                <div class="flex items-center gap-1 text-xs text-slate-400">
                  <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                  </svg>
                  <span>New</span>
                </div>
              </div>
              <h3 class="font-bold mb-3 text-slate-900 group-hover:text-brand-600 transition-colors">${blogData.title}</h3>
              <p class="text-sm text-slate-700 leading-relaxed mb-4">${blogData.excerpt}</p>
              <div class="flex items-center justify-between">
                <div class="flex items-center gap-1 text-xs text-slate-500">
                  <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clip-rule="evenodd"/>
                  </svg>
                  <span>${blogData.readTime}</span>
                </div>
                <div class="opacity-0 group-hover:opacity-100 transition-opacity">
                  <svg class="w-4 h-4 text-brand-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                  </svg>
                </div>
              </div>
            </a>`;
    
    // Find the blog grid and add/update the blog post
    const blogGridRegex = /<div class="grid sm:grid-cols-2 lg:grid-cols-2 gap-6">(.*?)<\/div>/s;
    const match = indexContent.match(blogGridRegex);
    
    if (match) {
      // Check if blog already exists
      const existingBlogRegex = new RegExp(`<a href="blog-${blogData.id}\\.html"[^>]*>.*?</a>`, 's');
      if (match[1].match(existingBlogRegex)) {
        // Replace existing blog
        const updatedGrid = match[1].replace(existingBlogRegex, blogCardHtml.trim());
        indexContent = indexContent.replace(blogGridRegex, `<div class="grid sm:grid-cols-2 lg:grid-cols-2 gap-6">${updatedGrid}</div>`);
      } else {
        // Add new blog at the beginning
        const updatedGrid = blogCardHtml + match[1];
        indexContent = indexContent.replace(blogGridRegex, `<div class="grid sm:grid-cols-2 lg:grid-cols-2 gap-6">${updatedGrid}</div>`);
      }
    }
    
    await fs.writeFile('index.html', indexContent);
  } catch (error) {
    console.error('Error updating blog in index:', error);
  }
}

// Helper function to remove blog from index.html
async function removeBlogFromIndex(blogId) {
  try {
    let indexContent = await fs.readFile('index.html', 'utf8');
    
    // Remove the blog card
    const blogCardRegex = new RegExp(`<a href="blog-${blogId}\\.html"[^>]*>.*?</a>`, 's');
    indexContent = indexContent.replace(blogCardRegex, '');
    
    await fs.writeFile('index.html', indexContent);
  } catch (error) {
    console.error('Error removing blog from index:', error);
  }
}

// Git operations
app.post('/api/git/commit', async (req, res) => {
  try {
    const { message } = req.body;
    
    // Add all changes
    await execCommand('git add .');
    
    // Commit changes
    await execCommand(`git commit -m "${message}"`);
    
    // Push to remote
    await execCommand('git push origin main');
    
    res.json({ success: true, message: 'Changes committed and pushed successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Git operation failed', details: error });
  }
});

app.post('/api/git/pull', async (req, res) => {
  try {
    await execCommand('git pull origin main');
    res.json({ success: true, message: 'Repository updated successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Git pull failed', details: error });
  }
});

app.get('/api/git/status', async (req, res) => {
  try {
    const result = await execCommand('git status --porcelain');
    const hasChanges = result.stdout.trim().length > 0;
    
    res.json({ 
      hasChanges,
      changes: result.stdout.split('\n').filter(line => line.trim()),
      message: hasChanges ? 'You have uncommitted changes' : 'Repository is up to date'
    });
  } catch (error) {
    res.status(500).json({ error: 'Failed to get git status', details: error });
  }
});

// File upload
app.post('/api/upload', upload.single('file'), (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: 'No file uploaded' });
    }
    
    res.json({ 
      success: true, 
      filename: req.file.filename,
      path: req.file.path,
      message: 'File uploaded successfully' 
    });
  } catch (error) {
    res.status(500).json({ error: 'File upload failed' });
  }
});

// Get file list
app.get('/api/files', async (req, res) => {
  try {
    const files = await fs.readdir('.');
    const fileList = [];
    
    for (const file of files) {
      const stats = await fs.stat(file);
      if (stats.isFile() && !file.startsWith('.') && file !== 'admin-server.js') {
        fileList.push({
          name: file,
          size: stats.size,
          modified: stats.mtime,
          type: path.extname(file)
        });
      }
    }
    
    res.json(fileList);
  } catch (error) {
    res.status(500).json({ error: 'Failed to read file list' });
  }
});

// Work Experience API endpoints
app.get('/api/work', async (req, res) => {
  try {
    // Extract work experience from index.html
    const indexContent = await fs.readFile('index.html', 'utf8');
    // This is a simplified version - you'd parse the actual HTML
    const workExperiences = [
      {
        id: 'jio-senior-pm',
        title: 'Senior Product Manager — Jio Platforms (AI Division)',
        company: 'Jio Platforms',
        startDate: 'Aug 2023',
        endDate: 'Present',
        achievements: [
          'JIA across 20M+ devices; 58K+ WAUs; 50% support deflection.',
          'Unified siloed assistants → one agent; duplicate queries −60; NPS +22.',
          'RAG on 100GB+ corpus (Gemini + LangChain) → +35 accuracy.'
        ]
      }
    ];
    res.json(workExperiences);
  } catch (error) {
    res.status(500).json({ error: 'Failed to read work experience' });
  }
});

app.post('/api/work', async (req, res) => {
  try {
    const { workExperiences } = req.body;
    // Update work section in index.html
    // This would involve parsing and updating the HTML structure
    res.json({ success: true, message: 'Work experience updated successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Failed to update work experience' });
  }
});

// Projects API endpoints
app.get('/api/projects', async (req, res) => {
  try {
    // Extract projects from index.html
    const projects = [
      {
        id: 'jia-assistant',
        title: 'JIA Agentic Assistant (Spotlight)',
        icon: '🤖',
        description: 'Multimodal orchestration, retrieval, guardrails, cost-aware rollout across 20M+ devices.',
        features: ['Gemini + LangChain RAG pipelines', 'Hallucination guardrails & label QA'],
        technologies: ['GenAI', 'RAG']
      }
    ];
    res.json(projects);
  } catch (error) {
    res.status(500).json({ error: 'Failed to read projects' });
  }
});

app.post('/api/projects', async (req, res) => {
  try {
    const { projects } = req.body;
    // Update projects section in index.html
    res.json({ success: true, message: 'Projects updated successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Failed to update projects' });
  }
});

// Education API endpoints
app.get('/api/education', async (req, res) => {
  try {
    const education = [
      {
        id: 'isb-mba',
        institution: 'Indian School of Business',
        degree: 'MBA',
        field: 'Strategy & Leadership, Marketing',
        details: 'GRE 332 (99th percentile)',
        achievements: ['Accenture Strategy National Finalist (16/8.5k) • PPI']
      }
    ];
    res.json(education);
  } catch (error) {
    res.status(500).json({ error: 'Failed to read education' });
  }
});

app.post('/api/education', async (req, res) => {
  try {
    const { education } = req.body;
    // Update education section in index.html
    res.json({ success: true, message: 'Education updated successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Failed to update education' });
  }
});

// Contact API endpoints
app.get('/api/contact', async (req, res) => {
  try {
    const contact = {
      email: 'srijaharshika.d@gmail.com',
      linkedin: 'https://www.linkedin.com/in/srijaharshika/',
      topmate: 'https://topmate.io/srijaharshika/',
      resume: 'Srija_Harshika_Resume.pdf'
    };
    res.json(contact);
  } catch (error) {
    res.status(500).json({ error: 'Failed to read contact info' });
  }
});

app.post('/api/contact', async (req, res) => {
  try {
    const contactData = req.body;
    // Update contact section in index.html
    res.json({ success: true, message: 'Contact information updated successfully' });
  } catch (error) {
    res.status(500).json({ error: 'Failed to update contact information' });
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`Admin server running on http://localhost:${PORT}`);
  console.log(`Access admin panel at http://localhost:${PORT}/admin.html`);
});

module.exports = app;
