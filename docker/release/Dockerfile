FROM ikropotov/notejam-base-image

# Copy application artifacts
COPY target /wheelhouse

# Install application
RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse notejam && \
    rm -rf /wheelhouse