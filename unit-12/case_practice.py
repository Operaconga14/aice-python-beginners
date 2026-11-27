name=" Joseph "
last_name= " kayode "
bio="i am a full stack developer who love to code and build saas peoduct"
full_name=f"{name} {last_name}"
cleaned_value=f"{full_name.strip().title()}"
full_bio=f"{full_name} {bio.upper()}"
original=f"{name} {last_name} {bio}"
print(original)
print(len(bio))
print(full_bio)
