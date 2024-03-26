from latex import generate_latex

data = [
    ["Возраст", "Вес", "Рост"],
    [5, 25, 130],
    [16, 66, 165],
    [45, 75, 178]
]

image_path = "HW2/artifacts/graphics.png"
latex_code = generate_latex(data, image_path)
print(latex_code)
