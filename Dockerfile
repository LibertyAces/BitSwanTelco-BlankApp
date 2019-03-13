FROM teskalabs/bspump:master-alpine3.8
MAINTAINER TeskaLabs Ltd (support@teskalabs.com)

# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV LANG C.UTF-8

# TODO: bspumptelco installation from proper source
RUN set -ex \
	pip install bspumptelco

RUN set -ex \
	mkdir /opt/bstelco-blank-app

COPY ./etc /opt/bstelco-blank-app/etc
COPY ./bstelco-blank-app.py /opt/bstelco-blank-app/bstelco-blank-app.py

WORKDIR /opt/bstelco-blank-app
CMD ["python3", "/opt/bstelco-blank-app/bstelco-blank-app.py", "-c", "/opt/bstelco-blank-app/etc/site.conf", "-w"]
