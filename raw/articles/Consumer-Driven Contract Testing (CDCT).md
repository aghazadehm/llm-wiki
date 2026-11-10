---
title: "Consumer-Driven Contract Testing (CDCT)"
source: "https://medium.com/insiderengineering/consumer-driven-contract-testing-cdct-b6c05c18ba25"
author:
  - "[[Mihriban Kumarci]]"
published: 2024-03-18
created: 2026-10-16
description: "Consumer-Driven Contract (CDC) Testing is gaining prominence in microservices architecture. It offers an efficient way to ensure that services meet their contracts without exhaustive end-to-end tests."
tags:
  - "clippings"
---
## Consumer-Driven Contract (CDC) Testing is gaining prominence in microservices architecture. It offers an efficient way to ensure that services meet their contracts without exhaustive end-to-end tests.

![](https://miro.medium.com/v2/resize:fit:1400/1*ZC5jgpyKIju5g-vWyFnMcg.png)

Contract testing is a testing methodology that ensures that two services are compatible and can communicate with each other. It checks whether the relationship between the consumer and provider complies with the contract. Here are 3 keywords:

> **Provider:** It often represents a microservice or a service that provides specific functionality in the context of microservices
> 
> **Consumer:** A component that utilizes the services provided by a provider. In the context of microservices, a consumer is typically another microservice or a client application that consumes the functionality exposed by a provider.
> 
> **Contract:** The agreement or set of rules that govern the interaction between a provider and a consumer. The contract generally specifies the expected behavior, data formats, security requirements etc.

In a typical contract testing scenario, contract tests are often executed as part of the provider’s continuous integration (CI) pipeline. The responsibility for maintaining the contracts and writing the contract tests often lies with the consumer team.

**Why Consumer Driven Contract Testing?**

- It supports **independent development and deployment** of provider and consumer components.

I mean that communication is of great importance in a work environment with multiple teams. Sometimes we may experience incidents that unintentionally affect other teams. Giving due importance to contracts speeds up development cycles by reducing inter-team dependencies and enabling teams to work simultaneously.

- It reveals clearly the areas each consumer is interested in.

Contracts specify the endpoints, data formats, and behaviors that each consumer expects from the provider. By examining these contracts, teams gain clear visibility into the exact requirements of each consumer.

- It is easy to debug and fix.

If a contract test fails, it indicates a deviation from the expected behavior, making it easy to pinpoint the source of the issue.

![](https://miro.medium.com/v2/resize:fit:1400/1*1fom4I6EuFVhkA1TqXkkgA.png)

Source: https://pactflow.io/blog/contract-testing-vs-integration-testing/

It is important to remember that contract testing is only one piece of the puzzle. Creating robust and reliable software systems requires a comprehensive testing approach that includes a variety of testing methodologies. Some important types of testing such as unit testing, integration testing, and user acceptance testing complement contract testing.

**How do we perform a contract test?**

[PACT](https://docs.pact.io/) is a tool for testing interactions between service consumers and providers in a microservices architecture. However, it is also possible to establish this contract test structure without using Pact.

In this Postman test case, we can control various aspects of the API response, such as response structure, expected texts, and errors.

```c
pm.test('Status code is 200', function () {
    pm.response.to.have.status(200);
})

pm.test('Response is an object', () => {
    pm.expect(pm.response.json().constructor.name).to.eql('Object');
})

var responseSchema = {
    'type': 'object',
    'properties': {
        'data': {
            'type': 'object',
            'properties': {
                'noSearch': { 'type': 'number' },
                'search': { 'type': 'number' },
                'searchResults': { 'type': 'object' }
            }
        }
    }
};

var jsonData = pm.response.json();

pm.test('Ensure expected response structure', function () {
    var validation = tv4.validate(jsonData, responseSchema);
    pm.expect(validation).to.be.true;
    pm.test('noSearch is a number', function () {
        pm.expect(typeof jsonData.data.noSearch).to.eql('number');
    });
    pm.test('search is a number', function () {
        pm.expect(typeof jsonData.data.search).to.eql('number');
    });
    pm.test('searchResults is a object', function () {
        pm.expect(typeof jsonData.data.searchResults).to.eql('object');
    });
})

pm.test('Response body should contain specific text', function () {
    var searchResultType = jsonData.data.searchResults.searchResultFound.searchResultType;
    pm.expect(searchResultType).to.include('searchResultFound');
});
```

A similar example is written in Java;

```c
public class ContractTest extends Base {

    public static String PAYLOAD = "/SearchReport";
    public static String REQUEST_URL = Url.search_report;
    public static String CONTRACT = "/expectedResponseBody/SearchReportResponseContract";
    
    public static final String BASE_PATH = Paths.get("").toAbsolutePath().toString();
    public static String ReadFile(String PATH) {
        try {
            String content = Files.readString(Paths.get(BASE_PATH, "src", "test", "resources", "payloads", PATH + ".json"));
            return normalizeJson(content);
        } catch (IOException e) {
            System.out.println("ERROR");
            throw new RuntimeException(e);
        }
    }

    private static String normalizeJson(String json) throws IOException {
        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper.enable(SerializationFeature.ORDER_MAP_ENTRIES_BY_KEYS);
        JsonNode tree = objectMapper.readTree(json);
        return objectMapper.writeValueAsString(tree);
    }
    
    @Test
    public void searchReport() throws IOException, ParseException {

        Response providerResponse = sendRequest(REQUEST_URL, requestJson(PAYLOAD));
        int statusCode = providerResponse.getStatusCode();
        System.out.println("Response Status Code: " + statusCode);
        Assert.assertEquals("Status code is not 200. Actual status code: " + statusCode, 200, statusCode);
    }

    @Test
    public void compareParameterInResponse() throws IOException, ParseException {

        Response providerResponse = sendRequest(REQUEST_URL, requestJson(PAYLOAD));

        // Parse the expected JSON contract
        String expectedResponse = ReadFile(CONTRACT);
        String expectedDataNoSearch = JsonPath.from(expectedResponse).getString("data.noSearch");
        String expectedDataSearch = JsonPath.from(expectedResponse).getString("data.search");
        int expectedResultTotalSearch = JsonPath.from(expectedResponse).getInt("data.searchResults.searchResultFound.totalSearch");

        // Convert the actual response to a JSON string
        String actualResponse = providerResponse.getBody().asString();

        String actualDataNoSearch = JsonPath.from(actualResponse).getString("data.noSearch");
        String actualDataSearch = JsonPath.from(actualResponse).getString("data.search");
        int actualResultTotalSearch = JsonPath.from(actualResponse).getInt("data.searchResults.searchResultFound.terms[0].totalSearch");
        int actualResultTotalSearch1 = JsonPath.from(actualResponse).getInt("data.searchResults.searchResultFound.terms[1].totalSearch");
        int TotalActualResultTotalSearch = actualResultTotalSearch + actualResultTotalSearch1;

        Assert.assertEquals("Value of data.noSearch is not as expected", expectedDataNoSearch, actualDataNoSearch);
        Assert.assertEquals("Value of data.search is not as expected", expectedDataSearch, actualDataSearch);
        Assert.assertEquals("Sum of terms' totalSearch are not equal to expected value!", expectedResultTotalSearch, TotalActualResultTotalSearch);

    }
}
```

## Conclusion

I briefly explained the contract-driven test and its difference from other tests. If you have any questions, feel free to ask away in the comments or reach me at [https://www.linkedin.com/in/mihribanokumus/](https://www.linkedin.com/in/mihribanokumus/)

If you would like to learn Grafana & Prometheus Fundamentals, you can visit [https://medium.com/insiderengineering/grafana-prometheus-fundamentals-9aff7a9beb0b](https://medium.com/insiderengineering/grafana-prometheus-fundamentals-9aff7a9beb0b)