import csv
rows=[]
with open("main.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]
print(headers)
print(star_data_rows[0])
headers[0] = "row_num"

temp_star_data_rows = list(star_data_rows)
for star_data in temp_star_data_rows:
  if star_data[1].lower() == "hd 100546 b":
    star_data_rows.remove(star_data)
    
final_dict = {}
for index,star_data in enumerate(star_data_rows):
  features_list = []
  gravity = (float(star_data[3])*5.972e+24)/(float(star_data[7])*float(star_data[7])*6371000*6371000)*6.674e-11
  try:
    if gravity>50 or gravity<350:
      features_list.append("gravity")
  except:
    pass
  try:
    distance = 2*3.14*(star_data[2]*1.496e+9)
    if distance<200:
      features_list.append("distance")
  except:
    pass
  final_dict[index] = features_list

print(final_dict)

fig1 = px.bar(x=star_names, y=star_masses, color="blue")
fig2 = px.bar(x=star_names, y=star_radiuses, color="yellow")
fig3 = px.bar(x=star_names, y=star_distance, color="orange")
fig4 = px.bar(x=star_names, y=star_gravity, color="red")
fig1.show()
fig2.show()
fig3.show()
fig4.show()