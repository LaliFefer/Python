import csv
import json



def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return 0


def write_people_to_csv(people, filename='people.csv'):
    headers = ['שם פרטי', 'שם משפחה', 'גיל', 'מקום מגורים']

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(people)

    print(f"הנתונים נכתבו בהצלחה לקובץ {filename}")


def write_and_read_json(data, filename='data.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    with open(filename, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)

    print("הנתונים שנקראו מהקובץ:")
    print(json.dumps(loaded_data, ensure_ascii=False, indent=4))
    return loaded_data


if __name__ == "__main__":
    print(count_words_in_file("example.txt"))

    people_list = [
        ["דוד", "כהן", 30, "תל אביב"],
        ["שרה", "לוי", 25, "חיפה"],
        ["יוסי", "פרץ", 40, "ירושלים"]
    ]
    write_people_to_csv(people_list)


    sample_data = {"שם": "דנה", "גיל": 29, "עיר": "באר שבע"}
    write_and_read_json(sample_data)  

