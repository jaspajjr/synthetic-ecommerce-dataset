FROM jaspajjr/data-science-dockerfile-python2

RUN mkdir /output && chmod 0755 /output


# COPY config.json /data
COPY container-entrypoint.sh /entry
RUN chmod 0755 /entry

COPY src /data

CMD ["start"]
ENTRYPOINT ["/entry"]
