# Python Bus Ticket Booking System

## Overview
The Python Bus Ticket Booking System is a desktop application built using Python with Tkinter for the GUI, MySQL for the database, Pillow for image processing, and PyCalendar for date selection. It allows users to book bus tickets by providing necessary details such as name, email, phone number, destination, number of passengers, seat selection, class preference, and meal option.

## Features
- User Registration: Users can register by providing basic details such as name, email, and phone number.
- Bus Ticket Booking: Users can select their destination, bus class, and meal preference before booking tickets.
- Seat Selection: An interactive seat map allows users to choose their preferred seats and specify the number of passengers (adults, children, and elderly).
- Data Persistence: User details are stored in a MySQL database, enabling easy retrieval for future bookings.
- Data Autofill: Users can autofill their details by entering their phone number, reducing input redundancy.
- Ticket Display: Users can view their ticket details, including fare and passenger information, before booking.
- Ticket Saving: Ticket details are saved in the system in a TXT format, ready for printing (printing functionality not implemented yet).

## Technologies Used
- Python
- Tkinter (GUI)
- SQLite3 (Database)
- Pillow (Image processing)
- PyCalendar (Date selection)

## Setup
## Setup
1. Clone the repository: `git clone https://github.com/username/python-bus-ticket-system.git`
2. Install dependencies:
   - Python: If not already installed, download and install Python from the official website.
   - Tkinter: After installing Python, open Command Prompt (Windows) or Terminal (macOS/Linux) and type `pip install tkinter`.
   - TkCalendar: Install TkCalendar using `pip install tkcalendar`.
   - Pillow: Install Pillow using `pip install pillow`.
   - PyMySQL: Install PyMySQL using `pip install pymysql`.
3. Run the `database.py` file: Before running the main application, open and run the `database.py` file to create the necessary database tables on your local machine.
4. Start the application: `python main.py`
5. Use the application to book bus tickets.

## Future Improvements
- Implement printing functionality for tickets.
- Enhance UI/UX for a more intuitive booking experience.
- Add support for additional features such as seat preferences and special accommodations.
- Implement user authentication and authorization for secure access.
 
## Contribution 
[Eshaan Manchanda](https://github.com/EshaanManchanda)


