#Lucia Castillo-Breton

#Inter Planetary Weights

n_Mercury_SGF = 0.38  #SGF: Surface Gravity Factor
n_Venus_SGF = 0.91
n_Moon_SGF = 0.165
n_Mars_SGF = 0.38
n_Jupiter_SGF = 2.34
n_Saturn_SGF = 0.93
n_Uranus_SGF = 0.92
n_Neptune_SGF = 1.12
n_Pluto_SGF = 0.066

#Name and Weight

s_Name = input("Enter name") #Lucia
s_Weight = input("Enter Weight on Earth")  #170
n_Weight_on_Earth = float(s_Weight) #Convert Weight to a Float

#Calculation Process

n_Weight_on_Mercury = n_Weight_on_Earth * n_Mercury_SGF
n_Weight_on_Venus = n_Weight_on_Earth * n_Venus_SGF
n_Weight_on_Moon = n_Weight_on_Earth * n_Moon_SGF
n_Weight_on_Mars = n_Weight_on_Earth *  n_Mars_SGF
n_Weight_on_Jupiter = n_Weight_on_Earth * n_Jupiter_SGF
n_Weight_on_Saturn = n_Weight_on_Earth * n_Saturn_SGF
n_Weight_on_Uranus = n_Weight_on_Earth * n_Uranus_SGF
n_Weight_on_Neptune = n_Weight_on_Earth * n_Neptune_SGF
n_Weight_on_Pluto = n_Weight_on_Earth * n_Pluto_SGF

#Output

print(f"\nWhat is your name? {s_Name}")
print(f"\What is your Weight on Earth? {s_Weight}")
print(f"/{s_Name}, this is your weight on our Solar System's Planet:")
print(f"Weight on Mercury:    {n_Weight_on_Mercury:.2f}")
print(f"Weight on Venus:      {n_Weight_on_Venus:.2f}")
print(f"Weight on Moon:       {n_Weight_on_Moon:.2f}")
print(f"Weight on Mars:       {n_Weight_on_Mars:.2f}")
print(f"Weight on Jupiter:    {n_Weight_on_Jupiter:.2f}")
print(f"Weight on Saturn:     {n_Weight_on_Saturn:.2f}")
print(f"Weight on Uranus:     {n_Weight_on_Uranus:.2f}")
print(f"Weight on Neptune:    {n_Weight_on_Neptune:.2f}")
print(f"Weight on Pluto:      {n_Weight_on_Pluto:.2f}")