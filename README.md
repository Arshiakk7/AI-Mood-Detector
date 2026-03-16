# AI-Mood-Detector(Text Sentiment Analyzer)

An AI-powered Mood Detector built with Python that analyzes text and predicts the emotional mood (Happy, Neutral, or Sad/Angry) using Natural Language Processing.

The application uses TextBlob sentiment analysis and provides a simple graphical interface built with Tkinter.

Users can enter any text and instantly see the emotional tone along with a sentiment score. The app also tracks previous analyses and visualizes them in a sentiment trend chart.
## Features
- Detects mood from user text
- Shows sentiment polarity score
**Classifies mood into:**
     - Happy
     - Neutral
     - Sad / Angry
     - Clean GUI built with Tkinter
     - Clear text button
- Sentiment trend visualization using matplotlib
- Tracks history of sentiment scores

**Technologies Used:**
 - Python
 - Tkinter – GUI interface
 - TextBlob – Natural Language Processing
 - Pandas – Data handling
 - Matplotlib – Sentiment trend chart

 ## Project Structure
- AI-Mood-Detector
- │
- ├── mood_detector.py
- ├── README.md


## How to Run the Project

- Run the Python file:
           python mood_detector.py

- The AI Sentiment Dashboard GUI will open.

## How It Works

- User enters text in the input box.

- The program analyzes the text using TextBlob sentiment polarity.

- The sentiment score determines the mood:

**Score Range	Mood:**
- > 0.3	Happy
- < -0.3	Sad / Angry
- -0.3 to 0.3	Neutral

The sentiment score is stored and can be visualized using the Show Chart button.

## Example

**Input:**
I am very excited about learning AI today!

## Output:
- Mood: Happy
- Score: 0.75
## Future Improvements
- Add real-time sentiment detection
- Add emoji mood visualization
- Support voice input
- Export sentiment history as CSV
- onvert to web app using Streamlit

## Author
Created by Arshiakk7



