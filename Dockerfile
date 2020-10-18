# --------------------------------------------------------------------------
# This is a Dockerfile to build a Python
# --------------------------------------------------------------------------
FROM python:3.7

RUN mkdir -p /code/logs

# Bundle app source
COPY . /code

# Workdir
WORKDIR /code

# Fix for underlying image issue (cf. https://github.com/pypa/setuptools/issues/2350#issue-688804947)
ENV SETUPTOOLS_USE_DISTUTILS stdlib

# Build requirements
RUN pip3 install -r requirements.txt

# Expose port
EXPOSE 8085

# Entrypoint
CMD python3 app.py
