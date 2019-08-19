FROM centos/python-27-centos7

#RUN apt-get update && apt-get install -ym python2

#RUN git clone https://github.com/jucaazevedo/papaulo

#ADD workbench_ova-1.0.0-20170504.084926-37.ova /work

#RUN vboxmanage import --vsys 0 --vmname wkb1 /work/workbench_ova-1.0.0-20170504.084926-37.ova

#EXPOSE 8443:8443

WORKDIR /root

CMD python2 -version
