import json

def merge_kural_files(target_file, source_file, output_file):
    # Load the target file (thirukkural.json - the one to be fixed)
    with open(target_file, 'r', encoding='utf-8') as f1:
        data1 = json.load(f1)

    # Load the source of truth file (thirukkural 2.json - the accurate version)
    with open(source_file, 'r', encoding='utf-8') as f2:
        data2 = json.load(f2)

    # Create a lookup dictionary from thirukkural 2.json based on the 'Number'
    accurate_kurals = {item['Number']: item for item in data2.get('kural', [])}

    # Iterate through the first file and update Line1 and Line2
    updated_count = 0
    for item in data1.get('kural', []):
        kural_num = item.get('Number')
        
        # If the kural exists in the accurate file, update the lines
        if kural_num in accurate_kurals:
            accurate_kural = accurate_kurals[kural_num]
            
            if 'Line1' in accurate_kural:
                item['Line1'] = accurate_kural['Line1']
            if 'Line2' in accurate_kural:
                item['Line2'] = accurate_kural['Line2']
                
            updated_count += 1

    # Save the corrected data to a new file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # ensure_ascii=False keeps the Tamil text intact instead of using unicode escapes
        json.dump(data1, outfile, ensure_ascii=False, indent=4)

    print(f"Successfully processed {updated_count} Kurals.")
    print(f"Saved the corrected data to '{output_file}'.")

# File paths
file1_path = 'thirukkural.json'
file2_path = 'thirukkural 2.json'
output_path = 'thirukkural_merged.json'

# Execute the merge
merge_kural_files(file1_path, file2_path, output_path)