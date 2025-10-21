# 📡 Farm-IQ API Documentation

This document provides comprehensive information about the Farm-IQ API endpoints, request/response formats, and usage examples.

## 🌐 Base URL

```
http://localhost:5000
```

For production deployments, replace with your actual domain.

## 📋 Table of Contents

- [Routes Overview](#routes-overview)
- [Crop Recommendation API](#crop-recommendation-api)
- [Fertilizer Recommendation API](#fertilizer-recommendation-api)
- [Disease Prediction API](#disease-prediction-api)
- [Error Handling](#error-handling)
- [Rate Limiting](#rate-limiting)

---

## 🗺️ Routes Overview

| Method | Endpoint | Description | Content Type |
|--------|----------|-------------|--------------|
| GET | `/` | Home page | HTML |
| GET | `/crop-recommend` | Crop recommendation form | HTML |
| POST | `/crop-predict` | Get crop recommendation | Form Data |
| GET | `/fertilizer` | Fertilizer recommendation form | HTML |
| POST | `/fertilizer-predict` | Get fertilizer recommendation | Form Data |
| GET/POST | `/disease-predict` | Disease detection form/prediction | HTML/Multipart Form |

---

## 🌱 Crop Recommendation API

### Endpoint

```
POST /crop-predict
```

### Description

Recommends the best crop to plant based on soil nutrients, pH level, rainfall, and weather conditions (temperature and humidity).

### Request Format

**Content-Type:** `application/x-www-form-urlencoded` or `multipart/form-data`

**Parameters:**

| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| nitrogen | integer | Yes | Nitrogen content ratio in soil (0-140) | 90 |
| phosphorous | integer | Yes | Phosphorus content ratio in soil (5-145) | 42 |
| pottasium | integer | Yes | Potassium content ratio in soil (5-205) | 43 |
| ph | float | Yes | pH value of soil (3.5-9.5) | 6.5 |
| rainfall | float | Yes | Rainfall in mm (20-300) | 202.9 |
| city | string | Yes | City name for weather data | Delhi |

### Example Request

**HTML Form:**

```html
<form action="/crop-predict" method="POST">
    <input type="number" name="nitrogen" value="90" required>
    <input type="number" name="phosphorous" value="42" required>
    <input type="number" name="pottasium" value="43" required>
    <input type="number" step="0.1" name="ph" value="6.5" required>
    <input type="number" step="0.1" name="rainfall" value="202.9" required>
    <input type="text" name="city" value="Delhi" required>
    <button type="submit">Get Recommendation</button>
</form>
```

**cURL:**

```bash
curl -X POST http://localhost:5000/crop-predict \
  -d "nitrogen=90" \
  -d "phosphorous=42" \
  -d "pottasium=43" \
  -d "ph=6.5" \
  -d "rainfall=202.9" \
  -d "city=Delhi"
```

**Python:**

```python
import requests

url = "http://localhost:5000/crop-predict"
data = {
    "nitrogen": 90,
    "phosphorous": 42,
    "pottasium": 43,
    "ph": 6.5,
    "rainfall": 202.9,
    "city": "Delhi"
}

response = requests.post(url, data=data)
print(response.text)
```

### Response

**Success (200 OK):**

Returns an HTML page with the recommended crop.

```html
<!-- crop-result.html -->
<div class="result">
    <h3>Recommended Crop: Rice</h3>
    <p>Based on your soil conditions and climate, Rice is the best crop for your field.</p>
</div>
```

**Error (Fallback):**

If weather data cannot be fetched, redirects to error page:

```html
<!-- try_again.html -->
<div class="error">
    <h3>Unable to fetch weather data</h3>
    <p>Please check your city name and try again.</p>
</div>
```

### Supported Crops

The model can recommend the following crops:

- Rice
- Maize
- Chickpea
- Kidney Beans
- Pigeon Peas
- Moth Beans
- Mung Bean
- Black Gram
- Lentil
- Pomegranate
- Banana
- Mango
- Grapes
- Watermelon
- Muskmelon
- Apple
- Orange
- Papaya
- Coconut
- Cotton
- Jute
- Coffee

### Notes

- Weather data is fetched in real-time from WeatherAPI
- Temperature is retrieved in Celsius
- Humidity is expressed as a percentage
- The ML model has an accuracy of **99.2%**

---

## 🧪 Fertilizer Recommendation API

### Endpoint

```
POST /fertilizer-predict
```

### Description

Recommends the appropriate fertilizer based on soil nutrient content and target crop.

### Request Format

**Content-Type:** `application/x-www-form-urlencoded` or `multipart/form-data`

**Parameters:**

| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| cropname | string | Yes | Name of the crop to be grown | Rice |
| nitrogen | integer | Yes | Current nitrogen content in soil | 37 |
| phosphorous | integer | Yes | Current phosphorus content in soil | 0 |
| pottasium | integer | Yes | Current potassium content in soil | 0 |

### Example Request

**HTML Form:**

```html
<form action="/fertilizer-predict" method="POST">
    <select name="cropname" required>
        <option value="Rice">Rice</option>
        <option value="Wheat">Wheat</option>
        <!-- More options -->
    </select>
    <input type="number" name="nitrogen" value="37" required>
    <input type="number" name="phosphorous" value="0" required>
    <input type="number" name="pottasium" value="0" required>
    <button type="submit">Get Recommendation</button>
</form>
```

**cURL:**

```bash
curl -X POST http://localhost:5000/fertilizer-predict \
  -d "cropname=Rice" \
  -d "nitrogen=37" \
  -d "phosphorous=0" \
  -d "pottasium=0"
```

**Python:**

```python
import requests

url = "http://localhost:5000/fertilizer-predict"
data = {
    "cropname": "Rice",
    "nitrogen": 37,
    "phosphorous": 0,
    "pottasium": 0
}

response = requests.post(url, data=data)
print(response.text)
```

### Response

**Success (200 OK):**

Returns an HTML page with fertilizer recommendations:

```html
<!-- fertilizer-result.html -->
<div class="result">
    <h3>Fertilizer Recommendation</h3>
    <p>Your soil needs additional Phosphorus and Potassium...</p>
    <ul>
        <li>Use DAP (Di-Ammonium Phosphate) for Phosphorus</li>
        <li>Use Potash for Potassium</li>
    </ul>
</div>
```

### Recommendation Logic

The system analyzes:

1. **Required nutrients** for the selected crop
2. **Current soil nutrients** provided by user
3. **Nutrient deficiency** or excess
4. Provides specific fertilizer recommendations

### Supported Crops for Fertilizer

- Rice
- Wheat
- Maize
- Sugarcane
- Cotton
- Ground Nuts
- Millets
- Oil Seeds
- Pulses
- Tobacco
- Paddy
- Barley
- And more...

---

## 🔍 Disease Prediction API

### Endpoint

```
GET /disease-predict  (Display form)
POST /disease-predict (Submit prediction)
```

### Description

Identifies plant diseases from leaf images using a deep learning model (ResNet9 architecture).

### Request Format

**Content-Type:** `multipart/form-data`

**Parameters:**

| Parameter | Type | Required | Description | Accepted Formats |
|-----------|------|----------|-------------|------------------|
| file | file | Yes | Image of plant leaf | JPG, JPEG, PNG |

### Example Request

**HTML Form:**

```html
<form action="/disease-predict" method="POST" enctype="multipart/form-data">
    <input type="file" name="file" accept="image/*" required>
    <button type="submit">Predict Disease</button>
</form>
```

**cURL:**

```bash
curl -X POST http://localhost:5000/disease-predict \
  -F "file=@/path/to/leaf_image.jpg"
```

**Python:**

```python
import requests

url = "http://localhost:5000/disease-predict"
files = {'file': open('leaf_image.jpg', 'rb')}

response = requests.post(url, files=files)
print(response.text)
```

### Response

**Success (200 OK):**

Returns an HTML page with disease diagnosis and treatment recommendations:

```html
<!-- disease-result.html -->
<div class="result">
    <h3>Disease Detected: Apple Scab</h3>
    <h4>Cause:</h4>
    <p>Fungal infection caused by Venturia inaequalis...</p>
    <h4>Treatment:</h4>
    <ul>
        <li>Remove infected leaves</li>
        <li>Apply fungicide spray</li>
        <li>Improve air circulation</li>
    </ul>
</div>
```

**Error:**

If no file is uploaded or invalid file:

```html
<div class="error">
    <p>Please upload a valid image file</p>
</div>
```

### Supported Plants & Diseases

The model can detect **38 different conditions** across **14 crop types**:

#### Fruits
- **Apple:** Scab, Black Rot, Cedar Apple Rust, Healthy
- **Blueberry:** Healthy
- **Cherry:** Powdery Mildew, Healthy
- **Grape:** Black Rot, Esca, Leaf Blight, Healthy
- **Orange:** Huanglongbing (Citrus Greening)
- **Peach:** Bacterial Spot, Healthy
- **Strawberry:** Leaf Scorch, Healthy
- **Raspberry:** Healthy

#### Vegetables
- **Pepper (Bell):** Bacterial Spot, Healthy
- **Potato:** Early Blight, Late Blight, Healthy
- **Tomato:** Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus, Healthy

#### Grains & Others
- **Corn (Maize):** Cercospora Leaf Spot, Common Rust, Northern Leaf Blight, Healthy
- **Soybean:** Healthy
- **Squash:** Powdery Mildew

### Image Requirements

- **Format:** JPG, JPEG, or PNG
- **Size:** Recommended < 5 MB
- **Quality:** Clear, well-lit images work best
- **Focus:** Leaf should be the primary subject
- **Background:** Plain background preferred

### Model Information

- **Architecture:** ResNet9 (9-layer Residual Network)
- **Training Dataset:** 87,000+ images
- **Accuracy:** 96.5%
- **Input Size:** Automatically resized to 256x256

---

## ❌ Error Handling

### Common HTTP Status Codes

| Status Code | Description |
|-------------|-------------|
| 200 | Success - Request completed successfully |
| 302 | Redirect - Usually to error page |
| 400 | Bad Request - Invalid input parameters |
| 404 | Not Found - Endpoint doesn't exist |
| 500 | Internal Server Error - Server-side issue |

### Error Scenarios

#### Weather API Failure

**Cause:** Invalid city name or API key issue

**Response:** Redirects to `try_again.html`

**Solution:**
- Verify city name spelling
- Check API key configuration
- Ensure internet connectivity

#### File Upload Error

**Cause:** No file selected or invalid file type

**Response:** Redirects to disease prediction form

**Solution:**
- Select a valid image file
- Ensure file is JPG/PNG format

#### Model Loading Error

**Cause:** Model files missing or corrupted

**Response:** 500 Internal Server Error

**Solution:**
- Verify model files exist in `app/models/`
- Re-download model files if corrupted

---

## ⚡ Rate Limiting

### Weather API Limits

The free tier of WeatherAPI has the following limits:

- **Requests per month:** 1,000,000
- **Requests per minute:** No specific limit
- **Quota reset:** Monthly

### Recommendations

For production use:
- Implement caching for weather data
- Add rate limiting middleware
- Consider upgrading API plan for high-traffic applications

---

## 🔐 Security Best Practices

1. **API Keys:** Never expose API keys in client-side code
2. **Input Validation:** All inputs are validated server-side
3. **File Upload:** Only accept image files
4. **HTTPS:** Use HTTPS in production
5. **CORS:** Configure CORS for API access from web apps

---

## 🧪 Testing the API

### Using Postman

1. Download and install [Postman](https://www.postman.com/)
2. Import the collection (if available)
3. Set base URL to `http://localhost:5000`
4. Test each endpoint with sample data

### Using Python Requests

```python
import requests

# Test crop recommendation
def test_crop_recommendation():
    url = "http://localhost:5000/crop-predict"
    data = {
        "nitrogen": 90,
        "phosphorous": 42,
        "pottasium": 43,
        "ph": 6.5,
        "rainfall": 202.9,
        "city": "Delhi"
    }
    response = requests.post(url, data=data)
    assert response.status_code == 200
    print("✓ Crop recommendation test passed")

# Test fertilizer recommendation
def test_fertilizer_recommendation():
    url = "http://localhost:5000/fertilizer-predict"
    data = {
        "cropname": "Rice",
        "nitrogen": 37,
        "phosphorous": 0,
        "pottasium": 0
    }
    response = requests.post(url, data=data)
    assert response.status_code == 200
    print("✓ Fertilizer recommendation test passed")

# Test disease prediction
def test_disease_prediction():
    url = "http://localhost:5000/disease-predict"
    files = {'file': open('test_image.jpg', 'rb')}
    response = requests.post(url, files=files)
    assert response.status_code == 200
    print("✓ Disease prediction test passed")

if __name__ == "__main__":
    test_crop_recommendation()
    test_fertilizer_recommendation()
    test_disease_prediction()
    print("\n✅ All tests passed!")
```

---

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [WeatherAPI Documentation](https://www.weatherapi.com/docs/)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)

---

## 🤝 Contributing

Found an issue or want to improve the API?

1. Check existing [issues](https://github.com/vannu07/Farm-IQ-AI-Powered-Smart-Farming-Assistant/issues)
2. Create a new issue describing the problem
3. Submit a pull request with improvements

---

## 📞 Support

Need help with the API?

- **Issues:** [GitHub Issues](https://github.com/vannu07/Farm-IQ-AI-Powered-Smart-Farming-Assistant/issues)
- **Discussions:** [GitHub Discussions](https://github.com/vannu07/Farm-IQ-AI-Powered-Smart-Farming-Assistant/discussions)
- **Email:** Contact the maintainer

---

**Last Updated:** October 2025

**API Version:** 1.0.0

**Maintained by:** Farm-IQ Team
