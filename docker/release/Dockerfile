FROM 878799173487.dkr.ecr.us-west-2.amazonaws.com/notejam

# Copy application artifacts
COPY target /wheelhouse

# Install application
RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse notejam && \
    rm -rf /wheelhouse