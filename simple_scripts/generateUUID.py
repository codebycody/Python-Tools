import uuid
import argparse

def generate_unique_uuid(used_uuids=None):
    # Ensure used_uuids is a set for fast lookup if provided
    if used_uuids is None:
        used_uuids = set()
    else:
        used_uuids = set(used_uuids)

    # Generate a new UUID
    new_uuid = uuid.uuid4()

    # Check if the UUID already exists in used_uuids
    while new_uuid in used_uuids:
        new_uuid = uuid.uuid4()  # Regenerate if a collision occurs

    return new_uuid

def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate a unique UUID.')
    parser.add_argument(
        '-u', '--used-uuids', nargs='*', help='List of already used UUIDs.', default=[]
    )
    return parser.parse_args()

def main():
    # Parse command-line arguments
    args = parse_arguments()
    
    # Convert input UUID strings to UUID objects
    used_uuids = [uuid.UUID(u) for u in args.used_uuids]

    # Generate and print the unique UUID
    new_uuid = generate_unique_uuid(used_uuids)
    print(new_uuid)

if __name__ == '__main__':
    main()
