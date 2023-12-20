FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
RUN mars_sre_runbook_api create-db
RUN mars_sre_runbook_api populate-db
RUN mars_sre_runbook_api add-user -u admin -p admin
EXPOSE 5000
CMD ["mars_sre_runbook_api", "run"]
