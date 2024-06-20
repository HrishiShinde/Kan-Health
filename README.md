# Kan-Health

Kan-Health is a healthcare management application designed to streamline the process of managing patient data and suggesting personalized health plans . This repository contains the code necessary to set up and run the Kan-Health application.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Python 3.8 or later.
- You have a working internet connection to download the necessary dependencies.

## Installation

Follow these steps to get the project up and running:

1. **Clone the repository:**
```sh
   git clone https://github.com/yourusername/kan-health.git
   cd kan-health
```

2. **Install the required packages:**
```sh
   pip install -r requirements.txt
```

3. **Apply database migrations:**
```sh
   python manage.py makemigrations
   python manage.py migrate
```

4. **Fine-tune the model:**
```sh
   python model/main.py
```

4. **Start the server:**
```sh
   python manage.py runserver
```

## Usage

Once the server is running, you can access the application in your web browser at http://127.0.0.1:8000.