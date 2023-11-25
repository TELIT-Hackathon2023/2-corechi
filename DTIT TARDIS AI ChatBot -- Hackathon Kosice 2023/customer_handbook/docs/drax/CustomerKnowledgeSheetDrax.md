# Guardians Drax Knowledge-Sheet 

[[_TOC_]]

## What has to be done?
You have to connect your application to a Drax-Collector endpoint 
(for the available URLs see [environment overview](https://developer.telekom.de/docs/src/tardis_customer_handbook/StarGate_Environment_Overview/#drax-jaeger-collector)).

The [jaeger-client libraries are being retired](https://www.jaegertracing.io/docs/1.35/client-libraries/), so you should no longer use them.
The collector still supports [all formats via different endpoints](https://developer.telekom.de/docs/src/tardis_customer_handbook/StarGate_Environment_Overview/#drax-jaeger-collector). 

!!! important
    Currently, T‧AR‧D‧I‧S supports [B3 HTTP Headers](https://github.com/opentracing/specification/blob/master/rfc/trace_identifiers.md#b3-http-headers)!
    [Trace-Context HTTP Headers](https://github.com/opentracing/specification/blob/master/rfc/trace_identifiers.md#trace-context-http-headers) aren´t completely supported. 
    We´re working on it.

See the following example implementations below.


## Golang using OpenTelemetry SDK 

OpenTelemetry provides for many languages standardized tracing libraries and more. 
Additionally OpenTelemetry supports many big player like Zipkin and Jaeger.
That´s why OpenTelemetry can be a good choice.

The [documentation](https://opentelemetry.io/docs/instrumentation/go/getting-started/) of OpenTelemetry already provides a good example.
That´s why we created a sample app which combines a consumer and provider connection and can be enriched by Stargate in between.
Additionally, this app can use several endpoints like Jaeger collector HTTP, Jaeger agent thrift compact or OpenTelemetry HTTP.

See the sample app [image repo](https://gitlab.devops.telekom.de/dhei/teams/skoll/dev/images/drax/sample-go-tracing-with-otel) and [helm chart repo](https://gitlab.devops.telekom.de/dhei/teams/skoll/dev/charts/drax/sample-tracing-app).

## Golang using Drax zipkin endpoint

See sample [image repo](https://gitlab.devops.telekom.de/dhei/teams/skoll/dev/images/drax/sample-go-tracing-with-zipkin) and [helm chart repo](https://gitlab.devops.telekom.de/dhei/teams/skoll/dev/charts/drax/sample-tracing-app).

This example is using the [go zipkin library](https://pkg.go.dev/github.com/openzipkin/zipkin-go) and the zipkin endpoint directly.

#### Endpoint instrumentation

The reporter will send the spans to the zipkin endpoint.

```gotemplate
import httpreporter "github.com/openzipkin/zipkin-go/reporter/http"

url = url + cfg.Host + ":" + strconv.Itoa(cfg.Port) + "/api/v2/spans"
reporter := httpreporter.NewReporter(url)

// defer reporter.Close()
// -> will be done via returned func from SetTraceProvider()
defer zipkinRpShutdown()
```

#### Create a new tracer

```gotemplate
import "github.com/openzipkin/zipkin-go"

endpoint, err := zipkin.NewEndpoint(serviceName, "localhost:0")

// provider.Reporter is the instrumentated reporter from httpreporter.NewReporter()
tr, err := zipkin.NewTracer(provider.Reporter, zipkin.WithLocalEndpoint(provider.Endpoint))
```

#### Create the first span

```gotemplate
	spanName := "run-zipkin-consumer"
	span := tr.StartSpan(spanName)
	defer span.Finish()
```

#### Create a child span

```gotemplate
	spanName := "call-zipkin-provider"
	span := tr.StartSpan(spanName, zipkin.Parent(spanCtx))
	defer span.Finish()
```

## Java SpringBoot using Drax zipkin endpoint
See sample project [sample-springboot-tracing-with-zipkin](https://gitlab.devops.telekom.de/dhei/teams/skoll/dev/images/drax/sample-springboot-tracing-with-zipkin).

An easy way can be to use the [zipkin library](https://zipkin.io/pages/tracers_instrumentation.html) and the zipkin endpoint directly.

#### Dependencies in pom.xml

````
<dependency>
  <groupId>org.springframework.cloud</groupId>
	<artifactId>spring-cloud-sleuth-zipkin</artifactId>
</dependency>
<dependency>
  <groupId>org.springframework.cloud</groupId>
	<artifactId>spring-cloud-starter-sleuth</artifactId>
</dependency>
````

#### Config in application.properties

````
#Tracing
spring.sleuth.sampler.probability=1.0
logging.pattern.level=%d{ABSOLUTE} [%X{traceId}/%X{spanId}] %-5p [%t] %C{2} - %m%n
spring.zipkin.service.name=my-zipkin-sample-service
spring.zipkin.sender.type=web
spring.zipkin.baseUrl=https://collector-zipkin-http-drax-guardians-playground.caas-t01.telekom.de:443/
````

#### TracingConfig

````
@Configuration
public class TracingConfig {

    @Bean
    public RestTemplate getRestTemplate() {
        return new RestTemplate();
    }
}
````

#### Controller

````
@RestController
public class GreetingController {

    @Autowired
    RestTemplate restTemplate;

    private static final String template = "Hello, %s!";
    private final AtomicLong counter = new AtomicLong();

    @GetMapping("/greeting")
    public Greeting greeting(@RequestParam(value = "name", defaultValue = "World") String name) {
        return new Greeting(counter.incrementAndGet(), String.format(template, name));
    }

    @GetMapping("/call-greeting")
    public Greeting callGreeting(@RequestParam(value = "name", defaultValue = "World") String name) {
        ResponseEntity<Greeting> response = restTemplate.getForEntity(
                "http://localhost:8080/greeting?name=" + name, Greeting.class);
        return response.getBody();
    }
}
````


## Java Quarkus using Drax http endpoint

#### Dependency in pom.xml

````
<dependency>
    <groupId>io.quarkus</groupId>
    <artifactId>quarkus-smallrye-opentracing</artifactId>
</dependency>
````

### Config in application.properties

````
#Tracing
quarkus.jaeger.service-name=myCoolService
quarkus.jaeger.sampler-type=const
quarkus.jaeger.sampler-param=1
quarkus.jaeger.endpoint=https://collector-http-drax-guardians.live.dhei.telekom.de/api/traces
quarkus.log.console.format=%d{HH:mm:ss} %-5p traceId=%X{traceId}, parentId=%X{parentId}, spanId=%X{spanId}, sampled=%X{sampled} [%c{2.}] (%t) %s%e%n
quarkus.jaeger.propagation=b3
````

### Java code

````
    @Traced
    public void myFunction( FlowMeterConfig config) {
        system.out.println("Here could be your traced code.")
    }
````

## Python using Drax zipkin endpoint
using [aiozipkin](https://github.com/aio-libs/aiozipkin)

````
import asyncio
import aiozipkin as az


async def run():
    # setup zipkin client
    zipkin_address = 'http://collector-zipkin-http-drax-guardians.live.dhei.telekom.de/api/v2/spans'
    endpoint = az.create_endpoint(
        "simple_service_python", ipv4="127.0.0.1", port=8080)
    tracer = await az.create(zipkin_address, endpoint, sample_rate=1.0)

    # create and setup new trace
    with tracer.new_trace(sampled=True) as span:
        # give a name for the span
        span.name("Slow SQL")
        # tag with relevant information
        span.tag("span_type", "root")
        # indicate that this is client span
        span.kind(az.CLIENT)
        # make timestamp and name it with START SQL query
        span.annotate("START SQL SELECT * FROM")
        # imitate long SQL query
        await asyncio.sleep(0.1)
        # make other timestamp and name it "END SQL"
        span.annotate("END SQL")

    await tracer.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
````
