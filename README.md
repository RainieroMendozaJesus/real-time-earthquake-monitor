# 🌍 Real-Time Earthquake Monitor

## Overview

**Real-Time Earthquake Monitor** is a Python-based data visualization project that connects to the official United States Geological Survey (USGS) real-time earthquake GeoJSON feed and displays recent earthquake activity from the last hour on an interactive global map.

This project was built as a hands-on learning exercise to practice working with:

* REST APIs
* JSON data processing
* Data visualization with Plotly
* Real-time dashboard behavior
* Streamlit web app deployment concepts

The application automatically refreshes every minute to display the most recent earthquake activity detected worldwide.

---

## Project Goals

The main objective of this project is educational.

Through this implementation, I practiced:

* Connecting to a real-world scientific API
* Understanding GeoJSON data structures
* Extracting nested dictionary values in Python
* Filtering and validating incoming data
* Building geographic visualizations
* Creating a simple real-time monitoring workflow
* Integrating Plotly with Streamlit
* Automatically refreshing dashboard data

---

## Data Source

This project uses the official real-time earthquake feed provided by:

**United States Geological Survey (USGS)**

Dataset used:

Last-hour global earthquake GeoJSON feed

[https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson)

The dataset updates automatically and provides:

* magnitude
* latitude
* longitude
* event title
* timestamp
* additional metadata for each earthquake

---

## Technologies Used

The project was implemented using the following Python libraries:

### requests

Used to perform HTTP requests and retrieve data from the USGS earthquake API.

### Plotly Express

Used to create an interactive geographic visualization where:

* marker size represents earthquake magnitude
* marker color reflects magnitude intensity
* the map projection displays global activity clearly

### Streamlit

Used to build the dashboard interface and render the visualization inside a web application layout.

### streamlit-autorefresh

Used to automatically refresh the dashboard every 60 seconds so that new earthquake events appear without manual reload.

---

## Features

* Real-time earthquake monitoring
* Interactive global map visualization
* Automatic refresh every 60 seconds
* Magnitude-based marker scaling
* Magnitude-based color gradient visualization
* Data filtering to remove invalid values

---

## How It Works

The application performs the following steps:

1. Connects to the USGS GeoJSON real-time feed
2. Retrieves earthquake event data
3. Extracts magnitude, coordinates, and titles
4. Filters invalid magnitude values
5. Builds a geographic scatter visualization using Plotly
6. Displays the visualization inside a Streamlit dashboard
7. Refreshes automatically every minute

---

## Learning Outcomes

Through this project I strengthened my understanding of:

* Working with external APIs
* Parsing nested JSON structures
* Data validation workflows
* Geographic visualization concepts
* Building simple monitoring dashboards
* Combining multiple Python visualization tools into a single workflow

---

## Possible Future Improvements

Potential enhancements for future versions of this project include:

* Adding earthquake depth visualization
* Adding magnitude filters
* Displaying historical comparisons
* Adding regional filtering
* Deploying the dashboard publicly
* Adding user interface controls

---

## Live Demo

A live version of the project can be viewed here:

[(Add your deployment link here)](https://real-time-earthquake-monitor-kfqonjjspygk86xsnsuugu.streamlit.app/)

---

## Author

Rainiero Mendoza de Jesus 2/4/2026

Created as a learning project focused on real-time data visualization using Python.

If you are learning data visualization, APIs, or Streamlit dashboards, feel free to explore and reuse this project structure as inspiration.
