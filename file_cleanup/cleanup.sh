#!/bin/bash

# Script to delete files/directories recursively based on provided parameters

# Functions
usage() {
    echo "Usage: $0 -p <file/directory matching pattern>"
    echo "       [-f] [-d] (delete files and/or directories, must specify one or both)"
    echo "       [-e] (optional, directories must be empty to delete)"
    echo "       [-a <minimum age in days>] (optional)"
    echo "       [-s <minimum size, suffxed with b,c,k,M,G>] (optional)"
    echo "       <List of directories, space separated>"
    echo
    echo "Example:"
    echo "$0 -p *.log -f -a 30 /var/log/httpd /var/log/audit"
    exit 1
}

# Global variables
DELETE_FILES="N"
DELETE_DIRS="N"
EMPTY=""
AGE=""
SIZE=""

# Main

# Argument parsing
while getopts ":p:efda:s:" OPT
do
    case "${OPT}" in
        p)
            PATTERN=${OPTARG}
        ;;
        e)
            EMPTY="-empty"
        ;;
        f)
            DELETE_FILES="Y"
        ;;
        d)
            DELETE_DIRS="Y"
        ;;
        a)
            AGE="-mtime +${OPTARG}"
        ;;
        s)
            SIZE="-size +${OPTARG}"
        ;;
        *)
            usage
        ;;
    esac
done

shift $((OPTIND - 1))

# Sanity check arguments after parsing

# What's left should be a list of directories to recurse
if [ $# -eq 0 ]
then
    echo -e "No directories specified.\n"
    usage
fi

LOCATION="$*"

for LOC in ${LOCATION}
do
    if ! test -d ${LOC}
    then
        echo -e "Specified location ${LOC} is not a directory.\n"
        usage
    fi
done

if [ -z "${PATTERN}" ]
then
    echo -e "Missing required arguments.\n"
    usage
fi

if [ "${DELETE_FILES}" != "Y" ] && [ "${DELETE_DIRS}" != "Y" ]
then
    echo "You must specify -f and/or -d to delete files and/or directories respectively"
    usage
fi

# Loop through the specified directories, taking the specified actions 
for LOC in ${LOCATION}
do
    if [ "${DELETE_FILES}" = "Y" ]
    then
        echo "Finding and deleting files under ${LOC}"
        find "${LOC}" -type f -name "${PATTERN}" ${AGE} ${SIZE} -print -delete
    fi

    if [ "${DELETE_DIRS}" = "Y" ]
    then
        # We use xargs here because -delete will not delete non-empty directories, which we are allowing
        # Also, specify -mindepth 1 to keep from deleting the specified directory itself
        echo "Finding and deleting directories under ${LOC}"
        find "${LOC}" -mindepth 1 -type d -name "${PATTERN}" ${AGE} ${SIZE} ${EMPTY} -print0 | xargs --null --no-run-if-empty --verbose rm -rf
    fi
done

