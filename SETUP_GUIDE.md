# 🚀 Farm-IQ Setup Guide

This guide will walk you through setting up Farm-IQ on your local machine for development and testing.

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.6 - 3.9** (Python 3.6.12 recommended)
- **Git** (for cloning the repository)
- **pip** (Python package manager)
- **virtualenv** or **conda** (for creating isolated environments)

### Checking Prerequisites

```bash
# Check Python version
python --version
# or
python3 --version

# Check pip version
pip --version

# Check Git version
git --version
```

## 📥 Step 1: Clone the Repository

Choose the appropriate branch based on your needs:

### For Development (Full Code with Notebooks)
```bash
git clone https://github.com/vannu07/Farm-IQ-AI-Powered-Smart-Farming-Assistant.git
cd Farm-IQ-AI-Powered-Smart-Farming-Assistant
```

### For Deployment (Production-Ready Code)
```bash
git clone -b deploy https://github.com/vannu07/Farm-IQ-AI-Powered-Smart-Farming-Assistant.git
cd Farm-IQ-AI-Powered-Smart-Farming-Assistant
```

## 🐍 Step 2: Create a Virtual Environment

### Option A: Using Conda (Recommended)

```bash
# Create a new conda environment
conda create -n Farm-IQ python=3.6.12

# Activate the environment
conda activate Farm-IQ
```

### Option B: Using venv

```bash
# Create a new virtual environment
python -m venv farmiq-env

# Activate the environment
# On Windows:
farmiq-env\Scripts\activate

# On macOS/Linux:
source farmiq-env/bin/activate
```

## 📦 Step 3: Install Dependencies

Navigate to the app directory and install required packages:

```bash
# Navigate to app directory
cd app

# Install dependencies
pip install -r requirements.txt
```

### Common Installation Issues

**Issue: PyTorch installation fails**
```bash
# Install PyTorch separately (CPU version)
pip install torch==1.7.0+cpu torchvision==0.8.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
```

**Issue: Permission denied**
```bash
# Use --user flag
pip install --user -r requirements.txt
```

**Issue: Outdated pip**
```bash
# Upgrade pip
pip install --upgrade pip
```

## 🔑 Step 4: Configure API Keys

The application uses WeatherAPI for real-time weather data.

### Get Your API Key

1. Visit [WeatherAPI.com](https://www.weatherapi.com/)
2. Sign up for a free account
3. Get your API key from the dashboard

### Configure the API Key

Create a `.env` file in the `app` directory (if not exists):

```bash
# In the app directory
touch .env
```

Add your API key to `.env`:

```env
WEATHER_API_KEY=your_api_key_here
```

**Important:** Never commit your `.env` file to version control!

### Alternative: Update config.py (Not Recommended for Production)

Edit `app/config.py`:

```python
weather_api_key = "your_api_key_here"
```

## 📁 Step 5: Verify Directory Structure

Ensure your project structure looks like this:

```
Farm-IQ-AI-Powered-Smart-Farming-Assistant/
│
├── app/
│   ├── Data/
│   │   └── fertilizer.csv
│   ├── models/
│   │   ├── plant_disease_model.pth
│   │   └── RandomForest.pkl
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── scripts/
│   ├── templates/
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── disease.py
│   │   ├── fertilizer.py
│   │   └── model.py
│   ├── app.py
│   ├── config.py
│   └── requirements.txt
│
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

### Missing Models?

If the `models` directory is missing, you'll need to:

1. Download pre-trained models from the repository releases
2. Or train your own models using the notebooks in the main branch

## 🚀 Step 6: Run the Application

Start the Flask development server:

```bash
# Make sure you're in the app directory
cd app

# Run the application
python app.py
```

You should see output similar to:

```
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## 🌐 Step 7: Access the Application

Open your web browser and navigate to:

```
http://127.0.0.1:5000/
```

or

```
http://localhost:5000/
```

You should see the Farm-IQ home page!

## 🧪 Step 8: Test the Features

### Test Crop Recommendation

1. Navigate to "Crop Recommendation"
2. Enter sample values:
   - Nitrogen: 90
   - Phosphorus: 42
   - Potassium: 43
   - pH: 6.5
   - Rainfall: 200
   - City: Delhi
3. Click "Get Recommendation"

### Test Fertilizer Recommendation

1. Navigate to "Fertilizer Recommendation"
2. Select a crop (e.g., "Rice")
3. Enter N-P-K values
4. Click "Get Recommendation"

### Test Disease Detection

1. Navigate to "Disease Detection"
2. Upload a plant leaf image (JPG/PNG)
3. Click "Predict"

## 🛠️ Development Tips

### Running in Debug Mode

Edit `app.py` and change:

```python
if __name__ == '__main__':
    app.run(debug=True)  # Enable debug mode
```

### Port Configuration

To run on a different port:

```python
if __name__ == '__main__':
    app.run(debug=False, port=8080)
```

### Accessing from Other Devices

To access the app from other devices on your network:

```python
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
```

## ❌ Troubleshooting

### Error: "Module not found"

```bash
# Ensure you're in the correct directory and environment is activated
cd app
pip install -r requirements.txt
```

### Error: "Model file not found"

```bash
# Check if models directory exists
ls models/

# If missing, download models from repository or train them
```

### Error: "Weather API returns error"

- Verify your API key is correct in `config.py` or `.env`
- Check your internet connection
- Ensure you haven't exceeded the API rate limit (free tier: 1M calls/month)

### Error: "Port already in use"

```bash
# Find process using port 5000
# On Linux/macOS:
lsof -i :5000

# On Windows:
netstat -ano | findstr :5000

# Kill the process or use a different port
```

### Application runs but shows blank page

- Clear your browser cache
- Check browser console for JavaScript errors (F12)
- Verify all static files are present in `app/static/`

## 🔄 Updating the Application

To get the latest changes:

```bash
# Save your work first
git stash

# Pull latest changes
git pull origin main

# Reapply your changes
git stash pop

# Update dependencies
pip install -r app/requirements.txt
```

## 🧹 Deactivating the Environment

When you're done:

```bash
# For conda
conda deactivate

# For venv
deactivate
```

## 📚 Next Steps

- Read [CONTRIBUTING.md](CONTRIBUTING.md) to learn how to contribute
- Explore the [API Documentation](API_DOCUMENTATION.md)
- Check out the [README.md](README.md) for project overview
- Join the community discussions

## 🆘 Getting Help

If you encounter issues:

1. Check the [Issues](https://github.com/vannu07/Farm-IQ-AI-Powered-Smart-Farming-Assistant/issues) page
2. Search for similar problems
3. Create a new issue with:
   - Your Python version
   - Operating system
   - Full error message
   - Steps to reproduce

## 📄 License

This project is licensed under the GNU General Public License v3.0.

---

**Happy Coding! 🌾**

Made with ❤️ by the Farm-IQ Team
