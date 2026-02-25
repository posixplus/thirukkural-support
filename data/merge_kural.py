import json

# Load the base file (truth for spelling and existing fields)
with open('thirukkural.json', 'r', encoding='utf-8') as f:
    thirukkural_data = json.load(f)

# Load the file with additional information
with open('all_thirukkural_information.json', 'r', encoding='utf-8') as f:
    all_info_data = json.load(f)

merged_kurals = []

# Fields we want to pull over if they exist in all_info (ignoring redundant ones like 5_mv)
# You can add or remove keys from this list if you find more commentaries you want
keys_to_add = [
    "6_parimela", 
    "6_manikudavar", 
    "6_v_munusami", 
    "6_kalaignar",
    "6_solomon_pappaiyah",
    "1_kural"
]

# Process each kural
for base_kural in thirukkural_data['kural']:
    kural_number = str(base_kural['Number'])
    
    # Get the corresponding extra info from the other file
    extra_info = all_info_data.get(kural_number, {})
    
    # Create a new dictionary for the merged kural to keep the order intact
    merged_kural = dict(base_kural)
    
    # Add the missing fields
    for key in keys_to_add:
        if key in extra_info:
            merged_kural[key] = extra_info[key]
            
    merged_kurals.append(merged_kural)

# Wrap it in the same structure as the original thirukkural.json
final_output = {
    "kural": merged_kurals
}

# Save the merged data to a new file
with open('merged.json', 'w', encoding='utf-8') as f:
    json.dump(final_output, f, ensure_ascii=False, indent=4)

print(f"Successfully merged {len(merged_kurals)} Kurals into 'merged.json'!")