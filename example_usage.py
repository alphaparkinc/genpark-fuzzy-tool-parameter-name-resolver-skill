from client import FuzzyParameterResolver

params = {"usr_id": "123", "usrname": "alice"}
schema = ["user_id", "username", "email"]
res = FuzzyParameterResolver.resolve_parameters(params, schema)
print("Resolved parameters:", res["resolved_parameters"])
