FROM python:3.6

RUN pip install --upgrade pip

WORKDIR /example
RUN useradd -m worker
RUN chown worker:worker .
USER worker

RUN pip install --upgrade --user pipenv
ENV PATH=/home/worker/.local/bin:$PATH

COPY --chown=worker:worker . ./

RUN pipenv lock -r > requirements.txt
RUN python -m pip install -r requirements.txt
ENV FLASK_APP=./server.py

ENV PORT=8080
EXPOSE 8080
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080"]