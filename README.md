Introduction
This project is a tournament management system designed to track and manage student scores across various game events. The system allows users to input rankings for different games, assign points to students based on their rankings, calculate total points for each student, and display a comprehensive scoreboard. The program is written in Python and utilizes 2D arrays to store and manage data related to game participants, rankings, and points.

Features
Game Ranking Entry: Users can enter rankings for different game events, ensuring that each participant's position is accurately recorded.

Points Assignment: The system automatically assigns points to students based on their rankings in each game (1st place: 60 points, 2nd place: 30 points, 3rd place: 5 points).

Total Points Calculation: The program calculates the total points earned by each student across all games they participated in.

Scoreboard Display: A detailed scoreboard is generated, showing each student's performance in individual games, their total points, and their overall ranking.

User-Friendly Menu: The system provides a menu-driven interface, making it easy for users to navigate through different options such as entering rankings, assigning points, calculating totals, and viewing the scoreboard.

How It Works
Data Input: The program reads game participant data from a text file (games22.txt) and stores it in a 2D array.

Ranking Entry: Users can enter rankings for each game event, and the system validates the input to ensure accuracy.

Points Assignment: Based on the rankings, points are assigned to students and stored in a structured format.

Total Points Calculation: The system sums up the points for each student across all games to determine their total score.

Scoreboard Generation: The program generates a scoreboard that displays each student's performance, including the games they participated in, points earned in each game, total points, and their final ranking.

Usage
Clone the Repository: Start by cloning the repository to your local machine.

Run the Program: Execute the Python script (Practice Task.py) to launch the tournament management system.

Follow the Menu: Use the menu options to enter rankings, assign points, calculate totals, and view the scoreboard.

Input Data: Ensure that the games22.txt file is correctly formatted and contains the necessary participant data.

Requirements
Python 3.x

A text file (games22.txt) containing game participant data
