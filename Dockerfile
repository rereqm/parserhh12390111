FROM python:3.10.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Upgrade pip
RUN pip install --upgrade pip

# Install necessary packages
RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext openssh-client flake8 locales vim

# Create a non-root user
RUN useradd -m -s /bin/bash secsait

# Set working directory
WORKDIR /secsait

# Copy project files and install dependencies
COPY --chown=secsait:secsait . /secsait/
RUN chown -R secsait:secsait /secsait
RUN pip install -r requirements.txt

# Create necessary directories and set permissions
RUN mkdir -p /secsait/static /secsait/media
RUN chmod -R 755 /secsait && chown -R secsait:secsait /secsait

# Change to non-root user
USER secsait

# Default command
CMD ["bash"]

