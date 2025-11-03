#!/usr/bin/bash
#
out_log=/tmp/output.log

build()
{
    #python3 -m venv venv
    #source venv/bin/activate
    #pip3 install -r requirements
    docker build --tag oregon-trail-docker .
}

run()
{
    docker run -d -p 5000:5000 oregon-trail-docker
}

pylint_test()
{
    echo 'pylint --rcfile=.pylintrc src/' > ${out_log}
    pylint --rcfile=.pylintrc src/ >> ${out_log}
    echo "flake8 src/" >> ${out_log}
    flake8 src/ >> ${out_log}
    echo "Output sent to ${out_log}"
    cat $out_log
}

if [ $1 = "tests" ]; then
    pylint_test
elif [ $1 = "build" ]; then
    build
elif [ $1 = "run" ]; then
    run
else
    echo "$1 Command not supported"
fi
