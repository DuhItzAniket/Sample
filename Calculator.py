# Navigate to your project folder
cd Desktop
mkdir python-calculator
cd python-calculator

# Create the Python file
echo "# Simple Calculator in Python" > README.md
# Now create calculator.py using your text editor
# (copy the Python code above)

# Initialize Git repository
git init

# Check status
git status

# Add files to staging
git add calculator.py README.md
# or add everything
git add .

# Commit the files
git commit -m "Initial commit: Add simple calculator script"

# Add remote repository (use your GitHub URL)
git remote add origin https://github.com/YOUR_USERNAME/python-calculator.git

# Push to GitHub
git branch -M main
git push -u origin main