export yodir="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

function yo() {
    if [[ $1 == "N" ]];
    then
        N=$2
        str="${@:3}"
    else
        N=1
        str="$*"
    fi
    python $yodir/yo.py --N=$N --query="""$str"""
}