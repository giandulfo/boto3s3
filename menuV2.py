while True:             
    print("S3 Automation Main Menu".center(80, "—"))
    print("1. List Buckets")
    print("2. Create a Bucket")
    print("3. Delete a Bucket")
    print("4. Exit")
    
    selection = input("\n\n~~>What would you like to do?: \n\n")

    if selection == "1":
        import listBuckets
    elif selection == "2":
        import createBucket
    elif selection == '3':
        import deletingBucket
    elif selection == "4" or "Exit" or "exit":       
        break  


# Add a confirmation message for each option? 