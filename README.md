# API Gateway Django Project

This project is a simple API gateway built using Django. It provides an interface to interact with various APIs and services. Follow the instructions below to set up and run the project locally.

## Prerequisites

Before setting up the project, ensure you have the following installed:
- Python 3.x
- pip (Python package manager)
- virtualenv (for managing Python environments)

## Installation

### 1. Create a Virtual Environment

Create a virtual environment for the project using the following command:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```bash
  venv\Scripts\activate
  ```

- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 2. Install Dependencies

Install the required packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Set up Environment Variables

Create a `.env` file in the root directory of the project. Add the following two environment variables:

```
OPENAI_API_KEY=your_openai_api_key_here
SECRET_KEY=your_django_project_secret_key_here
```

- Replace `your_openai_api_key_here` with your OpenAI API key.
- Replace `your_django_project_secret_key_here` with your Django project's secret key.

### 4. Configure Allowed Hosts

Before running the project locally, you need to add your local Wi-Fi's IP address to Django's `ALLOWED_HOSTS` setting.

To find your local Wi-Fi's IPv4 address:

- On Windows, run the following command in the Command Prompt:
  ```bash
  ipconfig
  ```
  Look for the "IPv4 Address" under your active network connection (usually it will look something like `192.168.x.x`).

- On macOS/Linux, run:
  ```bash
  ifconfig
  ```
  Look for the "inet" address under your active Wi-Fi connection.

Once you have your local Wi-Fi IP address, open the Django settings file (`settings.py`) and add the IP to the `ALLOWED_HOSTS` list:

```python
ALLOWED_HOSTS = ['your_wifi_ip_address_here']
```

Replace `your_wifi_ip_address_here` with the IP address you found.

### 5. Run the Django Server

To start the Django development server locally, run:

```bash
python manage.py runserver your_wifi_ip_address_here:8000
```

This will host the project on your local machine and allow you to access it using your local Wi-Fi IP address.

### 6. Access the Project Locally

Now you can access the project locally in your browser by navigating to:

```
http://your_wifi_ip_address_here:8000
```

Replace `your_wifi_ip_address_here` with your local Wi-Fi IP address.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/) - For the web framework.
- [OpenAI](https://openai.com/) - For the OpenAI API.
