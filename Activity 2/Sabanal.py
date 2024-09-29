def compute_average():
    # Input scores for each subject
    try:
        math_score = float(input("Enter Math score: "))
        science_score = float(input("Enter Science score: "))
        english_score = float(input("Enter English score: "))
        
        # Calculate the average
        average = (math_score + science_score + english_score) / 3
        
        # Print the average
        print(f"The average score is: {average:.2f}")
    except ValueError:
        print("Please enter valid numeric scores.")

