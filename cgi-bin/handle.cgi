#!/bin/bash

if [ -n "${QUERY_STRING}" ]
then
    ( exec "./internal.cgi" )
else
    ( exec "./remote.cgi" )
fi

exit 0
