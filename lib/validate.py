import json
import jsonschema
import sys 

def validate_json(file_path):
    try:
        with open(file_path, 'r') as f:
            print(f"Validating JSON file: {file_path}")
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON file: {e}")
        return False
    
    print("Done ☑")

    # Load the schema
    # with open('jsonschemas/records/record-v6.0.0.json', 'r') as f:
    #     schema = json.load(f)

    # # Validate the JSON data against the schema
    # try:
    #     jsonschema.validate(instance=data, schema=schema)
    #     print("JSON file is valid and conforms to the schema.")
    #     return True
    # except jsonschema.exceptions.ValidationError as e:
    #     print(f"JSON file does not conform to the schema: {e}")
    #     return False
    
if __name__ == "__main__":    
    if len(sys.argv) != 2:
      print("Usage: python validate.py <file_path>")
      sys.exit(1)   

    file_path = sys.argv[1]
    validate_json(file_path)  
  