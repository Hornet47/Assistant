get_current_weather = {
    "name": "get_current_weather",
    "description": "Get the weather in location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state e.g. San Francisco, CA",
            },
            "unit": {"type": "string", "enum": ["c", "f"]},
        },
        "required": ["location"],
    },
}
