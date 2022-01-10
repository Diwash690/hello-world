
print("\nSwallow Speed Analysis: Version 1.0\n")
List = []
A = input("Enter the Next Reading: ").lower()



if A == "":
    print("No readings entered. Nothing to do.")
else:
    while A!="":
        if (A[0] == "u") and (A[1:].isdigit()):
            print("Reading saved")
            List.append(float(A[ 1:]) * 1.61)
            A = input("Enter the Next Reading: ").lower()
        elif (A[0] == "e") and (A[1:].isdigit()):
            print("Reading saved")
            List.append(float(A[1:]))
            A = input("Enter the Next Reading: ").lower()
        else:
            print("Invalid reading")

            A = input("Enter the Next Reading: ").lower()


    if (len(List) != 0):
        print("\nReading summary\n")
        print(len(List), "Reading Analysed\n")
        print(f"Max Speed: {max(List) / 1.61:.1f} MPH,  {max(List):.1f} KPH")
        print(f"Min Speed: {min(List) / 1.61:.1f} MPH,  {min(List):.1f} KPH")


        total_Reading = 0
        for i in range(0, len(List)):
            total_Reading = total_Reading + List[i]
        average_Reading = total_Reading / len(List)
        print(f"Avg Speed: {average_Reading / 1.61:.1f} MPH, {average_Reading:.1f} KPH.")
    else:
        print("Invalid Input! Try Again")
