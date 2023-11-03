# Receipt Processor

A webservice that fulfils the documented API in [api.yaml](https://github.com/fetch-rewards/receipt-processor-challenge/blob/main/api.yml). More information and examples on how to use this API can be found here [receipt-processor](https://github..com/fetch-rewards/receipt-processor-challenge)

This project is a take home assesment for Fetch Rewards company Software Engineering Role.

# Tech Stack
Python, Django (Web Framework), Sqlite (Database), Docker

# How to start the webserver

1. Ensure that [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker](https://docs.docker.com/engine/install/) are installed in your system.
2. Open your terminal and git clone this repository by running the ff command:

```
git clone git@github.com:cleomart/fetch_receipt.git
```
3. Go to the `fetch_receipt` directory
```
cd fetch_receipt
```
4. Build the docker container with fetch-receipt tag using the ff command:

```
docker build . -t fetch-receipt
```
5. Run the docker container and port-forward the port 8000 of the docker application to your localhost port of 8000
```
docker run -p 8000:8000 fetch-receipt
```
6. The django server should be up and running and the APIs can be accessed in your localhost with port 8000
``````
http://localhost:8000/receipts/process
http://localhost:8000/receipts/{id}/points
