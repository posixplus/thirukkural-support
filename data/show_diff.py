import json

# Load the files
with open('T1.json', 'r', encoding='utf-8') as f1, open('T2_all.json', 'r', encoding='utf-8') as f2:
    t1_data = json.load(f1)
    t2_data = json.load(f2)

# Convert T1 array to a dictionary mapped by "Number" for easy lookup
t1_dict = {item["Number"]: item for item in t1_data["kural"]}

for key, t2_item in t2_data.items():
    number = t2_item.get("0_number")
    
    if number in t1_dict:
        t1_item = t1_dict[number]
        
        # 1. Compare T1 Line1/Line2 with T2 1_line1/1_line2
        if t1_item.get("Line1") != t2_item.get("1_line1"):
            print(f"Diff in Kural {number} Line 1:\n T1: {t1_item.get('Line1')}\n T2: {t2_item.get('1_line1')}\n")
            
        if t1_item.get("Line2") != t2_item.get("1_line2"):
            print(f"Diff in Kural {number} Line 2:\n T1: {t1_item.get('Line2')}\n T2: {t2_item.get('1_line2')}\n")
            
        # 2. Internal validation in T2: Does 1_kural match 1_line1 and 1_line2?
        kural_array = t2_item.get("1_kural", [])
        if len(kural_array) == 2:
            if kural_array[0] != t2_item.get("1_line1") or kural_array[1] != t2_item.get("1_line2"):
                print(f"Internal mismatch in T2 for Kural {number}:")
                print(f" Lines: '{t2_item.get('1_line1')}' | '{t2_item.get('1_line2')}'")
                print(f" Kural: '{kural_array[0]}' | '{kural_array[1]}'\n")

