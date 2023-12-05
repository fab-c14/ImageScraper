# ImageScrapper

![ImageScrapper Logo]([https://images.pexels.com/photos/19369623/pexels-photo-19369623/free-photo-of-a-surfer-walks-along-the-beach-with-the-sun-behind-him.jpeg?auto=compress&cs=tinysrgb&w=400&lazy=load])

## Overview

ImageScrapper is a versatile Python-based web scraping tool designed for fetching and downloading images from various websites. Leveraging the power of Flask, Requests, Flask-CORS, Logging, and Beautiful Soup, ImageScrapper provides a robust and efficient solution for your image scraping needs.

---

## Features

- **Web Scraping:** ImageScrapper extracts images from different websites by providing the target URL.
- **Flask API:** Built on the Flask framework, offering a RESTful API for seamless integration into your projects.
- **CORS Support:** Flask-CORS is implemented to facilitate Cross-Origin Resource Sharing, enabling API access from different domains.
- **Logging:** Comprehensive logging ensures transparency and aids in troubleshooting during the scraping process.
- **Beautiful Soup:** HTML parsing is performed using Beautiful Soup, simplifying navigation and search within the HTML tree.

---

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/fab-c14/ImageScraper.git
    cd ImageScraper
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application:**

    ```bash
    python app.py
    ```

    The server will be accessible at http://localhost:5000.

---

## Usage

1. **Make a POST request:**

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"url": "https://example.com"}' http://localhost:5000/scrape
    ```

2. **Download Images:**

    The scraped images will be available for download in the `images` directory.

---

## Configuration

You can customize ImageScrapper's behavior by modifying the parameters in the `app.py` file.

---

## Contributors

- [Fab-c14](https://github.com/fab-c14) - Project Lead

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

Special thanks to the contributors and the open-source community.

Feel free to contribute, report issues, or suggest improvements! Happy coding! 🚀

