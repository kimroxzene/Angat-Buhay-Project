# Angat-Buhay-Management-System
## Overview
The Angat Buhay Donation Management System is a system designed to manage and update various types of donations for multiple causes. 
It supports a wide range of donation categories, including food, water, clothes, books, school supplies, toiletries, and monetary contributions. 
The system allows users to add, update, and view donations, along with their associated details such as the cause, quantity, unit of measurement, 
and details. Each donation type is represented by a specific class, ensuring proper management of item-specific details. The project also offers 
a user-friendly interface for updating donation information, such as cause, quantity, unit, and additional details. This helps streamline the 
process of collecting and managing charitable donations, providing efficient tracking and updating functionalities for both donors and 
administrators. Angat Buhay Donation tracker tracks the donation of the donors.

## Python Concepts and Libraries applied
The donation tracking application utilizes several key Python concepts and libraries to build its graphical user interface and manage user 
interactions. It follows Object-Oriented Programming principles by organizing the application into a DonationApp class with methods to handle 
different functionalities like displaying forms, submitting donations, and managing user interactions. The Tkinter library is used extensively 
to create the GUI, providing widgets like buttons, labels, entry fields, and menus for user interaction. The application incorporates error 
handling to ensure smooth user interactions, using if-else statements to validate user inputs such as name, cause, quantity, and unit; if any 
fields are missing or incorrect, warning messages are displayed. 

In terms of data management, the application employ lists and dictionaries. The self.donations list stores all donation entries, with 
each donation represented as a dictionary containing details such as "donation_id", "donor_name", "cause", "quantity", "unit", and "description", 
enabling easy access and manipulation of donation data. The self.users_db dictionary stores user credentials, using the username as the key and 
the password as the value, allowing efficient user authentication and management. These data structures enable dynamic updates and effective 
management of user inputs and donation records.

## Details of the chosen SDG and its integration into project
The Angat Buhay Management System aligns with SDG 2: Zero Hunger and SDG 4: Quality Education by facilitating the collection and distribution 
of resources that support both food security and educational access. Through food, water, and toiletries donations, it directly addresses hunger 
and nutrition needs, crucial aspects of SDG 2. Book and school supplies donations also promote access to education, helping ensure that 
underprivileged children and communities can continue their learning, which contributes to SDG 4. By supporting these causes, it fosters both 
nutritional security and educational opportunities for those in need.

## Instructions for running the program

I.	Donate
When the Angat Buhay management system starts, the first option presented is donate, which allows the user to contribute goods. After selecting 
donate, the system prompts the user to choose a cause whether Climate Action Sustainability, Nutrition and Food Security, or Public Education. 
Once a cause is selected, the system will then ask which type of donation the user wishes to make. For Climate Action, there are five options: 
food, water, clothes, monetary, and toiletries donations. For Nutrition and Food Security, there are three options: food, water, and monetary 
donations. Lastly, for Public Education, users can choose from book, school supplies, or monetary donations. Once the user selects the type of 
donation, the system will prompt for the donor's name, select a cause, unit, quantity, and details. After entering this information, the donation 
is successfully added.

II.	Update Donation
The second option is updating a donation, the system first displays all of the donations made by various donors. The user is then prompted to 
select the donor id  corresponding to the donation they want to update. Once the donation is selected, the user can choose to update specific 
details, such as the cause, quantity, unit, or donation details. This allows for selective updates to the donation information based on the user’s preferences.

III.	View Dashboard
The third option is the viewing dashboard which displays a table of donations the table includes the number, donor name, cause of donation, 
donation type, quantity, unit, and donation details. This allows the user to easily view the information for each donation made.

IV.	Exit
Once the user selects "Exit”, the program will terminate and stop executing.
