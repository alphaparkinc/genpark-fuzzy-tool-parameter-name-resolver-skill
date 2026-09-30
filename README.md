# genpark-fuzzy-tool-parameter-name-resolver-skill

Fuzzy argument key alignment matching misspelled or near-match parameter names to target schema definitions.

## Architecture

```mermaid
flowchart LR
    Inputs["Model Args: {'qury': 'AI'}"] --> Matcher[difflib.get_close_matches]
    Schema["Allowed Schema: ['query', 'limit']"] --> Matcher
    Matcher --> Clean["Resolved Args: {'query': 'AI'}"]
```

## Features
- **Configurable Cutoff**: Flexible similarity thresholds.
- **Pure Python**: 100% standard library.
