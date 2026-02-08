from generated.models import create_dataset
from collections import Counter

def main():
    dataset = create_dataset()
    records = list(dataset)

    genders = Counter(r.demographics.gender for r in records if r.demographics.gender)
    dobs = [r.demographics.dob for r in records if r.demographics.dob]

    return {
        "total_records": len(records),
        "gender_distribution": dict(genders),
        "dob_sample_count": len(dobs),
        "unique_genders": len(genders)
    }

if __name__ == "__main__":
    result = main()
    print(result)
