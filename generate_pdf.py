import fitz

doc = fitz.open()  # new empty PDF
page = doc.new_page()

text = """Understanding Climate Change

Climate change refers to long-term shifts in temperatures and weather patterns. These shifts may be natural, such as through variations in the solar cycle. But since the 1800s, human activities have been the main driver of climate change, primarily due to burning fossil fuels like coal, oil and gas.

Burning fossil fuels generates greenhouse gas emissions that act like a blanket wrapped around the Earth, trapping the sun's heat and raising temperatures.

Examples of greenhouse gas emissions that are causing climate change include carbon dioxide and methane. These come from using gasoline for driving a car or coal for heating a building, for example. Clearing land and cutting down forests can also release carbon dioxide. Landfills for garbage are a major source of methane emissions. Energy, industry, transport, buildings, agriculture and land use are among the main emitters.
"""

# Simple text insertion handling newlines
y = 50
for line in text.split('\n'):
    if line.strip():
        page.insert_text((50, y), line, fontsize=12)
        y += 20
    else:
        y += 10 # smaller gap for empty lines

doc.save("data/Understanding_Climate_Change.pdf")
print("PDF created successfully at data/Understanding_Climate_Change.pdf")
