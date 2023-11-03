# Use the Python 3.11 base image
FROM python:3.11

WORKDIR /home/app

# Copy the django project and app
COPY manage.py /home/app/
COPY receipt /home/app/receipt
COPY receipt_api /home/app/receipt_api
COPY db.sqlite3 /home/app/

# Copy the Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock /home/app/

# Install pipenv and your project dependencies
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# Set the PATH environment variable to include pipenv's virtual environment
ENV PATH="/root/.local/share/virtualenvs:${PATH}"


EXPOSE 8000

# # Run Django Server
# ENTRYPOINT ["pipenv", "run", "python", "/home/app/manage.py"]
# CMD ["runserver", "0.0.0.0:8000"]

# Set the environment variable to disable buffering for Python's standard output
ENV PYTHONUNBUFFERED 1

# Entry point to activate the virtual environment and run the Django server
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]