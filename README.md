# Unbitly
Expand shortened URLs

## Installing

Install all necessary Python packages with `pip`.

```bash
$ pip install -r requirements.txt
```

## Running

Run the API as a simple Python script.

```bash
$ python api/app.py
```

## API

Send the URL to be expanded as the `url` parameter in a GET request.

### Request

```bash
$ curl http://localhost:5000?url=https://t.co/6Tx32jX6O9
```

### Result

```json
{
  "url": "https://techcrunch.com/2016/10/25/the-crunchies-nominations-close-soon/"
}
```