# 📊 Reddit Sentiment Analyzer

This is a web app built with **Streamlit** that performs **sentiment analysis** on Reddit posts and comments using the **VADER model** from NLTK.

🌐 **Live Demo:**  
🔗 [reddit-sentiment-analysis.streamlit.app](https://reddit-sentiment-analysis-nxnq5bdr9q7nyayqzkez4v.streamlit.app/)

<img width="828" height="492" alt="image" src="https://github.com/user-attachments/assets/b1bf63e0-8033-4d85-9fe1-8227aa2ad638" />
<img width="848" height="865" alt="image" src="https://github.com/user-attachments/assets/855eb0fc-0168-41de-9c8b-8b120d6fc18b" />
<img width="846" height="383" alt="image" src="https://github.com/user-attachments/assets/9a63a9cf-e14f-4772-9c00-b9cfe74cd6c0" />



## 🚀 Features

- 🔍 Analyze sentiments of hot posts from any subreddit (up to 200 posts)
- 💬 Analyze top-level comments from a specific Reddit post URL
- 📊 Visualize sentiment distribution using bar charts
- 🔐 Uses environment variables to keep Reddit API credentials secure

## 🧰 Tech Stack

- **Python**
- **NLTK VADER** for sentiment scoring
- **PRAW** (Python Reddit API Wrapper)
- **Streamlit** for the web interface
- **dotenv** for credential management

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/reddit-sentiment-analyzer.git
cd reddit-sentiment-analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Reddit API credentials
Create a ```.env``` file with the following contents:
```bash
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_custom_agent
```

## 🧠 How Sentiment Is Determined
### This app uses the VADER (Valence Aware Dictionary and Sentiment Reasoner) model from NLTK to analyze social media-style text. Each post/comment is scored and classified as:

- Positive (compound > 0.05)
- Negative (compound < -0.05)
- Neutral (otherwise)
