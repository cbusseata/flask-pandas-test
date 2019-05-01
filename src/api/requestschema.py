organizations = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "organizations",
    "type": "object",
    "properties": {
        "id": {
            "anyOf": [
                {
                    "type": "integer"
                },
                {
                    "type": "string",
                    "pattern": "^\\d*$"
                }
            ]
        },
        "name": {
            "type": "string",
            "minLength": 1
        },
        "city": {
            "type": "string",
            "minLength": 1
        },
        "state": {
            "type": "string",
            "length": 2,
			"pattern": "^[A-Z]{2}$"
        },
        "postal": {
            "anyOf": [
                {
                    "type": "integer"
                },
                {
                    "type": "string",
                    "pattern": "^\\d*$"
                }
            ]
        },
        "orderby": {
			"type": "string",
		    "enum": [
				"id",
				"name",
                "city",
                "state",
                "postal"
            ]
        },
        "direction": {
			"type": "string",
		    "enum": [
				"ASC",
                "DSC"
            ]
        }
    },
    "additionalProperties": False
}
