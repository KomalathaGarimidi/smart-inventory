# smart-inventory
Smart Inventory Management System using Django, DRF, PostgreSQL, Redis

A Django-based inventory management application.

## Prerequisites
- Python 3.12+
- Git

## How to Run Locally

Follow these steps to set up and run the project on your local machine:

### 1. Clone the repository
```bash
git clone [https://github.com/your-username/smart-inventory.git](https://github.com/your-username/smart-inventory.git)
cd smart-inventory

2. Create and activate a virtual environment
python -m venv venv
# On Windows (PowerShell):
venv\Scripts\Activate
# On macOS/Linux:
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Set up your environment variables
Create a .env file in the root directory based on the .env.example template:

cp .env.example .env

(Open the newly created .env file and make sure to populate it with your unique SECRET_KEY and DEBUG=True).

5. Run database migrations
python manage.py migrate

6. Start the development server
python manage.py runserver