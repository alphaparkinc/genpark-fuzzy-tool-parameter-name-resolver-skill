"""Fuzzy Tool Parameter Name Resolver.
100% Python Standard Library.
"""

import difflib

class FuzzyParameterResolver:
    """Resolves misspelled or hallucinated tool parameter names against schema definitions."""
    @staticmethod
    def resolve_parameters(input_params: dict, allowed_schema_params: list, cutoff: float = 0.6) -> dict:
        resolved = {}
        unresolved = []
        renamed = {}

        for k, v in input_params.items():
            if k in allowed_schema_params:
                resolved[k] = v
            else:
                matches = difflib.get_close_matches(k, allowed_schema_params, n=1, cutoff=cutoff)
                if matches:
                    best_match = matches[0]
                    resolved[best_match] = v
                    renamed[k] = best_match
                else:
                    unresolved.append(k)

        return {
            "resolved_parameters": resolved,
            "renamed_parameters": renamed,
            "unresolved_parameters": unresolved
        }
