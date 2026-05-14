from collections import defaultdict

def data_source(records):
    for r in records: yield r

def filter_empty(records):
    for r in records:
        if r.strip(): yield r

def parse_records(records):
    for r in records:
        try:
            name, subj, grade = r.split(",")
            yield {"student": name, "subject": subj, "grade": int(grade)}
        except ValueError: continue

def filter_passed(records, min_grade=60):
    for r in records:
        if r["grade"] >= min_grade: yield r

def format_output(records):
    for r in records:
        yield f"[{r['subject']}] {r['student']}: {r['grade']} балів"

def main():   
    pipeline = format_output(filter_passed(parse_records(filter_empty(data_source(SAMPLE_DATA))), 75))
    for line in pipeline: print(line)

    subject_grades = defaultdict(list)
    for r in parse_records(filter_empty(data_source(SAMPLE_DATA))):
        subject_grades[r["subject"]].append(r["grade"])

    print("\n=== Середній бал ===")
    for s, g in sorted(subject_grades.items()):
        print(f"  {s}: {sum(g)/len(g):.1f}")
