#!/usr/bin/env python3
from uuid_extensions import uuid7, uuid7str
from random import choice, randint
from datetime import datetime, timedelta
import json

directory = "minio_init"
number_of_files = 100
max_number_of_lines = 1000
user_ids = [
    '123e4567-e89b-12d3-a456-426614174000',
    '123e4567-e89b-12d3-a456-426614174001',
    '123e4567-e89b-12d3-a456-426614174002',
    '123e4567-e89b-12d3-a456-426614174003',
    '123e4567-e89b-12d3-a456-426614174004',
]
pages = [
    "home",
    "about",
    "contact",
    "blog",
    "login",
    "register",
]

for i in range(number_of_files):
    print(f"Generating file {i}...")
    file_id = uuid7str()
    file_name = f"{directory}/file_{file_id}.jsonl"
    print(f"File name: {file_name}")
    number_of_lines = randint(100, max_number_of_lines)
    with open(file_name, "w") as f:
        for j in range(number_of_lines):
            event_id = uuid7str()
            user_id = choice(user_ids)
            page = choice(pages)
            timestamp = datetime.now() + timedelta(seconds=j)
            line = {
                "id": event_id,
                "user_id": user_id,
                "page": page,
                "timestamp": timestamp.isoformat(),
            }
            json_line = json.dumps(line)
            f.write(json_line + "\n")
