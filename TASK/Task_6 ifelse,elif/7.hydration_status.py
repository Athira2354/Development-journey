urine_color_scale=int(input("enter the urine color scale: "))
if urine_color_scale<3:
    print("Well-Hydrated")
elif urine_color_scale<6:
    print("Mild-Dehydration ")
else:
    print("severe Dehydration")
