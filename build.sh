#!/usr/bin/bash
#
pylint_test()
{
    pylint src/
}

if [ $1 = "test" ]; then
    pylint_test
else
    echo "$1 Command not supported"
fi
