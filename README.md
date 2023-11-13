Project Overview

This repository contains code for a conversational AI-powered application utilizing multiple services and APIs. The application enables users to interact through audio and text with an AI model, leveraging OpenAI's GPT-3.5 for conversation and Eleven Labs for text-to-speech conversion.

Structure

Backend: Contains FastAPI endpoints and functions to interact with OpenAI and Eleven Labs.

Frontend: Frontend code for user interaction, likely a web application built using React.

Stored Data: Sample conversation data used to seed the AI's responses.

Configurations: Configuration files for API keys, environment variables, and database setups.

Models: Database model definitions using SQLAlchemy for user data.

Other files: Various utility functions and dependencies for audio conversion, API requests, and database interactions.

Components

Backend:

FastAPI serves as the backend, providing REST endpoints to interact with the AI model and audio conversion services.

It includes functions to store conversation data, reset conversations, and interact with OpenAI and Eleven Labs.

Frontend:

A React-based frontend that likely uses Axios for API requests and allows users to record and send audio, interacting with the backend services.

Stored Data:

Predefined conversation snippets used to prime the AI model when starting conversations.

Models:

SQLAlchemy-based database models to manage user data.

Usage

Setup: Ensure the necessary environment variables (API keys, configurations) are properly set in .env files.

Backend:

Run the FastAPI application using uvicorn main:app.
Endpoints are available for health check, conversation reset, and audio interaction.

Frontend:

For a typical React application, you'd likely run commands like npm install to install dependencies and then npm start to start the development server.

How to Run

Set up the environment variables in .env files.
Start the FastAPI backend by running uvicorn main:app.
Launch the frontend application, typically using npm start or similar commands.
Ensure the backend and frontend communicate properly for seamless user interaction.
Contribution Guidelines
Fork this repository, make changes, and submit pull requests for any enhancements or bug fixes.
Ensure code follows the existing style and maintain proper documentation.
Any major changes should be discussed beforehand via issues.

Additional Notes

Always maintain security by not exposing API keys or sensitive information in the repository.
Regularly update dependencies to the latest stable versions to ensure optimal performance and security.
