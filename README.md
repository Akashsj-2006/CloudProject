# MConnect - Campus Marketplace

MConnect is a web-based platform designed for college students to buy and sell second-hand items within their campus community. This application provides an easy and secure way for students to connect and trade items like textbooks, electronics, furniture, and more.

## Features

- **User-Friendly Interface**: Clean and intuitive design for easy navigation
- **Product Listings**: View and search for items available for sale
- **Sell Items**: Easy-to-use form to list items for sale
- **Product Details**: Detailed view of each product with descriptions and seller information
- **Responsive Design**: Works on desktop and mobile devices
- **Category Filtering**: Browse items by category
- **Campus-Centric**: Designed specifically for college campus use

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python with FastAPI
- **Templating**: Jinja2
- **Styling**: Custom CSS with responsive design
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Poppins)

## Project Structure

```
MConnect/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
├── static/             # Static files (CSS, JS, images)
│   └── images/         # Product images and icons
└── templates/          # HTML templates
    ├── base.html       # Base template
    ├── index.html      # Home page
    ├── sell.html       # Sell item page
    ├── product.html    # Product detail page
    └── 404.html        # 404 error page
```

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd MConnect
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the development server**
   ```bash
   uvicorn main:app --reload
   ```

2. **Open your browser and visit**
   ```
   http://127.0.0.1:8000
   ```

## Usage

- **Browse Items**: Visit the homepage to see featured items
- **Sell an Item**: Click "Sell Now" to list an item for sale
- **View Details**: Click on any item to see more information
- **Contact Sellers**: Use the "Chat with Seller" button to inquire about an item

## Features in Development

- User authentication and profiles
- Real-time chat between buyers and sellers
- Advanced search and filtering
- Favorites and saved items
- Ratings and reviews system
- Admin dashboard

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to all contributors who have helped with this project
- Inspiration from other campus marketplaces
- The FastAPI and frontend developer communities

## Contact

For any inquiries, please contact [your-email@example.com](mailto:your-email@example.com)

---

**Note**: This is a static version of the application. Future updates will include backend functionality and database integration.
