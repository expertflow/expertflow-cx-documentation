---
audience: [administrator]
doc-type: how-to
difficulty: intermediate
aliases: []
---

# Accessing Kubernetes Logs

This guide explains how to view OTLP-formatted logs from Expertflow CX applications running in a Kubernetes environment.

## Prerequisites
- `kubectl` configured for the target cluster.
- Deployment permissions for the `expertflow` namespace.

## Steps

### 1. Identify the Target Pod
List all running pods to find the one you need to inspect:
```bash
kubectl get pods -n expertflow
```

### 2. View Live Logs
Stream the logs for a specific pod:
```bash
kubectl logs -f <pod-name> -n expertflow
```

### 3. Filtering Logs
Use `grep` to isolate specific event types:
- **Audit Logs**: `kubectl logs <pod-name> -n expertflow | grep "audit_logging"`
- **Tracing**: `kubectl logs <pod-name> -n expertflow | grep "tracing"`

## Common Pod Prefixes
- `ef-ccm-*`: Core Conversation Manager
- `ef-agent-manager-*`: Agent state and session management
- `ef-unified-admin-*`: Admin interface backend
- `*-connector-*`: Individual channel connectors
