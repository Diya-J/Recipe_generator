# Recipe_generator
Project Overview
This project is an AI-powered recipe generator that leverages natural language processing (NLP) to generate recipes based on user inputs. It uses Rasa for conversational AI, SpaCy for entity extraction, and Python for backend logic and API integration. Users can ask for recipes by dish names or specify available ingredients to get personalized cooking suggestions.

 System Architecture
User Input:
User queries recipe or lists available ingredients.
Intent Recognition:
Rasa classifies the intent and extracts entities.
Custom Action Execution:
Custom actions fetch recipe details using APIs.
Response Generation:
The bot returns the formatted recipe and instructions.

Folder Structure
/recipe_generator
├── actions/
│   └── actions.py            # Custom actions to fetch recipes
├── data/
│   ├── nlu.yml               # Training data for NLU
│   └── stories.yml           # Conversation flow (stories)
├── models/
├── config.yml                # Pipeline and policies
├── credentials.yml           # API credentials
├── domain.yml                # Intents, entities, and responses
└── endpoints.yml             # Endpoint configuration for actions
