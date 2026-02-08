# Auto-generated Python classes from archetype
# Loads dummy data from CSV file for testing

import csv
import os
from typing import Any, Dict, List, Optional


def create_dataset(csv_file=None):
    """Create a dataset from CSV dummy data"""
    if csv_file is None:
        # Default to dummy CSV file
        csv_file = 'generated/data.csv'
    
    if not os.path.exists(csv_file):
        print(f'CSV file not found: {csv_file}')
        print('Run "epsilon archetypes <dataset_id>" to generate dummy data')
        return DatasetWrapper([])
    
    # Load CSV data
    records = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
    
    print(f'Loaded {len(records)} dummy records from CSV')
    return DatasetWrapper(records)


class DatasetWrapper:
    """Wrapper for dataset records with easy access"""
    def __init__(self, records):
        self.records = records if isinstance(records, list) else [records]
    
    def __len__(self):
        return len(self.records)
    
    def __iter__(self):
        for record in self.records:
            yield Root(record)
    
    def __getitem__(self, index):
        return Root(self.records[index])
    
    @property
    def first(self):
        return Root(self.records[0]) if self.records else None


class Education:
    def __init__(self, data):
        self._data = data if data else {}

    @property
    def school_level(self):
        # Try direct access first (JSON format)
        if 'school_level' in self._data:
            return self._data['school_level']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.school_level'):
                return v
        return None


class Household:
    def __init__(self, data):
        self._data = data if data else {}

    @property
    def location(self):
        # Try direct access first (JSON format)
        if 'location' in self._data:
            return self._data['location']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.location'):
                return v
        return None


class Health:
    def __init__(self, data):
        self._data = data if data else {}

    @property
    def smoking_status(self):
        # Try direct access first (JSON format)
        if 'smoking_status' in self._data:
            return self._data['smoking_status']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.smoking_status'):
                return v
        return None


class Demographics:
    def __init__(self, data):
        self._data = data if data else {}

    @property
    def gender(self):
        # Try direct access first (JSON format)
        if 'gender' in self._data:
            return self._data['gender']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.gender'):
                return v
        return None

    @property
    def dob(self):
        # Try direct access first (JSON format)
        if 'dob' in self._data:
            return self._data['dob']
        # Try flattened access (CSV format)
        for k, v in self._data.items():
            if k.endswith('.dob'):
                return v
        return None


class Person:
    def __init__(self, data):
        self._data = data if data else {}


class Root:
    def __init__(self, data):
        self._data = data if data else {}

    @property
    def education(self):
        # Handle nested field access with dot notation
        if 'education' in self._data and isinstance(self._data['education'], dict):
            return Education(self._data['education'])
        # Handle flattened CSV data
        flattened = {}
        prefix = 'education.'
        for k, v in self._data.items():
            if k.startswith(prefix):
                nested_key = k[len(prefix):]
                flattened[nested_key] = v
        return Education(flattened)

    @property
    def household(self):
        # Handle nested field access with dot notation
        if 'household' in self._data and isinstance(self._data['household'], dict):
            return Household(self._data['household'])
        # Handle flattened CSV data
        flattened = {}
        prefix = 'household.'
        for k, v in self._data.items():
            if k.startswith(prefix):
                nested_key = k[len(prefix):]
                flattened[nested_key] = v
        return Household(flattened)

    @property
    def health(self):
        # Handle nested field access with dot notation
        if 'health' in self._data and isinstance(self._data['health'], dict):
            return Health(self._data['health'])
        # Handle flattened CSV data
        flattened = {}
        prefix = 'health.'
        for k, v in self._data.items():
            if k.startswith(prefix):
                nested_key = k[len(prefix):]
                flattened[nested_key] = v
        return Health(flattened)

    @property
    def demographics(self):
        # Handle nested field access with dot notation
        if 'demographics' in self._data and isinstance(self._data['demographics'], dict):
            return Demographics(self._data['demographics'])
        # Handle flattened CSV data
        flattened = {}
        prefix = 'demographics.'
        for k, v in self._data.items():
            if k.startswith(prefix):
                nested_key = k[len(prefix):]
                flattened[nested_key] = v
        return Demographics(flattened)

    @property
    def person(self):
        # Handle nested field access with dot notation
        if 'person' in self._data and isinstance(self._data['person'], dict):
            return Person(self._data['person'])
        # Handle flattened CSV data
        flattened = {}
        prefix = 'person.'
        for k, v in self._data.items():
            if k.startswith(prefix):
                nested_key = k[len(prefix):]
                flattened[nested_key] = v
        return Person(flattened)
