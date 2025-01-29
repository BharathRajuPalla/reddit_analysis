# Reddit Data Analysis

This Python script continuously collects Reddit posts from the `all` subreddit and stores them in a PostgreSQL database. It is designed to run indefinitely, fetching new posts at regular intervals.

## Features

- Fetches Reddit posts in real-time
- Stores data in a PostgreSQL database
- Handles duplicate posts gracefully
- Robust error handling and connection management
- Configurable fetch interval

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.9+** installed
2. **PostgreSQL** installed and running
3. A **Reddit API account** with a registered application
4. Required Python libraries (listed in `requirements.txt`)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/BharathRajuPalla/reddit_analysis.git
cd reddit-data-collector

### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt

