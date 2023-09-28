#=============================================================================

if [ "$#" -ne 1 ]
then
  echo "Usage: $0 [NAMESPACE]" >&2
  exit 1
fi

NAMESPACE=$1

echo "Removing ScaleOut - $NAMESPACE"

helm delete  disco -n $NAMESPACE
