# Simple Online Bookstore System

A Django-based online bookstore system that provides book browsing, user authentication, and shopping cart functionality.

## System Requirements

### Hardware Requirements
- Minimum System Requirements:
 * CPU: 1.6 GHz dual-core processor or higher
 * RAM: 4GB minimum, 8GB recommended
 * Storage: 1GB of free space

- Development Environment Used:
 * MacBook Pro with M1 chip
 * Memory: 16GB RAM

### Software Requirements
* Docker Desktop
* Docker Compose

Or if running without Docker:
* Operating System: macOS or Linux
* Python 3.8+
* Django 3.2+
* PostgreSQL

## Installation

### Using Docker (Recommended)
```bash
# Clone the repository
git clone https://github.com/Annieliu16588/bshop.git
cd bshop

# Build and run with Docker
docker-compose up --build

# Apply database migrations
docker-compose exec web python manage.py migrate

http://localhost:8000
http://localhost:8000/admin/
