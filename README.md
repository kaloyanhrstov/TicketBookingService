# TicketBookingService
**The README and requirements.txt files were added after the interview

# Ticket Booking Service

A simple RESTful API built with **Django** and **Django REST Framework (DRF)** for managing events and ticket bookings, featuring session-based authentication and user registration.

---

## Prerequisites

* Python 3.10+
* pip (Python package manager)

---

## Getting Started & Running the Service

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/kaloyanhrstov/TicketBookingService.git](https://github.com/kaloyanhrstov/TicketBookingService.git)
   cd TicketBookingService
Create and activate a virtual environment:

Bash
python -m venv venv
venv\Scripts\activate
Install dependencies from requirements.txt:

Apply database migrations:

```bash
cd booking_project
python manage.py makemigrations
python manage.py migrate

# Create an admin superuser (optional):
python manage.py createsuperuser

# Run the development server:
python manage.py runserver
# The service will now be running locally at http://127.0.0.1:8000/.
