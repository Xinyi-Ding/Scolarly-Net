<!-- Generator: Widdershins v4.0.1 -->

<h1 id="fastapi">FastAPI v0.1.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

<h1 id="fastapi-default">Default</h1>

## root__get

<a id="opIdroot__get"></a>

> Code samples

- shell
```shell
curl -X GET / \
  -H 'Accept: application/json'
```

- http
```http
GET / HTTP/1.1
Accept: application/json
```

- javascript
```javascript
const headers = {
  'Accept':'application/json'
};

fetch('/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /`

*API Root*

This is the root endpoint of the API. It serves as an initial point to check the API status and discover the base URI.

> Example responses

> 200 Response

```json
null
```

<h3 id="root__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Provides a welcome message and the base URI of the API.|Inline|

<h3 id="root__get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="fastapi-catalog">catalog</h1>

## root_catalog__get

<a id="opIdroot_catalog__get"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X GET /catalog/ \
  -H 'Accept: application/json'
```

- http
```http
GET /catalog/ HTTP/1.1

Accept: application/json
```

- javascript
```javascript
const headers = {
  'Accept':'application/json'
};

fetch('/catalog/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/catalog/',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/catalog/', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/catalog/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/catalog/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/catalog/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /catalog/`

*Catalog API Root*

This is the root endpoint of the Catalog API. It provides a quick check to ensure the API is operational and to discover the base URI.

> Example responses

> 200 Response

```json
null
```

<h3 id="root_catalog__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Provides a welcome message along with the root URI for the Catalog API.|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|

<h3 id="root_catalog__get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## search_papers_catalog_papers_search_get

<a id="opIdsearch_papers_catalog_papers_search_get"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X GET /catalog/papers/search \
  -H 'Accept: application/json'
```

- http
```http
GET /catalog/papers/search HTTP/1.1

Accept: application/json
```

- javascript
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/catalog/papers/search',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/catalog/papers/search',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/catalog/papers/search', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/catalog/papers/search', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/catalog/papers/search");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/catalog/papers/search", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /catalog/papers/search`

*Search for Papers*

Search for papers based on various filters like title, publication date, DOI, and more.

<h3 id="search_papers_catalog_papers_search_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|article_id|query|integer|false|none|
|title|query|string|false|none|
|abstract|query|string|false|none|
|publisher|query|string|false|none|
|date|query|string|false|none|
|issn|query|string|false|none|
|eissn|query|string|false|none|
|volume|query|string|false|none|
|issue|query|string|false|none|
|page|query|string|false|none|
|doi|query|string|false|none|
|meeting|query|string|false|none|
|file_path|query|string|false|none|
|type|query|string|false|none|
|container_title|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "Success",
  "data": [
    {
      "id": 98,
      "title": "A method for deriving order compatible fuzzy relations from convex fuzzy partitions",
      "authors": [
        {
          "id": 219,
          "name": "Sandra Sandri",
          "email": "sandra.sandri@inpe.br",
          "affiliation": "Brazilian National Institute for Space Research (INPE) "
        },
        {
          "id": 220,
          "name": "Flávia Toledo Martins-Bedê",
          "affiliation": "Brazilian National Institute for Space Research (INPE) "
        }
      ]
    }
  ]
}
```

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

> 500 Response

```json
{
  "code": 500,
  "msg": "Internal Server Error"
}
```

<h3 id="search_papers_catalog_papers_search_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Papers found based on the search criteria|[PaperResponse](#schemapaperresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="search_papers_catalog_papers_search_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## search_topics_catalog_topics_search_get

<a id="opIdsearch_topics_catalog_topics_search_get"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X GET /catalog/topics/search \
  -H 'Accept: application/json'
```

- http
```http
GET /catalog/topics/search HTTP/1.1

Accept: application/json
```

- javascript
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/catalog/topics/search',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/catalog/topics/search',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/catalog/topics/search', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/catalog/topics/search', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/catalog/topics/search");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/catalog/topics/search", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /catalog/topics/search`

*Search for Topics*

Search for topics based on topic ID or name.

<h3 id="search_topics_catalog_topics_search_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|topic_id|query|integer|false|none|
|name|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "Success",
  "data": [
    {
      "id": 98,
      "topic": "Network data models",
      "count": 1
    }
  ]
}
```

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

> 500 Response

```json
{
  "code": 500,
  "msg": "Internal Server Error"
}
```

<h3 id="search_topics_catalog_topics_search_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Topics found based on the search criteria|[TopicResponse](#schematopicresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="search_topics_catalog_topics_search_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## search_authors_catalog_authors_search_get

<a id="opIdsearch_authors_catalog_authors_search_get"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X GET /catalog/authors/search \
  -H 'Accept: application/json'
```

- http
```http
GET /catalog/authors/search HTTP/1.1

Accept: application/json
```

- javascript
```javascript
const headers = {
  'Accept':'application/json'
};

fetch('/catalog/authors/search',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/catalog/authors/search',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/catalog/authors/search', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/catalog/authors/search', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/catalog/authors/search");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/catalog/authors/search", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /catalog/authors/search`

*Search for Authors*

Search for authors based on various filters like author ID, name, email, or affiliation.

<h3 id="search_authors_catalog_authors_search_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|author_id|query|integer|false|none|
|name|query|string|false|none|
|email|query|string|false|none|
|affiliation|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "Success",
  "data": [
    {
      "id": 98,
      "name": "A method for deriving order compatible fuzzy relations from convex fuzzy partitions",
      "count": 1
    }
  ]
}
```

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

> 500 Response

```json
{
  "code": 500,
  "msg": "Internal Server Error"
}
```

<h3 id="search_authors_catalog_authors_search_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Authors found based on the search criteria|[AuthorResponse](#schemaauthorresponse)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="search_authors_catalog_authors_search_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_same_topic_catalog_same_topic_get

<a id="opIdget_same_topic_catalog_same_topic_get"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X GET /catalog/same-topic \
  -H 'Accept: application/json'
```

- http
```http
GET /catalog/same-topic HTTP/1.1

Accept: application/json
```

- javascript
```javascript
const headers = {
  'Accept':'application/json'
};

fetch('/catalog/same-topic',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/catalog/same-topic',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/catalog/same-topic', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/catalog/same-topic', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/catalog/same-topic");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/catalog/same-topic", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`GET /catalog/same-topic`

*Articles under the Same Topic*

Retrieve articles that are related to the same topic based on a comprehensive set of article filters.

<h3 id="get_same_topic_catalog_same_topic_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|article_id|query|integer|false|none|
|title|query|string|false|none|
|abstract|query|string|false|none|
|publisher|query|string|false|none|
|date|query|string|false|none|
|issn|query|string|false|none|
|eissn|query|string|false|none|
|volume|query|string|false|none|
|issue|query|string|false|none|
|page|query|string|false|none|
|doi|query|string|false|none|
|meeting|query|string|false|none|
|file_path|query|string|false|none|
|type|query|string|false|none|
|container_title|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "Success",
  "data": {
    "connections": [
      {
        "topic": 10,
        "papers": [
          98
        ]
      },
      {
        "topic": 11,
        "papers": [
          98
        ]
      },
      {
        "topic": 12,
        "papers": [
          98
        ]
      },
      {
        "topic": 13,
        "papers": [
          98
        ]
      },
      {
        "topic": 14,
        "papers": [
          98
        ]
      }
    ],
    "topics": [
      {
        "id": 10,
        "name": "Similarity relations"
      },
      {
        "id": 11,
        "name": "Fuzzy relations"
      },
      {
        "id": 12,
        "name": "Fuzzy partitions"
      },
      {
        "id": 13,
        "name": "Total order"
      },
      {
        "id": 14,
        "name": "T-indistinguishable operators"
      }
    ],
    "papers": [
      {
        "id": 98,
        "title": "A method for deriving order compatible fuzzy relations from convex fuzzy partitions",
        "authors": [
          {
            "id": 219,
            "name": "Sandra Sandri",
            "email": "sandra.sandri@inpe.br",
            "affiliation": "Brazilian National Institute for Space Research (INPE) "
          },
          {
            "id": 220,
            "name": "Flávia Toledo Martins-Bedê",
            "affiliation": "Brazilian National Institute for Space Research (INPE) "
          }
        ]
      }
    ]
  }
}
```

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

> 500 Response

```json
{
  "code": 500,
  "msg": "Internal Server Error"
}
```

<h3 id="get_same_topic_catalog_same_topic_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Articles found based on the search criteria|[SameTopicResponseSchema](#schemasametopicresponseschema)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="get_same_topic_catalog_same_topic_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_co_author_catalog_co_author_get

<a id="opIdget_co_author_catalog_co_author_get"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X GET /catalog/co-author \
  -H 'Accept: application/json'
```

- http
```http
GET /catalog/co-author HTTP/1.1

Accept: application/json
```

- javascript
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/catalog/co-author',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/catalog/co-author',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/catalog/co-author', headers = headers)

print(r.json())
```

```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/catalog/co-author', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/catalog/co-author");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/catalog/co-author", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /catalog/co-author`

*Co-authorship Information*

Retrieve co-authorship information based on an article's filter.

<h3 id="get_co_author_catalog_co_author_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|article_id|query|integer|false|none|
|title|query|string|false|none|
|abstract|query|string|false|none|
|publisher|query|string|false|none|
|date|query|string|false|none|
|issn|query|string|false|none|
|eissn|query|string|false|none|
|volume|query|string|false|none|
|issue|query|string|false|none|
|page|query|string|false|none|
|doi|query|string|false|none|
|meeting|query|string|false|none|
|file_path|query|string|false|none|
|type|query|string|false|none|
|container_title|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "Success",
  "data": {
    "connections": [
      {
        "author": 219,
        "papers": [
          98
        ]
      },
      {
        "author": 220,
        "papers": [
          98
        ]
      }
    ],
    "authors": [
      {
        "id": 219,
        "name": "Sandra Sandri",
        "email": "sandra.sandri@inpe.br",
        "affiliation": "Brazilian National Institute for Space Research (INPE)"
      },
      {
        "id": 220,
        "name": "Flávia Toledo Martins-Bedê",
        "affiliation": "Brazilian National Institute for Space Research (INPE)"
      }
    ],
    "papers": [
      {
        "id": 98,
        "title": "A method for deriving order compatible fuzzy relations from convex fuzzy partitions",
        "authors": [
          {
            "id": 219,
            "name": "Sandra Sandri",
            "email": "sandra.sandri@inpe.br",
            "affiliation": "Brazilian National Institute for Space Research (INPE) "
          },
          {
            "id": 220,
            "name": "Flávia Toledo Martins-Bedê",
            "affiliation": "Brazilian National Institute for Space Research (INPE) "
          }
        ]
      }
    ]
  }
}
```

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

> 500 Response

```json
{
  "code": 500,
  "msg": "Internal Server Error"
}
```

<h3 id="get_co_author_catalog_co_author_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Co-authorship information found based on the search criteria|[CoAuthorResponseSchema](#schemacoauthorresponseschema)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="get_co_author_catalog_co_author_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_cited_tree_catalog_cited_tree_get

<a id="opIdget_cited_tree_catalog_cited_tree_get"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X GET /catalog/cited-tree \
  -H 'Accept: application/json'
```

- http
```http
GET /catalog/cited-tree HTTP/1.1

Accept: application/json
```

- javascript
```javascript
const headers = {
  'Accept':'application/json'
};

fetch('/catalog/cited-tree',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/catalog/cited-tree',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/catalog/cited-tree', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/catalog/cited-tree', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/catalog/cited-tree");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/catalog/cited-tree", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /catalog/cited-tree`

*Cited Tree of an Article*

Retrieve the citation tree of an article based on an article's filter.

<h3 id="get_cited_tree_catalog_cited_tree_get-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|article_id|query|integer|false|none|
|title|query|string|false|none|
|abstract|query|string|false|none|
|publisher|query|string|false|none|
|date|query|string|false|none|
|issn|query|string|false|none|
|eissn|query|string|false|none|
|volume|query|string|false|none|
|issue|query|string|false|none|
|page|query|string|false|none|
|doi|query|string|false|none|
|meeting|query|string|false|none|
|file_path|query|string|false|none|
|type|query|string|false|none|
|container_title|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "msg": "Success",
  "data": {
    "connections": [
      {
        "from_paper": 98,
        "to_paper": [
          75,
          99
        ]
      }
    ],
    "papers": [
      {
        "id": 75,
        "title": "A coloring algorithm for image classification, Inf",
        "authors": [
          {
            "id": 142,
            "name": "J. Montero"
          },
          {
            "id": 169,
            "name": "R. Mesiar"
          },
          {
            "id": 188,
            "name": "D. Gómez"
          },
          {
            "id": 189,
            "name": "J. Yáñez"
          },
          {
            "id": 229,
            "name": "B. Baets"
          },
          {
            "id": 230,
            "name": "T.-partitions"
          }
        ]
      },
      {
        "id": 98,
        "title": "A method for deriving order compatible fuzzy relations from convex fuzzy partitions",
        "authors": [
          {
            "id": 219,
            "name": "Sandra Sandri",
            "email": "sandra.sandri@inpe.br",
            "affiliation": "Brazilian National Institute for Space Research (INPE) "
          },
          {
            "id": 220,
            "name": "Flávia Toledo Martins-Bedê",
            "affiliation": "Brazilian National Institute for Space Research (INPE) "
          }
        ]
      },
      {
        "id": 99,
        "title": "On learning similarity relations in fuzzy case-based reasoning",
        "authors": [
          {
            "id": 221,
            "name": "E. Armengol"
          },
          {
            "id": 222,
            "name": "F. Esteva"
          },
          {
            "id": 223,
            "name": "L. Godo"
          },
          {
            "id": 224,
            "name": "V. Torra"
          }
        ]
      }
    ]
  }
}
```

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

> 500 Response

```json
{
  "code": 500,
  "msg": "Internal Server Error"
}
```

<h3 id="get_cited_tree_catalog_cited_tree_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Cited tree found based on the search criteria|[CitedTreeResponseSchema](#schemacitedtreeresponseschema)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="get_cited_tree_catalog_cited_tree_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="fastapi-analysis">analysis</h1>

## root_analysis__get

<a id="opIdroot_analysis__get"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X GET /analysis/ \
  -H 'Accept: application/json'
```

- http
```http
GET /analysis/ HTTP/1.1

Accept: application/json
```

- javascript
```javascript
const headers = {
  'Accept':'application/json'
};

fetch('/analysis/',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/analysis/',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/analysis/', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/analysis/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/analysis/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/analysis/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```

`GET /analysis/`

*Analysis API Root*

This is the root endpoint of the Analysis API. It can be used to check if the API is up and running.

> Example responses

> 200 Response

```json
null
```

<h3 id="root_analysis__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|A welcome message and the root URI.|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|

<h3 id="root_analysis__get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## upload_document_analysis_upload__post

<a id="opIdupload_document_analysis_upload__post"></a>

> Code samples

- shell
```shell
# You can also use wget
curl -X POST /analysis/upload/ \
  -H 'Content-Type: multipart/form-data' \
  -H 'Accept: application/json'
```

- http
```http
POST /analysis/upload/ HTTP/1.1

Content-Type: multipart/form-data
Accept: application/json
```

- javascript
```javascript
const inputBody = '{
  "file": "string"
}';
const headers = {
  'Content-Type':'multipart/form-data',
  'Accept':'application/json'
};

fetch('/analysis/upload/',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```

- ruby
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'multipart/form-data',
  'Accept' => 'application/json'
}

result = RestClient.post '/analysis/upload/',
  params: {
  }, headers: headers

p JSON.parse(result)
```

- python
```python
import requests
headers = {
  'Content-Type': 'multipart/form-data',
  'Accept': 'application/json'
}

r = requests.post('/analysis/upload/', headers = headers)

print(r.json())
```

- php
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'multipart/form-data',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/analysis/upload/', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```

- java
```java
URL obj = new URL("/analysis/upload/");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```

- go
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Content-Type": []string{"multipart/form-data"},
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("POST", "/analysis/upload/", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}

```

`POST /analysis/upload/`

*Upload a document*

Upload a document to the server and process it. The document will be saved, analyzed, and the extracted information will be stored.

> Body parameter

```yaml
file: string

```

<h3 id="upload_document_analysis_upload__post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_upload_document_analysis_upload__post](#schemabody_upload_document_analysis_upload__post)|true|none|

> Example responses

> 200 Response

```json
{
  "code": 200,
  "message": "File uploaded successfully",
  "data": {
    "title": "Example Title",
    "authors": [
      {
        "name": "Author One",
        "affiliation": "University of Examples"
      }
    ],
    "abstract": "This is an example of an abstract from the uploaded document.",
    "keywords": [
      "example",
      "document",
      "upload"
    ]
  }
}
```

> 422 Response

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

> 500 Response

```json
{
  "detail": "Could not save file"
}
```

<h3 id="upload_document_analysis_upload__post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Document uploaded and processed successfully.|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not found|None|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="upload_document_analysis_upload__post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_AuthorItemSchema">AuthorItemSchema</h2>
<!-- backwards compatibility -->
<a id="schemaauthoritemschema"></a>
<a id="schema_AuthorItemSchema"></a>
<a id="tocSauthoritemschema"></a>
<a id="tocsauthoritemschema"></a>

```json
{
  "id": 0,
  "name": "string",
  "count": 0
}

```

AuthorItemSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|The unique identifier of the author.|
|name|string|false|none|The name of the author.|
|count|integer|false|none|The number of papers by the author.|

<h2 id="tocS_AuthorResponse">AuthorResponse</h2>
<!-- backwards compatibility -->
<a id="schemaauthorresponse"></a>
<a id="schema_AuthorResponse"></a>
<a id="tocSauthorresponse"></a>
<a id="tocsauthorresponse"></a>

```json
{
  "code": 200,
  "msg": "success",
  "data": []
}

```

AuthorResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|The HTTP status code of the response.|
|msg|string|false|none|The message of the response.|
|data|[[AuthorItemSchema](#schemaauthoritemschema)]|false|none|The list of authors.|

<h2 id="tocS_AuthorSchema">AuthorSchema</h2>
<!-- backwards compatibility -->
<a id="schemaauthorschema"></a>
<a id="schema_AuthorSchema"></a>
<a id="tocSauthorschema"></a>
<a id="tocsauthorschema"></a>

```json
{
  "id": 0,
  "name": "string",
  "email": "string",
  "affiliation": "string"
}

```

AuthorSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|The unique identifier of the author.|
|name|string|false|none|The name of the author.|
|email|string|false|none|The email of the author.|
|affiliation|string|false|none|The affiliation of the author.|

<h2 id="tocS_Body_upload_document_analysis_upload__post">Body_upload_document_analysis_upload__post</h2>
<!-- backwards compatibility -->
<a id="schemabody_upload_document_analysis_upload__post"></a>
<a id="schema_Body_upload_document_analysis_upload__post"></a>
<a id="tocSbody_upload_document_analysis_upload__post"></a>
<a id="tocsbody_upload_document_analysis_upload__post"></a>

```json
{
  "file": "string"
}

```

Body_upload_document_analysis_upload__post

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|file|string(binary)|true|none|The document file to be uploaded.|

<h2 id="tocS_CitedConnectionItemSchema">CitedConnectionItemSchema</h2>
<!-- backwards compatibility -->
<a id="schemacitedconnectionitemschema"></a>
<a id="schema_CitedConnectionItemSchema"></a>
<a id="tocScitedconnectionitemschema"></a>
<a id="tocscitedconnectionitemschema"></a>

```json
{
  "from_paper": 0,
  "to_paper": []
}

```

CitedConnectionItemSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|from_paper|integer|true|none|The unique identifier of the paper.|
|to_paper|[integer]|false|none|The list of papers cited by the from paper.|

<h2 id="tocS_CitedTreeDataSchema">CitedTreeDataSchema</h2>
<!-- backwards compatibility -->
<a id="schemacitedtreedataschema"></a>
<a id="schema_CitedTreeDataSchema"></a>
<a id="tocScitedtreedataschema"></a>
<a id="tocscitedtreedataschema"></a>

```json
{
  "connections": [],
  "papers": []
}

```

CitedTreeDataSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|connections|[[CitedConnectionItemSchema](#schemacitedconnectionitemschema)]|false|none|The list of connections.|
|papers|[[PaperItemSchema](#schemapaperitemschema)]|false|none|The list of papers.|

<h2 id="tocS_CitedTreeResponseSchema">CitedTreeResponseSchema</h2>
<!-- backwards compatibility -->
<a id="schemacitedtreeresponseschema"></a>
<a id="schema_CitedTreeResponseSchema"></a>
<a id="tocScitedtreeresponseschema"></a>
<a id="tocscitedtreeresponseschema"></a>

```json
{
  "code": 200,
  "msg": "success",
  "data": {}
}

```

CitedTreeResponseSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|The HTTP status code of the response.|
|msg|string|false|none|The message of the response.|
|data|[CitedTreeDataSchema](#schemacitedtreedataschema)|false|none|The data of the response.|

<h2 id="tocS_CoAuthorConnectionItemSchema">CoAuthorConnectionItemSchema</h2>
<!-- backwards compatibility -->
<a id="schemacoauthorconnectionitemschema"></a>
<a id="schema_CoAuthorConnectionItemSchema"></a>
<a id="tocScoauthorconnectionitemschema"></a>
<a id="tocscoauthorconnectionitemschema"></a>

```json
{
  "author": 0,
  "papers": []
}

```

CoAuthorConnectionItemSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|author|integer|false|none|The unique identifier of the author.|
|papers|[integer]|false|none|The list of papers by the author.|

<h2 id="tocS_CoAuthorDataSchema">CoAuthorDataSchema</h2>
<!-- backwards compatibility -->
<a id="schemacoauthordataschema"></a>
<a id="schema_CoAuthorDataSchema"></a>
<a id="tocScoauthordataschema"></a>
<a id="tocscoauthordataschema"></a>

```json
{
  "connections": [],
  "authors": [],
  "papers": []
}

```

CoAuthorDataSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|connections|[[CoAuthorConnectionItemSchema](#schemacoauthorconnectionitemschema)]|false|none|The list of connections.|
|authors|[[AuthorSchema](#schemaauthorschema)]|false|none|The list of authors.|
|papers|[[PaperItemSchema](#schemapaperitemschema)]|false|none|The list of papers.|

<h2 id="tocS_CoAuthorResponseSchema">CoAuthorResponseSchema</h2>
<!-- backwards compatibility -->
<a id="schemacoauthorresponseschema"></a>
<a id="schema_CoAuthorResponseSchema"></a>
<a id="tocScoauthorresponseschema"></a>
<a id="tocscoauthorresponseschema"></a>

```json
{
  "code": 200,
  "msg": "success",
  "data": {}
}

```

CoAuthorResponseSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|The HTTP status code of the response.|
|msg|string|false|none|The message of the response.|
|data|[CoAuthorDataSchema](#schemacoauthordataschema)|false|none|The data of the response.|

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_PaperItemSchema">PaperItemSchema</h2>
<!-- backwards compatibility -->
<a id="schemapaperitemschema"></a>
<a id="schema_PaperItemSchema"></a>
<a id="tocSpaperitemschema"></a>
<a id="tocspaperitemschema"></a>

```json
{
  "id": 0,
  "title": "string",
  "authors": []
}

```

PaperItemSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|The unique identifier of the paper.|
|title|string|false|none|The title of the paper.|
|authors|[[AuthorSchema](#schemaauthorschema)]|false|none|The authors of the paper.|

<h2 id="tocS_PaperResponse">PaperResponse</h2>
<!-- backwards compatibility -->
<a id="schemapaperresponse"></a>
<a id="schema_PaperResponse"></a>
<a id="tocSpaperresponse"></a>
<a id="tocspaperresponse"></a>

```json
{
  "code": 200,
  "msg": "success",
  "data": []
}

```

PaperResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|The HTTP status code of the response.|
|msg|string|false|none|The message of the response.|
|data|[[PaperItemSchema](#schemapaperitemschema)]|false|none|The list of papers.|

<h2 id="tocS_SameTopicConnectionItemSchema">SameTopicConnectionItemSchema</h2>
<!-- backwards compatibility -->
<a id="schemasametopicconnectionitemschema"></a>
<a id="schema_SameTopicConnectionItemSchema"></a>
<a id="tocSsametopicconnectionitemschema"></a>
<a id="tocssametopicconnectionitemschema"></a>

```json
{
  "topic": 0,
  "papers": []
}

```

SameTopicConnectionItemSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|topic|integer|false|none|The unique identifier of the topic.|
|papers|[integer]|false|none|The list of papers in the topic.|

<h2 id="tocS_SameTopicDataSchema">SameTopicDataSchema</h2>
<!-- backwards compatibility -->
<a id="schemasametopicdataschema"></a>
<a id="schema_SameTopicDataSchema"></a>
<a id="tocSsametopicdataschema"></a>
<a id="tocssametopicdataschema"></a>

```json
{
  "connections": [],
  "topics": [],
  "papers": []
}

```

SameTopicDataSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|connections|[[SameTopicConnectionItemSchema](#schemasametopicconnectionitemschema)]|false|none|The list of connections.|
|topics|[[TopicSchema](#schematopicschema)]|false|none|The list of topics.|
|papers|[[PaperItemSchema](#schemapaperitemschema)]|false|none|The list of papers.|

<h2 id="tocS_SameTopicResponseSchema">SameTopicResponseSchema</h2>
<!-- backwards compatibility -->
<a id="schemasametopicresponseschema"></a>
<a id="schema_SameTopicResponseSchema"></a>
<a id="tocSsametopicresponseschema"></a>
<a id="tocssametopicresponseschema"></a>

```json
{
  "code": 200,
  "msg": "success",
  "data": {}
}

```

SameTopicResponseSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|The HTTP status code of the response.|
|msg|string|false|none|The message of the response.|
|data|[SameTopicDataSchema](#schemasametopicdataschema)|false|none|The data of the response.|

<h2 id="tocS_TopicItemSchema">TopicItemSchema</h2>
<!-- backwards compatibility -->
<a id="schematopicitemschema"></a>
<a id="schema_TopicItemSchema"></a>
<a id="tocStopicitemschema"></a>
<a id="tocstopicitemschema"></a>

```json
{
  "id": 0,
  "topic": "string",
  "count": 0
}

```

TopicItemSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|The unique identifier of the topic.|
|topic|string|false|none|The name of the topic.|
|count|integer|false|none|The number of papers in the topic.|

<h2 id="tocS_TopicResponse">TopicResponse</h2>
<!-- backwards compatibility -->
<a id="schematopicresponse"></a>
<a id="schema_TopicResponse"></a>
<a id="tocStopicresponse"></a>
<a id="tocstopicresponse"></a>

```json
{
  "code": 200,
  "msg": "success",
  "data": []
}

```

TopicResponse

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|code|integer|false|none|The HTTP status code of the response.|
|msg|string|false|none|The message of the response.|
|data|[[TopicItemSchema](#schematopicitemschema)]|false|none|The list of topics.|

<h2 id="tocS_TopicSchema">TopicSchema</h2>
<!-- backwards compatibility -->
<a id="schematopicschema"></a>
<a id="schema_TopicSchema"></a>
<a id="tocStopicschema"></a>
<a id="tocstopicschema"></a>

```json
{
  "id": 0,
  "name": "string"
}

```

TopicSchema

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|none|The unique identifier of the topic.|
|name|string|false|none|The name of the topic.|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[anyOf]|true|none|none|

anyOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|string|false|none|none|

or

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» *anonymous*|integer|false|none|none|

continued

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|none|
|type|string|true|none|none|

