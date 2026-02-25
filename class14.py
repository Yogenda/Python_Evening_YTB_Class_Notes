dirty_data = ["  PROD_99_old  ", "prod_88_OLD", "  pRoD_77_OlD  ", " PROD_66 "]
'''
# not optimized
print(dirty_data)
cleaned_list = []
for item in dirty_data:
    step1 = item.strip()
    step2 = step1.upper()
    step3 = step2.replace("_OLD","_ACTIVE")
    if "_ACTIVE" not in step3:
        step3 = step3+"_NEW"
    cleaned_list.append(step3)
print(cleaned_list)
final_string = ""
for code in cleaned_list:
    final_string+=code+"|"
print(final_string)
'''
'''
#optimized
cleaned_data=[]
for item in dirty_data:
    code = item.strip().upper().replace("_OLD","_ACTIVE")
    if "_ACTIVE" not in code:
        code+="_NEW"
    cleaned_data.append(code)
final_output ="|".join(cleaned_data)
print(f"Sanitized data: {final_output}")
'''
# name = "yogen bi"
# print(name.title())

# card = "1234-5678-9012-3456"
# rem = card.replace(card[:15],"xxxx-xxxx-xxxx-")
# print(rem)

# url = "http://codingyogendrabire.com"
# if not url.startswith("https"):
#     print("its not safe")
# if url.endswith(".com"):
#     print("its globally avaialbe")
