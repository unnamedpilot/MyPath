# MyPath

This is a usage and setup guide for the travel planning application that utilizes Django, the ChatGPT API, and jsPDF. This application allows users to plan their trips interactively, select their preferences, get information about cities and routes, design their itinerary, and download it in PDF format.

## Requirements

Make sure to have the following components installed before running the application:

- Python 3.x
- Django
- A ChatGPT (Generative Pre-trained Transformer) account for interactive text generation
- jsPDF (JavaScript library for generating PDF files)

## Configuration

1. Clone the application's repository from GitHub:
   - https://github.com/unnamedpilot/MyPath.git
  
2. Create a virtual environment for the application:
3. Activate the virtual environment:

- On Windows:

  ```
  venv\Scripts\activate
  ```

- On macOS or Linux:

  ```
  source venv/bin/activate
  ```

4. Install Python dependencies:

   - pip install -r requirements.txt

6. Configure the ChatGPT API:

- Obtain your ChatGPT credentials and ensure you have the corresponding Python library installed.
- Configure the credentials in `settings.py` of the application.

6. Configure jsPDF:

- Include the jsPDF library in your project, either by downloading the necessary files or using a package manager.

## Usage

1. Start the Django application:
   - python manage.py runserver
  
2. Open a web browser and access the application at `http://localhost:8000`.

3. Interact with the application as follows:

- **Preferences Page:** Aspirants can select their travel preferences using buttons and options.
- **Home Page:** Cities and routes with descriptions are displayed. Users can use an input field to interact with ChatGPT and get detailed travel information.
- **Travel Planning Page:** This page displays a list of the itinerary by days with descriptions. Users can customize their itinerary.
- **Comments:** Users can leave comments about their experience.

4. Download the itinerary in PDF format:

- Implement a function that generates a PDF using the jsPDF library and the travel itinerary data. This function should be linked to a button or action in the application.

## Customization

You can customize the application to suit your specific needs, such as adding more features, styles, and travel-specific functionalities.

## Contribution

If you want to contribute to the development of this application, follow these steps:

1. Fork the repository.
2. Create a new branch for your contribution.
3. Make your changes and ensure the application continues to work correctly.
4. Submit a pull request for review.

## Known Issues

- None

   
