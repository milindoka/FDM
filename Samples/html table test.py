# Your 2D list
d = [
    ["col1", "col2", "col3"],  # title row
    ["x1", "x2", "23/12/19"],
    ["y1", "y2", "11/03/17"],
    ["z1", "z2", "10/09/18"],
]

# Function to convert the 2D list to an HTML table
def list_to_html_table(data):
    html = "<table border='1'>\n"
    for row in data:
        html += "  <tr>\n"
        for cell in row:
            html += f"    <td>{cell}</td>\n"
        html += "  </tr>\n"
    html += "</table>"
    return html

# Convert the list to an HTML table
html_table = list_to_html_table(d)

# Save the HTML table to a file
with open("output_table.html", "w") as file:
    file.write(html_table)

print("HTML table saved to output_table.html")
