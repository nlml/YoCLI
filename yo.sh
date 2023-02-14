export yodir="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

function yo() {
    # Check if user provided the 'N' argument
    if [[ $1 == "N" ]];
    then
        N=$2
        str="${@:3}"
    else
        N=1
        # Query is concatentation of all other arguments
        str="$*"
    fi
    python3 $yodir/yo.py --N=$N --query="""$str"""
}