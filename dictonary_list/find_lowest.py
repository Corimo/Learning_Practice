sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

lowest_subject = ""
marks = 10000

for subject in sample_dict:
    if marks > sample_dict.get(subject):
        marks = sample_dict.get(subject)
        lowest_subject = subject
    else:
        continue

print(lowest_subject)