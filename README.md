# Manoeuvre - Event Management Software

**Manoeuvre** is an event management system designed specifically for college-level events. Built with **Django (Python)**, it serves as a comprehensive solution for managing event registrations, participant details, and event schedules.

---

## Key Features

### For Students:
- **Event Registration**: Students can register for specific events such as **Coding**, **Web Designing**, etc.
- **Status Updates**: Check the status of registration and event participation.
- **Event Information**: View detailed descriptions, timings, and locations for events.

### For Event Coordinators:
- **Participant Management**: Access participant details for assigned events.
- **Concurrent User Handling**: Manage high user activity without system downtimes.

### For Admins:
- **Export Data**: Download event-wise participant details in **Excel format** for processing and reporting.
- **Centralized Control**: Oversee all event registrations and user interactions.

---

## Technology Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default) or any other Django-supported database
- **Other tools**: PowerShell, Shell scripting for additional tasks.

---

## Project Setup

### 1. Prerequisites
Ensure you have the following installed:
- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package manager
- **Django**: Install via `pip install django`

### 2. Clone the Project
```bash
git clone https://github.com/basillal/Manoeuvre.git
cd Manoeuvre
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Server
```bash
python manage.py runserver
```
The application will be available at `http://127.0.0.1:8000` in your browser.

---

## Usage Workflow

1. **Student Registration**:
   - Students create an account and register for desired events.
   
2. **Event View**:
   - Students and coordinators can view event details such as time, description, and participation status.

3. **Coordinator Access**:
   - Event heads can manage participant information for their specific events.

4. **Admin Control**:
   - Admins can monitor all activities and export participant data for analysis.

---

## Example Events
- Coding
- Web Designing
- Poster Design
- Quiz
- Hackathon

---

## Benefits
- Simplifies the process of managing large events with many participants.
- Provides a centralized platform for coordination between students, organizers, and admins.
- Ensures smooth handling of concurrent user activity without performance lag.

---

**Manoeuvre** is a powerful and efficient solution for managing college-level events of all sizes.
