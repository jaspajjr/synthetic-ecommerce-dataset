FROM jaspajjr/data-science-dockerfile-python2

COPY src /data

RUN mkdir /output && chmod 0755 /output

COPY container-entrypoint.sh /entry
RUN chmod 0755 /entry

CMD ["start"]
ENTRYPOINT ["/entry"]
