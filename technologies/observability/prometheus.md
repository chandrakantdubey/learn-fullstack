# Prometheus

**Role:** Primary | **Layer:** Metrics

## Mental model
Prometheus collects time-series metrics identified by metric names and labels, then evaluates PromQL queries and alerting rules.

## Learn
- counters, gauges, histograms
- labels and cardinality
- scrape model
- PromQL
- recording and alerting rules
- exporters
- federation/remote storage concepts

## Production
Use low-cardinality labels, histogram buckets suited to SLOs, recording rules for expensive queries, and alerts tied to actionable failure conditions rather than noise.

## Related
OpenTelemetry, Grafana, Kubernetes.
