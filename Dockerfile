FROM python:3.6.8-stretch

LABEL "version"="1.0.0"

LABEL "com.github.actions.name"="GitHub Action for Python"
LABEL "com.github.actions.description"="Wraps the Python CLI to enable common python/pip commands."
LABEL "com.github.actions.icon"="package"
LABEL "com.github.actions.color"="blue"

COPY use_virtualenv.sh /

ENTRYPOINT [ "/use_virtualenv.sh" ]
CMD [ "--help" ]
