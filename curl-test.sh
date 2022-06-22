#!/bin/bash

read -p "Input id for new timeline post. " id

curl -X POST http://localhost:5000/api/timeline_post -d 'name=curl-test&email=curl-test@email.com&content=curl test script&id="$id"'
echo "Printing all requests: "
curl http://localhost:5000/api/timeline_post

read -p "Input id for post to be deleted: " id2
curl -X DELETE http://localhost:5000/api/timeline_post/$id2
