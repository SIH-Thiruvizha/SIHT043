# Publications Marketplace

Publications Marketplace is a Flask web application where users can buy and sell publications. It allows users to add their publications for sale, view publications, perform web scraping, and view analytics.

![Publications Marketplace](demo.gif)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Sell a Publication](#sell-a-publication)
  - [View Publication Details](#view-publication-details)
  - [Perform Web Scraping](#perform-web-scraping)
  - [View Analytics](#view-analytics)
- [Contributing](#contributing)


## Features

- Add publications for sale with details like book name, description, and price.
- Upload photos of publications.
- View a list of publications available for sale.
- View details of a specific publication.
- Perform web scraping to extract content from a website based on a specified topic.
- View analytics dashboard with sample sales data.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/publications_marketplace.git
    ```

2. Navigate into the project directory:

    ```bash
    cd publications_marketplace
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the application.

## Usage

### Sell a Publication

1. Click on the "Sell" button on the home page.
2. Fill in the details of the publication (book name, description, price, and optionally upload a photo).
3. Click on the "Submit" button to add the publication for sale.

### View Publication Details

1. Click on the "View Details" link on any publication card on the home page.
2. You will be redirected to a page displaying the details of the publication.

### Perform Web Scraping

1. Click on the "Web Scrape" button on the home page.
2. Enter the URL of the website you want to scrape and the topic you want to search for.
3. Click on the "Scrape" button to perform web scraping.

### View Analytics

1. Click on the "Analytics" button on the home page.
2. You will be redirected to an analytics dashboard displaying sample sales data.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.


